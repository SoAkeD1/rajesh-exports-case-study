# 3. The analysis

How the memo gets from the exhibits to Option D, with every calculation shown so
it can be checked.

---

## The shape of the argument

The memo is deliberately built in this order:

1. **State the company's defence at its strongest.** Not a token paragraph — the
   real, best version, including the one argument that could genuinely exonerate
   it.
2. **Then break that specific argument** with three facts it cannot account for.
3. **Convert the finding into a portfolio decision** using the fund's duty to
   its clients, not moral outrage.
4. **Say exactly what would reverse the decision.**

This matters for marking. A memo that knocks down a weak version of the other
side looks like it has not understood the case. The bull case in this memo is
written to be genuinely persuasive before it is dismantled.

---

## Step 1: the strongest version of the company's defence

Gold refining is a **high-throughput, low-margin** business. When a refiner takes
ownership of metal, the full value of that metal passes through its revenue line
while it keeps only a sliver. Margins of a few hundredths of a percent are normal.

So the bull argument runs:

> Valcambi's standalone accounts may report revenue on a **net** basis — the
> refining fee only. The group consolidates on a **gross** basis — the full
> bullion value. Comparing the two is comparing a fee to a turnover. The gap is
> not missing money; the gap *is* the margin.

And here is what makes it genuinely strong rather than a dodge:

> If refining value-addition runs at about **0.2%** of metal value, then a net
> figure would be about **1/500th** of a gross one. The observed ratio is about
> **1/500th**. On this reading, the ratio is not an anomaly — it is exactly what
> the accounting would predict.

That coincidence is real and the memo says so. Any submission that ignores it
has not engaged with the case.

**Supporting bull points:** the order is only *interim*; "prima facie" is a low
bar; no restatement has happened; no auditor has resigned; and the company is
debt-free, so no lender can force a collapse before the facts emerge.

---

## Step 2: the three facts that break it

### Fact 1 — the two series move in opposite directions

Refining fees are usually charged **per ounce**. So a fee tracks *throughput* —
how much gold is handled — not the gold price. A rising price lifts gross revenue
and leaves the fee flat; only lower throughput cuts the fee. (This is also why the
net/gross ratio is *not* a fixed percentage: it falls whenever the price rises.)

```
Revenue credited to subsidiaries   FY21  2,56,245  ->  FY25  4,16,072
  4,16,072 / 2,56,245 - 1 = +62.4%                                UP

Valcambi SA audited revenue        FY21      586   ->  FY25      427
  427 / 586 - 1 = -27.1%                                        DOWN
```

Full series for Valcambi: 586 → 729 → 743 → 543 → 427. Note it *rose* until FY23;
the fall is FY23→FY25 (−42.5%), while attributed revenue rose 24.6% over the same
two years. The memo quotes that window rather than claiming a steady decline.

**Decompose the top line into price × volume.** The rupee gold price rose roughly
as much as attributed revenue over FY21–FY25:

```
FY21 average international gold price ~ $1,824/oz x Rs 74.2 / 31.1035 = Rs 4,350/g
FY25 average international gold price ~ $2,585/oz x Rs 84.6 / 31.1035 = Rs 7,029/g
price rise ~ +62%        attributed revenue rise +62.4%   ->  implied volume ~ flat

(cross-check with calendar-year LBMA averages: 2020 $1,774, 2024 $2,386 -> +52%)
```

So the attributed rise is mostly **price**, not volume. That is the company's best
point, and the memo concedes it. The anomaly that survives is the other line: at
flat volume a per-ounce fee should hold (or rise ~14% with the rupee), yet
Valcambi's audited line **fell 27%**, implying its own throughput fell roughly a
third. Gross-versus-net explains a gap in *level*; it cannot explain that fall.

The monthly prices above are reconstructed from LBMA averages and RBI rates; treat
them as approximate. The conclusion holds on either basis.

Chart 1 in the memo draws this. The gold-price line uses these approximate
fiscal-year averages (₹ per 10 g):

| | FY21 | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|---|
| Gold price, ₹/10 g (approx.) | 43,500 | 43,550 | 46,630 | 52,950 | 70,300 |
| Index, FY21 = 100 | 100 | 100 | 107 | 122 | 162 |
| Attributed revenue index | 100 | 92 | 130 | 107 | 162 |
| Valcambi audited index | 100 | 124 | 127 | 93 | 73 |

FY22–FY24 are estimates built the same way as FY21 and FY25; spot-check them
against RBI or LBMA data before relying on them in a question-and-answer session.

### Fact 2 — profit collapsed while revenue grew

```
Consolidated revenue   FY23  3,39,690  ->  FY25  4,23,099
  4,23,099 / 3,39,690 - 1 = +24.6%                                UP

Consolidated PAT       FY23     1,432  ->  FY25        95
  95 / 1,432 - 1 = -93.4%                                       DOWN

Margin: 0.42% -> 0.12% -> 0.02%
```

