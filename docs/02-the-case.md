# 2. The case

> Reminder: this is a **fictionalised teaching case** written by the competition
> organisers. The fund, its staff and the emails are invented. The figures below
> are reproduced from the case booklet's exhibits and are used here only to
> explain the exercise.

---

## The setup

**You are** a research analyst at Aarohan Capital, a long-only Indian equity
fund managing ₹4,500 crore.

*("Long-only" means the fund only buys shares hoping they rise. It cannot make
money from a share falling, so a bad holding is simply a loss.)*

**The fund owns** a small legacy position in **Rajesh Exports Limited**, a
Bengaluru-based listed company in gold jewellery manufacturing, export and
refining. It was bought because the company appeared to have:

- Massive consolidated revenue
- A globally important gold refining subsidiary (Valcambi SA, in Switzerland)
- A long operating history
- Low debt
- Export scale
- A share price that looked cheap on valuation screens

**What changed:** In **June 2026** the securities regulator issued an *interim
order* questioning the company's consolidated revenues, its overseas
subsidiaries, the supporting documents, and Valcambi's role. The company denied
wrongdoing and said the regulator had misunderstood how gold refining and
bullion revenue work.

**Your task:** the Portfolio Manager needs a recommendation by end of day. The
case is explicit that the job is **not to prove fraud** — it is to think like an
analyst under uncertainty and decide whether the evidence supports an investment
case, or whether the risk is too great for money held on behalf of clients.

---

## The four choices

| | Option | Meaning |
|---|---|---|
| **A** | Buy / Average Down | The market has overreacted; the explanation is credible and the stock is mispriced. |
| **B** | Hold / Wait for Forensic Audit | Serious risk, but do not sell until more evidence emerges. |
| **C** | Exit / Avoid | The uncertainty makes the stock unsuitable. Sell. |
| **D** | Forensic Red Flag / Uninvestable | Remove from the investable universe until independent verification is complete. |

**This submission chooses D.** The reasoning is in
[`03-the-analysis.md`](03-the-analysis.md).

---

## The people writing to you

The case is delivered as an inbox of four emails. Each one is a different way of
looking at the same facts — part of the exercise is noticing what each person
takes for granted.

| Person | Role | Their position |
|---|---|---|
| **Meera Shah** | Portfolio Manager | Approved the position because it screened cheap. Wants a clean call, not a description of the price fall. Asks four specific questions. |
| **Kabir Rao** | Risk Officer | Would exit now. His argument: if revenue is uncertain, profit is uncertain; if profit is uncertain, book value is uncertain; so the stock is not cheap, it is *unanalysable*. |
| **Nikhil Arora** | External broker (bullish) | Thinks the market has overreacted. Gold refining is high-volume and low-margin by nature — huge revenue with tiny margins is normal, not fake. |
| **Ananya Menon** | Forensic accounting consultant | Says the real question is narrower: can the specific revenue reported be verified at transaction level? Who were the customers and suppliers? Were there invoices, shipping documents, bank trails? Were transactions circular? |

Meera's four questions are the ones the memo must answer:

1. Can we trust the reported revenue?
2. Does the company's explanation make sense?
3. What evidence would change our mind?
4. Should we hold, exit or classify it as uninvestable?

---

## The group structure (Exhibit 1)

| Entity | Country | Role | The question it raises |
|---|---|---|---|
| Rajesh Exports Limited | India | Listed parent | What does the parent actually earn on its own? |
| REL Singapore Pte Ltd | Singapore | Overseas subsidiary | Does it have real operations? |
| Global Gold Refineries SA | Switzerland | **Holding company** | Why are large revenues booked *here*? |
| Valcambi SA | Switzerland | Gold refinery | Do its audited numbers reconcile with group revenue? |
| ACC Energy Storage Pvt Ltd | India | Battery / energy | Is this core business, or a distraction? |

The third row matters more than it looks. A *holding* company does not trade or
manufacture — it just owns other companies. Revenue appearing at a holding
company, rather than at the refinery underneath it that actually does the work,
is unusual.

---

## The numbers

### Exhibit 4 — Consolidated vs standalone revenue (₹ crore)

"Standalone" is the listed Indian parent on its own. "Consolidated" is the
parent plus everything it owns.

