# 1. The competition

Everything on this page comes from the organisers' official rulebook. It is
recorded here so anyone picking up this repository knows what the submission had
to satisfy.

---

## Who could enter

- Open to **all college students**, regardless of course or year.
- Teams of **2 to 4 members**.
- Members may come from **different colleges**.
- **Team composition is locked at registration** — no substitutions afterwards.

## The three rounds

| Round | What happens | Output |
|---|---|---|
| **1 — Online Quiz** | A 30-minute quiz testing knowledge, analysis and problem-solving. Teams are ranked; the top teams go through. | Quiz score |
| **2 — Case Study** | Shortlisted teams receive the case by email on 19 September 2026 and write an Investment Committee memo. **This repository is Round 2.** | A single PDF |
| **3 — Grand Finale** | Finalists get a *new* problem statement and present to a jury, live at Tech Zephyr, IIT Bhubaneswar. Judged on solution quality, analysis, creativity, feasibility and presentation. | A live presentation (expected to be a slide deck) |

Note that Round 3 is a fresh problem, not a continuation of this one. The
written format below applies to Round 2 only.

## What Round 2 required

| Requirement | Detail |
|---|---|
| Format | One **PDF** |
| Filename | `TeamName_TLsName` (TL = team leader) |
| Page 1 | Every member's name, their college/institution, and contact details |
| Memo body | **2,000–2,500 words**, in exactly six named sections |
| Justification | A **separate** piece, **500 words maximum**, with one option ticked |
| Deadline | **30 September, 11:59 PM** |

The six section names are fixed by the case booklet and cannot be renamed:

1. Recommendation
2. Situation Summary
3. Bull Case
4. Bear Case
5. Key Evidence Needed
6. Final Decision

## Submission rules

- Work must be **original and written specifically for this competition**.
- **Plagiarism, copied material, or reusing a previously submitted solution
  results in disqualification.**
- All external sources, data and statistics must be **properly cited**.
- **Late submissions are not accepted under any circumstances.**
- Teams are responsible for making sure the uploaded file is complete,
  openable and in the right format.

## Grounds for disqualification

A team may be disqualified for any of the following:

- Plagiarism or academic misconduct
- Submitting previously used or copied solutions
- Providing false or misleading information
- Breaching the submission guidelines or the deadline
- Unfair practices, or seeking an unauthorised advantage
- Disrupting proceedings or breaching the code of conduct

## Organiser authority

The organising committee may change the schedule, format or rules as needed.
All decisions on shortlisting, evaluation, qualification and disqualification
rest with the jury and organising committee, and are **final and binding**.
Entering the competition counts as accepting this.

## Key dates

| Stage | Date |
|---|---|
| Case study problem statement released | 19 September 2026 |
| **Case study submission due** | **30 September, 11:59 PM** |
| Grand Finale | During Tech Zephyr, IIT Bhubaneswar |

Participants were told to watch their registered email and the official channels
for announcements.

---

## How this repository maps onto the requirements

| Requirement | Where it is met | Status |
|---|---|---|
| Six named sections | [`submission/memo.md`](../submission/memo.md) | Done |
| 2,000–2,500 word body | 2,421 words — verified by `tools/wordcount.py` | Done |
| ≤ 500 word justification | 472 words — verified by the same script | Done |
| One option ticked | Option D, in the Final Recommendation Box | Done |
| Page 1 team details | Placeholders in `memo.md` | **Outstanding** |
| Correct filename | Set via `python tools/build.py TeamName_TLName` | **Outstanding** |
| Citations | Source note at the end of the memo | Done |