Careful here: revenue rising does **not** mean volume rising. The rupee gold price
rose about 51% over FY23→FY25 while revenue rose only 24.6%, so implied volume
actually *fell* around 17%. A rising price also compresses the margin *percentage*
mechanically — the same per-ounce spread becomes a smaller slice of a bigger number.

What price cannot explain is the fall in **rupee** profit. At a constant per-ounce
spread, FY25 PAT should be roughly 1,432 × 0.83 (volume) × 1.05 (rupee) ≈
₹1,245 crore — and margin about 0.29%. The reported figures are ₹95 crore and
0.02%. That gap is the robust fact, and it is what the memo leads with. Chart 2 in
the memo shows it: revenue bars beside profit bars, on separate scales.

The sharper version — comparing what we can inspect against what we cannot:

```
FY25 subsidiaries (opaque):  PAT 71 / revenue 4,16,072 = 0.0171%
FY25 Indian parent (audited):PAT 24 / revenue   7,027  = 0.342%

0.342 / 0.0171 = 20x
```

The Indian parent is audited under Indian rules and anyone can inspect it. It
earns a normal thin-trading margin. The overseas entities, which nobody can
inspect, earn a margin **twenty times worse**.

The obvious objection is business mix: jewellery manufacturing earns more than
refining, so the parent *should* out-earn the subsidiaries. The exhibits refute
it. In FY22 the subsidiaries earned 987 / 2,36,891 = **0.42%** while the parent
earned 23 / 6,237 = **0.37%**. If mix explained the FY25 gap, that could not happen.

### Fact 3 — gold at that scale cannot move without paperwork

This argument is built carefully, because the obvious version of it is wrong.

**The arithmetic:**

```
FY25 international gold price ~ Rs 70,000 per 10 grams (LBMA, at RBI rates)
  = Rs 7,000 per gram
  = Rs 7,000,000,000 per tonne
  = Rs 700 crore per tonne

FY25 consolidated revenue 4,23,099 crore / 700 = ~604 tonnes
FY25 subsidiary revenue   4,16,072 crore / 700 = ~594 tonnes
```

**Use the international price, not the domestic one.** The Indian domestic price
(around ₹80,000 per 10 g in FY25) includes import duty and GST, which do not apply
to revenue earned overseas.

| Gold price basis | ₹ crore per tonne | Implied tonnes | Share of 4,962 t |
|---|---|---|---|
| ₹64,000 / 10g (calendar 2024 LBMA average) | 640 | ~661 | 13.3% |
| ₹70,000 / 10g (FY25 international average) | 700 | ~604 | 12.2% |
| ₹80,000 / 10g (domestic, duty-inclusive — wrong basis) | 800 | ~529 | 10.7% |

World gold supply in calendar 2024 was **4,962 tonnes** (World Gold Council, Gold
Demand Trends Full Year 2025). Calendar 2024 is used because it covers nine of FY25's
twelve months; 2025's 5,002 tonnes gives the same answer. The implied volume is
roughly **11–13%** of world supply.

**The wrong conclusion:** "that is impossible, therefore the revenue is fake."
It is *not* impossible. Valcambi is one of the world's largest refineries and
throughput in the hundreds of tonnes is plausible. An argument built on
disbelieving the headline number would be attacked immediately and deserves to
be.

**The right conclusion — invert it.** Suppose the metal really did move. Then
there necessarily exist, in large volume and in several countries, held largely
by **third parties**:

- vault receipts and storage records
- assay (purity) certificates
- chain-of-custody documentation
- shipping and insurance papers
- counterparty invoices
- bank settlements matching those invoices

Six hundred tonnes of gold cannot be moved quietly. The documentation is not a
courtesy; it is operationally unavoidable, and much of it is not even in the
company's own control. Two caveats keep this honest: metal traded on paper
(unallocated) or re-traded several times produces no vault or shipping papers —
but it still produces **invoices and bank settlements**, which carry the argument
on their own.

So the bull case's own premise — that the scale is real — is what makes the
missing paperwork damning. A gross-versus-net dispute is resolved by **one
reconciliation schedule**. The regulator says it asked
repeatedly and was not given the records (Exhibit 7); the company says documents
will follow (Exhibit 9), and the case records none yet.

Exhibit 12 treats *refusal to share records* as bearish. "Not yet produced" is not
the same as "refused", and the memo keeps them apart — but even short of refusal,
non-production is not neutral when production would be cheap and immediately
exculpatory.

**Confidentiality and Swiss law.** Swiss blocking statutes (Criminal Code Arts.
271 and 273) restrict handing business records directly to a foreign authority,
so "hand them over under seal" is weaker than it sounds. The stronger answer: the
consolidation schedule is the Indian parent's own document, outside Swiss rules.

---

## Step 3: two structural points

**Revenue is booked at a holding company.** Exhibit 1 shows large revenues
attributed to **Global Gold Refineries SA**, which is a *holding* company, rather
than to Valcambi, the refinery that does the actual work. That is not
proof of anything: commodity groups often book sales in a trading entity while the
refinery earns a fee. But the company's reply (Exhibit 9) does not offer that
explanation, so the question stands.

