# Rajesh Exports — Investment Committee Memo

**A finance case-study competition entry.** This repository holds the written
submission for Round 2 of a college case-study competition, plus every note and
script used to produce it.

> **Read this first.** The case is a *teaching exercise*. It was written by the
> competition organisers and is explicitly fictionalised: the investment fund
> ("Aarohan Capital"), its staff, and all the emails in the case are invented.
> Nothing in this repository is a statement of fact about any real company or
> person, and nothing here is investment advice. Every number used comes from
> the case booklet handed to participants — not from company filings, news
> reports, or any regulator's actual order.

---

## 1. What is this, in plain English?

A competition gave each team a made-up story with real-looking numbers and asked
them to make a decision, the way a professional investor would.

The story: an investment fund owns a small amount of shares in a gold company.
The government's markets regulator has just said it is not satisfied that the
company's sales figures are real. The fund's boss wants a written recommendation
by the end of the day — **keep the shares, sell them, buy more, or declare the
company impossible to analyse.**

Our job was to pick one and defend it in a 2,000–2,500 word memo.

**We picked: declare it impossible to analyse.** (Formally, "Option D — Forensic
Red Flag / Uninvestable".)

---

## 2. Understand the whole problem in 60 seconds

Imagine a corner shop tells you it sold **₹1 crore** of goods last year.

You say: *fine, show me the receipts.*

The shop shows you receipts totalling **₹20,000**.

The shop then explains: *"you have misunderstood — those receipts only record my
profit on each sale, not the full sale value."* That is a perfectly reasonable
explanation. It might even be true.

So you say: *fine, then show me the sales book, the supplier invoices, and your
bank statements.* And the shop does not.

That is this case, scaled up enormously. Over five years the company said its
overseas arms earned **₹15,18,413 crore**. The audited accounts of its main
overseas business, a Swiss gold refinery called Valcambi, show **₹3,027 crore** —
about **one five-hundredth** of the claim. The company says the regulator is
comparing two different kinds of number. The regulator says it asked for the
underlying records and did not get them.

**Our memo argues: the explanation might be right, but until the records appear,
nobody can put a value on this company at all — so a fund with a duty to its
clients should not own it.**

---

## 3. Some words you will need

You do not need a finance background to follow the memo. You do need six words.
A fuller list is in [`docs/05-glossary.md`](docs/05-glossary.md).

| Word | What it actually means |
|---|---|
| **Revenue** | Total money coming in from sales. Not profit. |
| **Profit (PAT)** | What is left after every cost and tax is paid. |
| **Margin** | Profit as a percentage of revenue. Sell for ₹100, keep ₹0.02 → a 0.02% margin. |
| **Subsidiary** | A company owned by another company. |
| **Standalone vs consolidated** | *Standalone* = the parent company alone. *Consolidated* = the parent plus everything it owns, added together. |
| **Audited** | Checked and signed off by an independent accounting firm. Unaudited numbers are just what management typed. |

---

## 4. The decision, and the three reasons behind it

The company's defence is genuinely reasonable, and the memo says so at length
before arguing against it. Gold refining really *is* a business where gigantic
revenue and near-zero profit are normal — melting and reselling gold means the
whole value of the metal flows through the books while you keep only a sliver.
So a huge revenue number with a tiny margin is **not**, by itself, suspicious.

Three facts are what break that defence.

### Reason 1 — the two sets of numbers move in opposite directions

If the group's giant revenue really comes from the Swiss refinery's activity,
then when one goes up the other must go up too. They do not.

| | FY21 | FY25 | Change |
|---|---|---|---|
| Revenue the group credits to its overseas arms | ₹2,56,245 cr | ₹4,16,072 cr | **up 62%** |
| Valcambi's own audited revenue | ₹586 cr | ₹427 cr | **down 27%** |

The company's "you are comparing different things" defence could explain why one
number is *bigger* than the other. It cannot explain why they move in **opposite
directions**. Something other than the refinery is driving the big number.

### Reason 2 — the profit collapsed while the revenue grew

A real trading business earns a thin but steady slice. More volume should mean
more profit. Here, revenue grew and profit nearly vanished.

| | FY23 | FY25 |
|---|---|---|
| Consolidated revenue | ₹3,39,690 cr | ₹4,23,099 cr (**+24.6%**) |
| Consolidated profit | ₹1,432 cr | ₹95 cr (**−93.4%**) |
| Margin | 0.42% | **0.02%** |

There is a sharper version of this. In FY25 the *Indian* parent company — the one
that is audited in India and that anyone can inspect — earned a 0.34% margin.
The overseas arms, which nobody can inspect, earned **0.017%**. The part we can
check behaves like a normal business. The part we cannot, does not.

### Reason 3 — gold that big cannot move invisibly

This one is counter-intuitive, so read it twice.

At roughly ₹80,000 per 10 grams, FY25's ₹4,23,099 crore of revenue works out to
about **530 tonnes of gold value**. Against world gold supply of roughly 4,800 tonnes
a year, that is large but genuinely possible for a major refinery — so it does
**not** prove anything is wrong. We say so plainly in the memo.

But here is the thing: *if* 530 tonnes of metal really moved, then vault receipts, purity
certificates, shipping papers, insurance documents and matching bank transfers
exist in enormous quantity, held by outside parties in several countries. Half a
thousand tonnes of gold cannot be moved quietly. **The paperwork is not optional —
it is unavoidable.** And it has not been produced.

That is why the physical scale argument, flipped around, is the strongest point
in the memo rather than the weakest.

### Why not just sell, or just wait?

- **Why not "wait and see"?** Because waiting is not free. If the investigation
  ends badly, the share price hits its daily fall limit and there is nobody to
  sell to. You would be stuck holding it — all of the downside, none of the
  ability to act.
- **Why not simply "sell"?** Selling treats this as a price problem, as if a
  cheaper price would fix it. It would not. The problem is that the financial
  statements themselves cannot be relied on, and that stays true at any price.

"Uninvestable" is the only answer that both removes the risk **and** says, in
plain testable terms, exactly what evidence would bring the company back. The
memo lists six such items.

---

## 5. What is in this repository

```
rajesh-exports-case-study/
├── README.md                  <- you are here
├── submission/
│   ├── memo.md                <- THE SUBMISSION, in editable text form
│   └── TeamName_TLsName.pdf   <- the same thing as a finished PDF
├── docs/
│   ├── 01-the-competition.md  <- rules, deadlines, what must be handed in
│   ├── 02-the-case.md         <- the case explained, with all the source data
│   ├── 03-the-analysis.md     <- the full reasoning and every calculation
│   ├── 04-building-the-pdf.md <- how the PDF is generated
│   └── 05-glossary.md         <- every finance term, in plain English
├── tools/
│   ├── build.py               <- turns memo.md into the final PDF
│   └── wordcount.py           <- checks the two word limits
└── build/                     <- generated files (not tracked by git)
```

**If you only open one file, open [`submission/memo.md`](submission/memo.md).**
That is the actual entry. Everything else exists to explain or produce it.

---

## 6. How to rebuild the PDF

You need Python 3 and Microsoft Edge. Both come with a standard Windows 11
machine, and nothing needs installing.

```bash
python tools/build.py
```

That single command checks both word limits, converts the memo to HTML, and
prints it to PDF. To name the file properly for submission:

```bash
python tools/build.py Vanguard_ShrimonMishra
```

which writes `submission/Vanguard_ShrimonMishra.pdf`.

To check the word counts without rebuilding:

```bash
python tools/wordcount.py
```

Full details, including what to do if Edge is unavailable, are in
[`docs/04-building-the-pdf.md`](docs/04-building-the-pdf.md).

---

## 7. Before submitting — checklist

The memo is written and both word limits are met. These items are **not** done
yet:

- [ ] **Fill in the placeholders on page 1** of `submission/memo.md` —
      `[TEAM NAME]`, `[TEAM LEADER NAME]`, and the four member rows
      (`[MEMBER 1]`, `[COLLEGE]`, `[EMAIL]`, `[PHONE]`).
- [ ] **Rebuild the PDF** with the correct filename:
      `python tools/build.py YourTeam_YourLeaderName`
- [ ] **Open the PDF and read it** — confirm no `[PLACEHOLDER]` text survives.
- [ ] **Upload before 30 September, 11:59 PM.** Late entries are not accepted
      under any circumstances.

Current status:

| Check | State |
|---|---|
| Memo body word count | 2421 — within the 2,000–2,500 limit (2421/2500, 79 to spare) |
| Justification word count | 472 — within the 500 limit |
| All six required sections present | Yes |
| One option ticked in the recommendation box | Yes — Option D |
| Page 1 team details | **Placeholders — still to fill in** |
| Filename | **Placeholder — still to set** |

---

## 8. A note on sources

Every figure in the memo comes from the exhibits in the competition's own case
booklet — Exhibits 1, 4, 5, 6, 8, 9, 11 and 12. No outside research was used.
That was a deliberate choice: the case is fictionalised, so mixing in real-world
reporting would risk contradicting the organisers' own numbers, and the marking
rewards reasoning from the evidence given.

The only two numbers from outside the booklet are the gold price
(≈ ₹80,000 per 10 grams) and annual world gold supply (≈ 4,800 tonnes), both used
for the tonnage estimate in Reason 3. Both are stated as assumptions in the memo
itself so that a reader can challenge them.
