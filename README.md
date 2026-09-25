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

A refinery is paid a fee per ounce of gold it handles. So its fee tracks *how much*
gold passes through, not what gold is worth. Watch what the two numbers do.

| | FY21 | FY25 | Change |
|---|---|---|---|
| Revenue the group credits to its overseas arms | ₹2,56,245 cr | ₹4,16,072 cr | **up 62%** |
| Valcambi's own audited revenue | ₹586 cr | ₹427 cr | **down 27%** |

The top row's 62% rise roughly matches the rise in the rupee gold price over the
same years. So the *amount* of gold handled was about flat — the rise is mostly
price. But if the amount of gold was flat, a per-ounce fee should have stayed flat
too. Instead the refinery's own audited line **fell 27%**. The company's "you are
comparing different things" defence explains why one number is *bigger* than the
other; it does not explain that fall.

There is a fair objection here, and the memo answers it rather than ducking it.
The table above is not strictly like-for-like: the top row covers *all* the
overseas companies, the bottom row covers only Valcambi. So perhaps the gold
business simply shifted to a different company in the group, and Valcambi's own
figures shrank for innocent reasons.

Possibly. But that reply costs the company something. It means the revenue now
sits in companies that have **no stated gold-refining operations at all** — which
moves the question rather than answering it. And it would be settled instantly
by one disclosure: a breakdown of revenue company by company. That breakdown has
never been provided.

### Reason 2 — the profit collapsed while the revenue grew

When the gold price rises, a bullion trader's profit *percentage* shrinks — the
same fee is now a smaller slice of a bigger number. But its profit *in rupees*
should hold up. Here, profit in rupees nearly vanished.

| | FY23 | FY25 |
|---|---|---|
| Consolidated revenue | ₹3,39,690 cr | ₹4,23,099 cr (**+24.6%**) |
| Consolidated profit | ₹1,432 cr | ₹95 cr (**−93.4%**) |
| Margin | 0.42% | **0.02%** |

There is a sharper version of this. In FY25 the *Indian* parent company — the one
that is audited in India and that anyone can inspect — earned a 0.34% margin.
The overseas arms, which nobody can inspect, earned **0.017%**. The part we can
check behaves like a normal business. The part we cannot, does not.

"That's just business mix," someone will say — jewellery earns more than refining.
But in FY22 the overseas arms actually earned a *higher* margin than the parent
(0.42% against 0.37%). So mix does not explain the FY25 gap.

Again there are innocent explanations, and again the memo names them: the company
may have lost money on stock it was holding, or on hedging, or taken a one-off
write-off. Any of those is possible. But none has been disclosed, and a one-off
charge would not repeat across two years of falling rupee profit.

### Reason 3 — gold that big cannot move invisibly

This one is counter-intuitive, so read it twice.

At the international gold price of about ₹70,000 per 10 grams (LBMA, converted at
RBI rates), FY25's ₹4,23,099 crore of revenue works out to about **600 tonnes of
gold value**. World gold supply in calendar 2024 — which covers nine months of FY25 — was 4,962
tonnes (World Gold Council), so
that is about 12% — large but genuinely possible for a major refinery. It does
**not** prove anything is wrong, and the memo says so plainly.

But here is the thing: *if* that much gold really moved, then vault receipts, purity
certificates, shipping papers, insurance documents and matching bank transfers
exist in enormous quantity, held by outside parties in several countries. Even gold
that is traded on paper, without moving, still leaves invoices and bank transfers.
**The paperwork is not optional — it is unavoidable.** The regulator says it asked
for it repeatedly and was not given it. The company says documents will follow; the
case records none yet.

The obvious reply is that the paperwork is confidential — it names customers and
suppliers, and companies do not hand that around. True, and it still does not
work. A reconciliation statement and an auditor's sign-off name nobody at all, and
the key reconciliation belongs to the Indian parent company, so Swiss secrecy rules
do not cover it. Confidentiality explains why the records are not *published*. It
does not explain why they were not *handed over* when asked.

That is why the physical scale argument, flipped around, is the strongest point
in the memo rather than the weakest.

### Why not just sell, or just wait?

- **Why not "wait and see"?** Because waiting is not free. If the investigation
  ends badly, the share price hits its daily fall limit and there is nobody to
  sell to. You would be stuck holding it — all of the downside, none of the
  ability to act.
- **Why not simply "sell"?** Selling is part of the answer — the memo sells too.
  The difference is the rule attached. Plain selling says "this looks unsuitable".
  "Uninvestable" adds a gate: no buying back at *any* price until the missing
  records are independently checked.