**The consolidation itself was never auditable.** Ananya Menon asks why the group
relied on unaudited holding company consolidation numbers instead of visible
audited subsidiary accounts. Investors were asked to trust a consolidation they were never
permitted to examine. This is Ananya Menon's point in the case, and it is the
reason "show us the audited subsidiary accounts" is a threshold condition in the
memo rather than a nice-to-have.

**A minor governance note.** Capital going into ACC Energy Storage — an
unrelated, capital-intensive battery business — while the core revenue base is
unverified is a signal in its own right, and a cash drain that cannot be sized
from outside.

---

## Step 4: from finding to portfolio decision

This is where the memo converts analysis into an action, using the fund's
position rather than a moral judgement.

```
If 98.34% of revenue cannot be verified
   -> profit cannot be verified
      -> book value cannot be verified
         -> price-to-book and price-to-sales are not LOW, they are UNDEFINED
```

The original reason for owning the stock was that it "screened cheap". But a
screen divides the price by the reported figures — and those figures are exactly
what is in dispute. **The thesis was circular.**

One more figure makes the point that the scale never paid anybody:

```
Five-year cumulative consolidated revenue: 15,44,899 crore
Five-year cumulative consolidated PAT:          3,717 crore
Cumulative margin:                              0.24%
```

Five years of ranking among India's largest listed revenue generators produced
₹3,717 crore of profit. The fund was never paid for the scale — only exposed to it.

### Why D and not B (hold and wait)

Waiting is not a neutral act. If the forensic audit comes back adverse, the
share price hits successive lower circuits and there is no buyer. **You cannot
sell into the bad news.** So holding means accepting the full downside of an
adverse finding while giving up the ability to act on it. The optionality of
waiting is *negative*.

B's strongest form deserves respect: the order is interim, and the company has
promised documents (Exhibit 9). The memo's answer is not that B is foolish, but
that the cost of being wrong while holding cannot be undone once trading locks.

### Why D and not C (exit)

The case defines C as "the uncertainty around revenue quality, disclosures and
governance makes the stock unsuitable". D sells too. What D adds is a **formal
gate**: the name leaves the investable universe, so it cannot be bought back on
price alone, and the memo states exactly which independently obtained evidence
would readmit it — plus the triggers that would make the exclusion permanent.

### Why D is defensible rather than dramatic

The case is explicit: *"Your task is not to prove fraud."* Option D does not
allege fraud. It says:

> We cannot analyse this security. Therefore it cannot hold money we manage on
> behalf of other people. Here are the six specific, checkable things that would
> reverse that.

That is a disciplined conclusion, not an accusation — and the falsifiable
re-entry test is what separates it from panic.

---

## What the memo deliberately does *not* argue

Recording these matters, because avoiding bad arguments is part of the analysis:

| Tempting argument | Why it was rejected |
|---|---|
| "Revenue that big must be fake" | It is not implausible for a major refinery. The tonnage maths shows ~12% of world supply, which is large but achievable. Arguing from disbelief would be shot down. |
| "Tiny margins prove fraud" | Flatly untrue in bullion. This is exactly the mistake the broker warns against, and the case sets the trap deliberately. |
| "The regulator said so, so it is true" | The order is interim and *prima facie*. Treating an allegation as a finding is poor analysis. |
| "The share price crashed, so something is wrong" | Meera explicitly says not to tell her the stock is down. Price is not evidence. |
| Citing real-world news about the company | The case is fictionalised. Outside reporting could contradict the organisers' own exhibits, and the marking rewards reasoning from the evidence supplied. |

---

## The six pieces of evidence that would reverse the call

From Section 5 of the memo, in priority order. Items 1 and 5 are threshold
conditions — without them the rest cannot be trusted, because they would still
be documents the company chose to hand over.

1. **A signed reconciliation** bridging Valcambi SA's statutory accounts to the
   ₹4,16,072 crore FY25 attributed figure, prepared independently.
2. **Customer-wise sales ledger** for the top 20 counterparties, covering at least
   80% of attributed revenue, confirmed directly by the auditor.
3. **Vendor-wise procurement ledger**, matched to vault, assay and shipping
   records showing physical metal movement.
4. **Bank statements reconciling to invoices** across at least 80% of attributed
   revenue — cash, not accounting entries — with operating cash flow reconciled to
   reported profit.
5. **Confirmation that subsidiary accounts were audited in their own
   jurisdictions**, with those reports made available.
6. **A clean forensic audit** plus an unqualified FY27 audit opinion.

**Review trigger:** the forensic report or the next audited results, whichever
comes first. (Not "FY26 results": under SEBI LODR Regulation 33(3)(d), annual
audited results are due within 60 days of year-end, so FY26's were due by 30 May
2026 — before the June order.)

And the things that would make the exclusion permanent: any restatement, an
auditor resignation or qualification, continued non-production, unexplained
related-party flows, or promoter/trading restrictions.

Finally, what would **not** change the view: another denial from management, a
further fall in the price, or simply time passing without an adverse finding.
*The absence of confirmed wrongdoing is not evidence of verifiable revenue.*
