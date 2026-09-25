"""Counts the two word-limited parts of the memo under three conventions.

The competition sets two hard limits:
  * the memo body (sections 1-6)  -> must be 2,000-2,500 words
  * the justification             -> must be 500 words or fewer

The rulebook does not say how a word is counted, so this checks every
reasonable convention and tests each limit against the least favourable one:

  K1  every whitespace-separated token counts (a lone dash counts)
  K2  only tokens containing a letter or digit count
  K3  as K2, but hyphen-, dash- and slash-joined compounds are split
      ("price-to-book" = 3, "FY21-FY25" = 2)

The ceilings are checked against the highest count, the floor against the
lowest. Run directly to see the counts:  python tools/wordcount.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEMO = REPO / "submission" / "memo.md"

BODY_LO, BODY_HI, JUST_MAX = 2000, 2500, 500
JOINERS = "-–—/"


def render(text):
    """Strip markdown syntax so the text matches what a reader sees."""
    text = re.sub(r"<div[^>]*></div>", " ", text)
    lines = []
    for line in text.split("\n"):
        if line.strip() == "---" or line.strip().startswith("!["):
            continue
        line = re.sub(r"^#+\s*", "", line).replace("**", "").replace("*", "")
        lines.append(line)
    return "\n".join(lines)


def k1(text):
    return len(text.split())


def k2(text):
    return sum(1 for w in text.split() if any(c.isalnum() for c in w))


def k3(text):
    parts = (p for w in text.split() for p in re.split("[" + re.escape(JOINERS) + "]", w))
    return sum(1 for p in parts if any(c.isalnum() for c in p))


def slice_between(text, start, end):
    return text[text.index(start):text.index(end)]


def regions(path=MEMO):
    t = Path(path).read_text(encoding="utf-8")
    body = render(slice_between(t, "## 1. Recommendation", "# Final Recommendation Box"))
    just = render(slice_between(t, "## Justification", "*All financial figures"))
    return body, just


def all_counts(path=MEMO):
    """Return {'body': {K1, K2, K3}, 'just': {K1, K2, K3}}."""
    body, just = regions(path)
    return {name: {"K1": k1(s), "K2": k2(s), "K3": k3(s)}
            for name, s in (("body", body), ("just", just))}


def counts(path=MEMO):
    """Return the least favourable (highest) body and justification counts."""
    c = all_counts(path)
    return max(c["body"].values()), max(c["just"].values())


def report(path=MEMO):
    """Print every convention and return True if all limits hold under all of them."""
    c = all_counts(path)
    b, j = c["body"], c["just"]
    # A marker may also count the To/From/Date/Subject block, so the ceiling must hold with it.
    t = Path(path).read_text(encoding="utf-8")
    hdr = render(slice_between(t, "# Investment Committee Memo", "## 1. Recommendation"))
    with_hdr = max(b[k] + f(hdr) for k, f in (("K1", k1), ("K2", k2), ("K3", k3)))
    body_ok = min(b.values()) >= BODY_LO and max(b.values()) <= BODY_HI and with_hdr <= BODY_HI
    just_ok = max(j.values()) <= JUST_MAX
    print("                              K1     K2     K3    worst   limit")
    print(f"  memo body (sections 1-6) {b['K1']:6d} {b['K2']:6d} {b['K3']:6d} {max(b.values()):7d}   "
          f"{BODY_LO}-{BODY_HI}  {'OK' if body_ok else 'OUT OF RANGE'}"
          f"  ({BODY_HI - max(b.values())} spare)")
    print(f"  body + memo header                            {with_hdr:7d}   "
          f"max {BODY_HI}  {'OK' if with_hdr <= BODY_HI else 'OVER LIMIT'}  ({BODY_HI - with_hdr} spare)")
    print(f"  justification            {j['K1']:6d} {j['K2']:6d} {j['K3']:6d} {max(j.values()):7d}   "
          f"max {JUST_MAX}   {'OK' if just_ok else 'OVER LIMIT'}"
          f"  ({JUST_MAX - max(j.values())} spare)")
    return body_ok and just_ok


if __name__ == "__main__":
    sys.exit(0 if report() else 1)