| Year | Consolidated | Standalone | From subsidiaries | Subsidiary share |
|---|---|---|---|---|
| FY21 | 2,58,306 | 2,060 | 2,56,245 | 99.20% |
| FY22 | 2,43,128 | 6,237 | 2,36,891 | 97.43% |
| FY23 | 3,39,690 | 5,762 | 3,33,928 | 98.30% |
| FY24 | 2,80,676 | 5,401 | 2,75,276 | 98.08% |
| FY25 | 4,23,099 | 7,027 | 4,16,072 | 98.34% |

**Read this as:** almost the entire business sits outside India, in entities that
Indian investors cannot inspect.

### Exhibit 5 — Profit after tax (₹ crore)

| Year | Consolidated PAT | Standalone PAT | Subsidiary PAT |
|---|---|---|---|
| FY21 | 845 | 99 | 746 |
| FY22 | 1,009 | 23 | 987 |
| FY23 | 1,432 | 30 | 1,402 |
| FY24 | 336 | 17 | 318 |
| FY25 | 95 | 24 | 71 |

**Read this as:** profit depends on the subsidiaries too — and it collapsed in
FY24 and FY25 even though revenue did not.

### Exhibit 6 — Revenue against profitability

| Year | Consolidated revenue | Consolidated PAT | Margin |
|---|---|---|---|
| FY21 | 2,58,306 | 845 | 0.33% |
| FY22 | 2,43,128 | 1,009 | 0.41% |
| FY23 | 3,39,690 | 1,432 | 0.42% |
| FY24 | 2,80,676 | 336 | 0.12% |
| FY25 | 4,23,099 | 95 | **0.02%** |

The case itself notes that thin margins are not automatically suspicious in
bullion trading — but that when margins are *this* thin, small accounting
differences can change the whole picture.

### Exhibit 8 — The heart of the dispute (₹ crore)

| Year | Credited to subsidiaries | Valcambi SA audited revenue | Difference |
|---|---|---|---|
| FY21 | 2,56,245 | 586 | 2,55,659 |
| FY22 | 2,36,891 | 729 | 2,36,163 |
| FY23 | 3,33,928 | 743 | 3,33,185 |
| FY24 | 2,75,276 | 543 | 2,74,733 |
| FY25 | 4,16,072 | 427 | 4,15,646 |
| **Total** | **15,18,413** | **3,027** | **15,15,385** |

This single table is the case. The audited refinery is roughly **0.2%** of what
the group credits to its overseas arms.

---

## Exhibit 7 — What the regulator alleged

- The overwhelming majority of consolidated revenue was credited to overseas and
  step-down subsidiaries.
- The company **failed to furnish verifiable transaction-level records** despite
  repeated requests.
- The regulator compared Valcambi's audited standalone revenue with the much
  larger group figures.
- Roughly **₹15.15 lakh crore** of subsidiary revenue over FY21–FY25 was
  *prima facie* misrepresented.
- A forensic examination was ordered.
- **The findings are interim — not a final adjudication.**

*"Prima facie" means "on first look". It is a low bar, not a verdict.*

## Exhibit 9 — What the company replied

| Argument | What it means |
|---|---|
| The order is interim | Nothing is conclusively decided yet |
| Revenue is genuine | All the figures are true |
| Valcambi is a major global refinery | Large throughput genuinely produces large revenue |
| The regulator misunderstood | It confused standalone value-addition figures with consolidated bullion revenue |
| The company is debt-free | The business does not depend on outside finance |
| Explanations will follow | Documents and evidence will be provided |

---

## Exhibit 12 — What evidence would settle it

| Evidence | Direction | Why it matters |
|---|---|---|
| Customer-wise sales ledger | Bullish if verified | Proves real buyers existed |
| Vendor-wise purchase ledger | Bullish if verified | Supports the gold procurement trail |
| Bank statements matching invoices | Bullish if verified | Shows cash actually moved |
| Shipping / vault / refinery records | Bullish if verified | Shows physical gold moved |
| Independent Valcambi audit reconciliation | Bullish if clean | Resolves the core mismatch |
| Clean forensic audit | Bullish | Could restore confidence |
| Unexplained related-party transactions | **Bearish** | Raises circular transaction risk |
| Auditor resignation or qualification | **Bearish** | Indicates the auditor is uncomfortable |
| **Refusal to share records** | **Bearish** | Prevents independent verification |
| Revenue restatement | **Bearish** | Damages trust and valuation |

The bolded "refusal to share records" line is important: the case itself treats
non-production of documents as evidence in its own right, not as a neutral
absence. The memo leans on this.
