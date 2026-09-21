"""Builds the submission PDF from submission/memo.md.

Pipeline:  memo.md  ->  build/memo.html  ->  submission/<name>.pdf

The HTML step is a small purpose-built markdown converter (only the handful of
markdown features this memo actually uses). The PDF step drives Microsoft Edge
in headless mode, which every Windows 11 machine already has -- no LaTeX,
no pandoc, no Word install required.

Usage:
    python tools/build.py                      # -> submission/Inferno_Mahi.pdf
    python tools/build.py Inferno_MahiFullName   # override the default name
"""
import html
import re
import subprocess
import sys
from pathlib import Path

import wordcount

REPO = Path(__file__).resolve().parent.parent
MEMO = REPO / "submission" / "memo.md"
BUILD = REPO / "build"

EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]

CSS = """
@page { size: A4; margin: 19mm 17mm; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt;
       line-height: 1.55; color: #1a1a1a; margin: 0; }
h1 { font-size: 17pt; margin: 0 0 10pt 0; padding-bottom: 5pt;
     border-bottom: 1.5pt solid #7a6320; letter-spacing: -0.2pt; }
h2 { font-size: 12pt; margin: 17pt 0 7pt 0; color: #5d4c18;
     page-break-after: avoid; letter-spacing: -0.1pt; }
p { margin: 0 0 8pt 0; text-align: left; }
strong { font-weight: 700; }
table { width: 100%; border-collapse: collapse; margin: 9pt 0 12pt 0;
        font-size: 9.5pt; page-break-inside: avoid; }
th { text-align: left; font-weight: 700; background: #f5f2e9;
     border-bottom: 1pt solid #b9a96f; padding: 5pt 7pt; }
td { border-bottom: 0.5pt solid #ddd; padding: 5pt 7pt; vertical-align: top; }
ol, ul { margin: 0 0 9pt 0; padding-left: 17pt; }
li { margin-bottom: 5pt; }
hr { border: 0; border-top: 0.5pt solid #d8d3c4; margin: 13pt 0; }
.pagebreak { page-break-after: always; }
.box { display: inline-block; width: 9pt; height: 9pt; border: 1pt solid #666;
       vertical-align: -1pt; margin-right: 3pt; }
.box.checked { background: #5d4c18; border-color: #5d4c18; position: relative; }
.box.checked::after { content: "✓"; color: #fff; font-size: 8pt;
       position: absolute; left: 1pt; top: -2pt; font-family: 'Segoe UI', sans-serif; }
em.note { font-size: 8.5pt; color: #666; }
"""


def smart_quotes(t):
    """Straight quotes to typographic ones. Word counts are unaffected."""
    t = re.sub(r"(?<=\w)'(?=\w)", "’", t)
    t = re.sub(r"(^|[\s(\[—–])\"", lambda m: m.group(1) + "“", t)
    t = t.replace('"', "”")
    t = re.sub(r"(^|[\s(\[—–])'", lambda m: m.group(1) + "‘", t)
    return t.replace("'", "’")


def inline(t):
    """Apply inline markdown (bold, italic) and the ballot-box glyphs."""
    t = html.escape(smart_quotes(t), quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = t.replace("\u2612", '<span class="box checked"></span>')
    t = t.replace("\u2610", '<span class="box"></span>')
    return t


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def to_html(src):
    out, lines, i = [], src.split("\n"), 0
    while i < len(lines):
        s = lines[i].strip()

        if not s:
            i += 1
            continue

        if s == '<div class="pagebreak"></div>':
            out.append(s)
            i += 1
            continue

        if s.startswith("#"):
            lvl = len(s) - len(s.lstrip("#"))
            out.append(f"<h{lvl}>{inline(s.lstrip('#').strip())}</h{lvl}>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", s):
            out.append("<hr>")
            i += 1
            continue

        # table: a pipe row followed by a |---|---| separator row
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            head = cells(s)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(cells(lines[i]))
                i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in head]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # ordered / unordered lists, including wrapped continuation lines
        ordered = re.match(r"^\d+\.\s+(.*)", s)
        if ordered or re.match(r"^[-*]\s+(.*)", s):
            tag = "ol" if ordered else "ul"
            pat = r"^\d+\.\s+(.*)" if ordered else r"^[-*]\s+(.*)"
            items = []
            while i < len(lines):
                m = re.match(pat, lines[i].strip())
                if not m:
                    if not lines[i].strip():
                        break
                    if items:
                        items[-1] += " " + lines[i].strip()
                        i += 1
                        continue
                    break
                items.append(m.group(1))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        # paragraph
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(#|\||-{3,}|\d+\.\s|[-*]\s|<div)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        if para:
            # a run of "**Label:** value" lines is a memo header -> keep line breaks
            is_header = all(re.match(r"^\*\*[^*]+:\*\*", p) for p in para)
            text = ("<br>" if is_header else " ").join(inline(p) for p in para)
            if para[0].startswith("*All financial"):
                out.append(f"<p><em class='note'>{text}</em></p>")
            else:
                out.append(f"<p>{text}</p>")

    return (f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Team Inferno — Rajesh Exports IC Memo</title>"
            f"<style>{CSS}</style></head><body>{''.join(out)}</body></html>")


def find_edge():
    for p in EDGE_CANDIDATES:
        if p.exists():
            return p
    sys.exit("Microsoft Edge not found. Open build/memo.html in any browser and "
             "print to PDF manually (Ctrl+P -> Save as PDF).")


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "Inferno_Mahi"
    pdf = REPO / "submission" / f"{name}.pdf"

    print("Checking word limits:")
    ok = wordcount.report()
    if not ok:
        print("\n  WARNING: a word limit is breached. Fix submission/memo.md before submitting.\n")

    BUILD.mkdir(exist_ok=True)
    page = BUILD / "memo.html"
    page.write_text(to_html(MEMO.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"\nWrote {page.relative_to(REPO)}")

    if pdf.exists():
        pdf.unlink()
    subprocess.run([str(find_edge()), "--headless", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                    page.as_uri()], check=True, capture_output=True)

    if not pdf.exists():
        sys.exit("Edge ran but produced no PDF.")
    print(f"Wrote {pdf.relative_to(REPO)}  ({pdf.stat().st_size / 1024:.1f} KB)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
