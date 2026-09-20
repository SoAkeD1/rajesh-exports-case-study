"""Counts the two word-limited parts of the memo.

The competition sets two hard limits:
  * the memo body (sections 1-6)  -> must be 2,000-2,500 words
  * the justification             -> must be 500 words or fewer

Run directly to see the counts:  python tools/wordcount.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEMO = REPO / "submission" / "memo.md"

BODY_LO, BODY_HI, JUST_MAX = 2000, 2500, 500


def count(text):
    """Word count, ignoring markdown punctuation and HTML scaffolding."""
    text = re.sub(r"<div[^>]*></div>", " ", text)
    text = re.sub(r"[#*_|`>-]", " ", text)
    return len([w for w in text.split() if any(c.isalnum() for c in w)])


def slice_between(text, start, end):
    return text[text.index(start):text.index(end)]


def counts(path=MEMO):
    """Return (body_words, justification_words)."""
    t = Path(path).read_text(encoding="utf-8")
    body = slice_between(t, "## 1. Recommendation", "# Final Recommendation Box")
    just = slice_between(t, "## Justification", "*All financial figures")
    return count(body), count(just)


def report(path=MEMO):
    """Print the counts and return True if both limits are satisfied."""
    body, just = counts(path)
    body_ok = BODY_LO <= body <= BODY_HI
    just_ok = just <= JUST_MAX
    print(f"  memo body (sections 1-6) : {body:>5}   limit {BODY_LO}-{BODY_HI}"
          f"   {'OK' if body_ok else 'OUT OF RANGE'}")
    print(f"  justification            : {just:>5}   limit {JUST_MAX} max"
          f"        {'OK' if just_ok else 'OVER LIMIT'}")
    return body_ok and just_ok


if __name__ == "__main__":
    sys.exit(0 if report() else 1)
