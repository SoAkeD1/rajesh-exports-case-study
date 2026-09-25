"""Draws the two memo figures as PNGs in submission/figures/.

Figures are images, so their labels add no words to the PDF's extractable text.
Run: python tools/charts.py   (build.py embeds whatever is in submission/figures/)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "submission" / "figures"

YEARS = ["FY21", "FY22", "FY23", "FY24", "FY25"]
ATTRIBUTED = [256245, 236891, 333928, 275276, 416072]   # Exhibit 8, ₹ crore
VALCAMBI = [586, 729, 743, 543, 427]                    # Exhibit 8, ₹ crore
REVENUE = [258306, 243128, 339690, 280676, 423099]      # Exhibit 6, ₹ crore
PAT = [845, 1009, 1432, 336, 95]                        # Exhibit 5, ₹ crore
# Approximate fiscal-year averages, ₹ per 10 g: LBMA USD price x RBI USD/INR rate.
GOLD = [43500, 43550, 46630, 52950, 70300]

BLUE, ORANGE = "#2a78d6", "#eb6834"                     # validated categorical slots 1-2
GREY, INK, MUTED, GRID = "#8a8a84", "#1a1a1a", "#666666", "#e6e4dd"

plt.rcParams.update({
    "font.family": "Georgia", "font.size": 8.5, "axes.edgecolor": GRID,
    "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False,
})


def index(series):
    return [v / series[0] * 100 for v in series]


def style(ax):
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)
    ax.spines["left"].set_visible(False)


def title(fig, head, sub, source):
    fig.text(0.01, 0.97, head, fontsize=10.5, fontweight="bold", color=INK, va="top")
    fig.text(0.01, 0.885, sub, fontsize=8.5, color=MUTED, va="top")
    fig.text(0.01, 0.02, source, fontsize=7, color=MUTED, va="bottom")


def divergence():
    fig, ax = plt.subplots(figsize=(6.3, 2.65), dpi=300)
    fig.subplots_adjust(left=0.07, right=0.80, top=0.78, bottom=0.17)
    x = range(len(YEARS))
    series = [
        (index(ATTRIBUTED), BLUE, "-", "Revenue attributed\nto subsidiaries"),
        (index(GOLD), GREY, "--", "Rupee gold price"),
        (index(VALCAMBI), ORANGE, "-", "Valcambi SA\naudited revenue"),
    ]
    for ys, colour, ls, label in series:
        ax.plot(x, ys, color=colour, linestyle=ls, linewidth=2, marker="o", markersize=4,
                markeredgecolor="white", markeredgewidth=1, label=label.replace("\n", " "))
    ax.axhline(100, color=MUTED, linewidth=0.6)
    # direct end labels; blue and grey both end near 162, so split them vertically
    ends = [(index(ATTRIBUTED)[-1] + 9, BLUE, "Attributed revenue  162"),
            (index(GOLD)[-1] - 9, GREY, "Gold price  162"),
            (index(VALCAMBI)[-1], ORANGE, "Valcambi audited  73")]
    for y, colour, text in ends:
        ax.text(4.12, y, text, color=INK, fontsize=8, va="center")
        ax.plot([4.02, 4.1], [y, y], color=colour, linewidth=2)
    ax.set_xticks(list(x), YEARS)
    ax.set_xlim(-0.15, 4.1)
    ax.set_ylim(50, 180)
    style(ax)
    fig.legend(loc="upper right", frameon=False, fontsize=7.5, ncol=3, bbox_to_anchor=(0.995, 0.915),
               handlelength=2.2, columnspacing=1.2)
    title(fig, "Group revenue rose with the gold price; the refinery's audited revenue fell",
          "Index, FY21 = 100",
          "Source: Exhibit 8. Gold price: LBMA annual averages converted at RBI reference rates (approximate).")
    fig.savefig(OUT / "fig1-divergence.png")
    plt.close(fig)


def profit():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 2.35), dpi=300)
    fig.subplots_adjust(left=0.03, right=0.99, top=0.72, bottom=0.17, wspace=0.12)
    x = range(len(YEARS))
    panels = [
        (a1, [v / 100000 for v in REVENUE], "Consolidated revenue, ₹ lakh crore",
         lambda v: f"{v:.2f}"),
        (a2, PAT, "Consolidated profit after tax, ₹ crore",
         lambda v: f"{v:,.0f}"),
    ]
    for ax, ys, head, fmt in panels:
        bars = ax.bar(x, ys, width=0.58, color=BLUE)
        for b, v in zip(bars, ys):
            ax.text(b.get_x() + b.get_width() / 2, v, fmt(v), ha="center", va="bottom",
                    fontsize=7.5, color=INK)
        ax.set_xticks(list(x), YEARS)
        ax.set_yticks([])
        ax.set_ylim(0, max(ys) * 1.18)
        ax.set_title(head, fontsize=8.5, color=MUTED, loc="left", pad=4)
        style(ax)
        ax.grid(False)
    title(fig, "Revenue rose 24.6% from FY23 to FY25; profit in rupees fell 93.4%",
          "Same years, same group, two separate scales",
          "Source: Exhibits 5 and 6.")
    fig.savefig(OUT / "fig2-profit.png")
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    divergence()
    profit()
    print("Wrote", *sorted(p.name for p in OUT.glob("*.png")))
