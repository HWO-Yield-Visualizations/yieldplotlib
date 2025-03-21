"""Pipeline for generating a standard sheet of yield plots."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import yieldplotlib as ypl
from yieldplotlib.load import AYODirectory, EXOSIMSDirectory
from yieldplotlib.plots.yield_hist import plot_hist

# Set pipeline plot specific params
params = {
    "axes.titlesize": 12,
    "axes.labelsize": 8,
    "lines.linewidth": 4,
    "lines.markersize": 4,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
}
plt.rcParams.update(params)


def ypl_pipeline(runs):
    """Runs the yieldplotlib pipeline to generate a page of summary plots."""
    ax_kwargs = {}

    fig, axes = plt.subplot_mosaic("ABC;DEE;FGG", figsize=(8.5, 11))
    plt.margins(0.1, 0.2)

    # Add ypl "watermark".
    ypl_logo = plt.imread("/Users/ssteiger/repos/yieldplotlib/docs/_static/logo.png")
    newax = fig.add_axes([0.05, 0.9, 0.05, 0.05], anchor="NE", zorder=1)
    newax.axis("off")
    newax.imshow(ypl_logo)

    # Plot summary yield text for a reasonable number of runs.
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
        ax.set(**ax_kwargs)

    # Plot stellar parameters.
    scatter_kwargs = {"alpha": 0.7}
    axes["A"].set_yscale("log")
    ypl.compare(axes["A"], runs, "star_dist", y="star_L",
                plot_type="scatter", **scatter_kwargs)

    hist_kwargs = {"histtype": "step"}
    axes["B"].set_ylabel("# Targets")
    axes["B"].set_xlim((0, 4))

    ypl.compare(axes["B"], runs, "angdiam", plot_type="hist", **hist_kwargs)

    axes["C"].set_ylabel("# Targets")
    ypl.compare(axes["C"], runs, "MV", plot_type="hist", **hist_kwargs)

    axes["D"].set_ylabel("# Targets")
    ypl.compare(axes["D"], runs, "exp_time_det", plot_type="hist", **hist_kwargs)

    axes["F"].set_ylabel("# Targets")
    ypl.compare(axes["F"], runs, "exp_time_char", plot_type="hist", **hist_kwargs)

    # Plot HZ completeness.
    ypl.compare(
        axes["E"], runs, "star_dist", y="star_L", c="star_comp_det",
        plot_type="scatter", **scatter_kwargs
    )

    # Create the inset colorbar axes object.
    cax = inset_axes(
        axes["E"],
        width="60%",
        height="5%",
        loc="upper left",
    )

    cmappable = ScalarMappable(Normalize(0, 1))
    cbar = fig.colorbar(cmappable, cax=cax, orientation="horizontal")
    cbar.set_label("HZ Completeness", loc="center", fontsize=8)
    cbar.ax.xaxis.set_label_position("bottom")
    cbar.ax.xaxis.set_ticks_position("bottom")
    cbar.ax.tick_params(labelsize=6, width=1.0)

    # Plot planet yield bar chart.
    temps = ["hot", "warm", "cold"]
    planet_bins = ["Earth", "Rocky", "Super Earth"]
    run_labels = [
        "EXOSIMS" if isinstance(run, EXOSIMSDirectory) else "AYO" for run in runs
    ]
    plot_hist(temps, planet_bins, runs, run_labels, ax=axes["G"])

    plt.tight_layout(rect=[0, 0, 1, 0.9])
    plt.savefig("./ypl_summary.pdf")
    plt.show()
