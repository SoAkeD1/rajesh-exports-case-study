# 4. Building the PDF

The submission is written as **Markdown** (plain text) and converted to PDF by a
script. This page explains why, how, and what to do when something breaks.

---

## Why not just write it in Word?

Three reasons:

1. **The word limits are hard limits.** 2,000–2,500 for the body, 500 for the
   justification. A script can check both every single time the document is
   built, so it is impossible to submit an over-length memo by accident.
2. **The text is version-controlled.** Markdown is plain text, so git can show
   exactly what changed between drafts. A `.docx` is a binary blob and git can
   only say "the file changed".
3. **Rebuilds are identical.** The same input always produces the same PDF. No
   manual formatting to redo when a sentence gets edited.

---

## What you need

| Requirement | Notes |
|---|---|
| **Python 3** | Standard library only — nothing to `pip install`. |
| **Microsoft Edge** | Pre-installed on every Windows 11 machine. Used in headless mode purely as a PDF printer. |

No LaTeX, no pandoc, no Word licence.

---

## The one command

```bash
python tools/build.py
```

This does three things in order:

1. Counts the memo body and the justification, and reports whether both are
   within their limits.
2. Converts `submission/memo.md` into `build/memo.html`.
3. Runs Edge headlessly to print that HTML to
   `submission/TeamName_TLsName.pdf`.

Expected output:

```
Checking word limits:
  memo body (sections 1-6) :  2185   limit 2000-2500   OK
  justification            :   483   limit 500 max        OK

Wrote build\memo.html
Wrote submission\TeamName_TLsName.pdf  (137.1 KB)
```

### Naming the file for submission

The rulebook requires the filename to be `TeamName_TLsName`. Pass it as an
argument:

```bash
python tools/build.py Vanguard_ShrimonMishra
```

That writes `submission/Vanguard_ShrimonMishra.pdf`.

### Checking word counts without rebuilding

```bash
python tools/wordcount.py
```

Useful while editing. It exits with an error code if either limit is breached,
so it can be wired into a pre-commit hook if you want.

---

## How the conversion actually works

### `tools/wordcount.py`

Slices `memo.md` into its two limited regions by searching for fixed markers:

- **Body** = from `## 1. Recommendation` up to `# Final Recommendation Box`
- **Justification** = from `## Justification` up to the closing source note

It then strips markdown punctuation (`#`, `*`, `|`, backticks and so on) and
counts anything left containing a letter or digit. The cover page, the section
headings' markup and the recommendation table are excluded, so the number
reflects prose the way a marker would count it.

> If you rename a heading in `memo.md`, update the markers in this file or the
> count will fail.

### `tools/build.py`

A small purpose-built Markdown converter. It deliberately supports only what
this memo uses:

| Markdown | Becomes |
|---|---|
| `# Heading`, `## Heading` | `<h1>`, `<h2>` |
| `**bold**`, `*italic*` | `<strong>`, `<em>` |
| `\| a \| b \|` tables | `<table>` with a styled header row |
| `1.` and `-` lists | `<ol>`, `<ul>` (wrapped lines are joined) |
| `---` | `<hr>` |
| `<div class="pagebreak"></div>` | a forced page break |
| `☒` / `☐` | a filled / empty tick box |

Consecutive lines that all look like `**Label:** value` are treated as a memo
header block and keep their line breaks instead of being joined into a
paragraph. That is what keeps To / From / Date / Subject on four separate lines.

The styling lives in the `CSS` string near the top of the file: A4 page, 19 mm
top and bottom margins, Georgia at 10.5 pt, and a dark-gold accent on headings
and table rules. Edit that string to change the look.

### The PDF step

```
msedge.exe --headless --disable-gpu --no-pdf-header-footer
           --print-to-pdf="<output>" "file:///<path to memo.html>"
```

`--no-pdf-header-footer` is what suppresses Edge's default date-and-URL strip
along the top and bottom of every page.

---

## Editing the memo

Open `submission/memo.md` in any text editor. A few things to respect:

- **Do not rename the six section headings.** The competition fixes them, and
  `wordcount.py` locates the body by searching for the first one.
- **Keep the tick box characters.** `☒` marks the chosen option, `☐` the others.
  Exactly one should be `☒`.
- **Re-run the build after every edit** and check the word counts.
- The placeholders on page 1 (`[TEAM NAME]`, `[COLLEGE]`, …) are ordinary text.
  Replace them in place.

---

## Troubleshooting

**"Microsoft Edge not found"**
The script checks both standard install paths. If Edge really is absent, open
`build/memo.html` in any browser and print manually: `Ctrl+P` → Destination
"Save as PDF" → set margins to Default → untick "Headers and footers".

**A word limit says OUT OF RANGE or OVER LIMIT**
The build still produces a PDF, but prints a warning and exits with an error
code. Edit the memo and rebuild. Do not submit until both report OK.

**The ₹ symbol renders as a box**
The font stack is Georgia → Times New Roman → generic serif. All three support ₹
on Windows 11. If you move this to Linux or macOS, add a font that covers the
Indian Rupee sign.

**A table is split across two pages**
Tables carry `page-break-inside: avoid`, so this should not happen. If a table
grows too tall for one page the rule is ignored by the browser — split the table
or shorten the rows.

**`python` is not recognised**
Try `py tools/build.py` instead, or install Python from python.org and tick
"Add Python to PATH" during setup.

---

## The `build/` folder

Intermediate output — currently just `memo.html`. It is regenerated on every run
and is excluded from git by `.gitignore`. Nothing in it needs to be kept, but it
is useful for debugging: open it in a browser to see exactly what Edge was asked
to print.
