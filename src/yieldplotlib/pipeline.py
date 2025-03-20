"""Pipeline for generating a standard sheet of yield plots."""

import matplotlib.pyplot as plt
import numpy as np

import yieldplotlib as ypl
from yieldplotlib.load import AYODirectory, EXOSIMSDirectory
from yieldplotlib.plots.yield_hist import plot_hist


def ypl_pipeline(runs):
    ax_kwargs = {}

    fig, axes = plt.subplot_mosaic("ABC;DEF;GHH", figsize=(8.5, 11))
    plt.margins(0.1, 0.2)

    # Add ypl "watermark".
    ypl_logo = plt.imread("/Users/ssteiger/repos/yieldplotlib/docs/_static/logo.png")
    newax = fig.add_axes([0.05, 0.9, 0.05, 0.05], anchor="NE", zorder=1)
    newax.axis("off")
    newax.imshow(ypl_logo)

    if len(runs) < 5:
        y_locs = np.linspace(0.92, 0.94, len(runs))
        for i, run in enumerate(runs):
            if isinstance(run, EXOSIMSDirectory):
                earth_yield = run.get("yield_earth")
                plt.figtext(
                    0.11,
                    y_locs[i],
                    "EXOSIMS ExoEarth yield: {:.2f}".format(earth_yield[0]),
                    fontdict={"fontsize": 8},
                )
            elif isinstance(run, AYODirectory):
                earth_yield = run.get("yield_earth")
                plt.figtext(
                    0.11,
                    y_locs[i],
                    "AYO ExoEarth yield: {:.2f}".format(earth_yield),
                    fontdict={"fontsize": 8},
                )

    for ax in axes.values():
        print(ax)
        ax.set(**ax_kwargs)

    hist_kwargs = {"histtype": "step"}
    axes["A"].set_ylabel("# Targets")
    ypl.compare(axes["A"], runs, "angdiam", plot_type="hist", **hist_kwargs)

    axes["B"].set_ylabel("# Targets")
    ypl.compare(axes["B"], runs, "MV", plot_type="hist", **hist_kwargs)

    axes["C"].set_ylabel("# Targets")
    ypl.compare(axes["C"], runs, "exp_time_det", plot_type="hist", **hist_kwargs)

    ypl.compare(axes["D"], runs, "star_dist", y="star_L", plot_type="scatter")

    axes["E"].set_ylabel("# Targets")
    ypl.compare(axes["E"], runs, "exp_time_char", plot_type="hist", **hist_kwargs)

    ypl.compare(
        axes["G"], runs, "star_dist", y="star_L", c="star_comp_det", plot_type="scatter"
    )

    temps = ["hot", "warm", "cold"]
    planet_bins = ["Earth", "Rocky", "Super Earth"]
    run_labels = [
        "EXOSIMS" if isinstance(run, EXOSIMSDirectory) else "AYO" for run in runs
    ]
    plot_hist(temps, planet_bins, runs, run_labels, ax=axes["H"])

    plt.tight_layout(rect=[0, 0, 1, 0.9])
    plt.savefig("./ypl_summary.pdf")
    plt.show()