"Uninvestable" is the only answer that both removes the risk **and** says, in
plain testable terms, exactly what evidence would bring the company back. The
memo lists six such items, sets a size threshold on each so they cannot be
satisfied with a token sample, and commits to looking again when the forensic
report is published or at the next audited results, whichever comes first. That last
part matters: a verdict with no review date is not a judgement, it is a grudge.

---

## 5. What is in this repository

```
rajesh-exports-case-study/
├── README.md                  <- you are here
├── submission/
│   ├── memo.md                <- THE SUBMISSION, in editable text form
│   ├── Inferno_Mahi.pdf        <- the same thing as a finished PDF (9 pages)
│   └── figures/               <- the memo's two charts, as PNG images
├── docs/
│   ├── case-explained-simply.pdf  <- START HERE if you know nothing
│   ├── explainer.html         <- the source for that PDF
│   ├── 01-the-competition.md  <- rules, deadlines, what must be handed in
│   ├── 02-the-case.md         <- the case explained, with all the source data
│   ├── 03-the-analysis.md     <- the full reasoning and every calculation
│   ├── 04-building-the-pdf.md <- how the PDF is generated
│   └── 05-glossary.md         <- every finance term, in plain English
├── tools/
│   ├── build.py               <- turns memo.md into the final PDF
│   ├── charts.py              <- draws the two charts in submission/figures/
│   └── wordcount.py           <- checks both word limits under three counting conventions
└── build/                     <- generated files (not tracked by git)
```

**If you only open one file, open [`submission/memo.md`](submission/memo.md).**
That is the actual entry. Everything else exists to explain or produce it.

**If finance is not your subject**, open
[`docs/case-explained-simply.pdf`](docs/case-explained-simply.pdf) instead. It is a
12-page illustrated walkthrough with flowcharts and everyday examples — a juice
stall, a corner shop, an airport money-changer — that assumes you know nothing
about finance, the competition, or the problem. Rebuild it after editing
`docs/explainer.html` with:

```bash
"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="docs/case-explained-simply.pdf" "docs/explainer.html"
```

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
python tools/build.py Inferno_Mahi
```

which writes `submission/Inferno_Mahi.pdf`.

The memo has two charts (page 4). They are already saved in `submission/figures/`,
so the build just embeds them. Only if you change the chart data, redraw them first
(this one step needs `pip install matplotlib`):

```bash
python tools/charts.py
```

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

- [ ] **Fill in the placeholders on page 1** of `submission/memo.md` — the
      member names, colleges, emails and phones (`[MEMBER 2]`, `[COLLEGE]`,
      `[EMAIL]`, `[PHONE]`), and delete any unused rows.
- [ ] **Do not commit the filled-in page 1.** This repository is public, so
      committing it would publish every member's phone number and email.
- [ ] **Rebuild the PDF** with the registered names:
      `python tools/build.py Inferno_RegisteredLeaderName`
- [ ] **Open the PDF and read it** — confirm no `[PLACEHOLDER]` text survives.
- [ ] **Upload before 30 September, 11:59 PM** — ideally by 28 September.
      Late entries are not accepted under any circumstances.

Current status:

| Check | State |
|---|---|
| Memo body word count | 2,464 at the strictest convention — inside 2,000–2,500, 36 words spare (2,493 even if the To/From header is counted) |
| Justification word count | 486 at the strictest convention — inside the 500 cap, **14 words spare**; recheck after any edit |
| All six required sections present | Yes |
| Charts | Two, on page 4 — revenue vs Valcambi vs gold price, and revenue vs profit. They are images, so they add no words |
| One option ticked in the recommendation box | Yes — Option D, with a visible tick |
| Page 1 team details | **Placeholders — still to fill in** |
| Filename | `Inferno_Mahi.pdf` — matches the required TeamName_TLsName pattern |

---

## 8. A note on sources

Every company figure in the memo comes from the exhibits in the competition's own
case booklet (Exhibits 1–12). No news reporting or filings about any real company
were used. That was a deliberate choice: the case is fictionalised, so mixing in
real-world reporting would risk contradicting the organisers' own numbers, and the
marking rewards reasoning from the evidence given.

Two general reference figures come from outside the booklet, and the memo cites
both: the FY21 and FY25 international gold price (about ₹70,000 per 10 grams in FY25 — LBMA
Gold Price, converted at RBI reference rates) and calendar-2024 world gold supply (4,962
tonnes — World Gold Council, Gold Demand Trends Full Year 2025). They feed the tonnage
estimate in Reason 3, the price-versus-volume point in Reason 1, and the gold-price
line in Chart 1 (FY21–FY25 annual averages, approximate). The memo also cites the
Swiss Criminal Code (Articles 271 and 273) where it mentions Swiss blocking rules. The domestic
Indian price (around ₹80,000) is deliberately *not* used: it includes import duty
and GST, which do not apply to revenue earned overseas.
