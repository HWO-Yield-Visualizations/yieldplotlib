"""Plots a HZ completeness comparison between an AYO and EXOSIMS run."""

import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from yieldplotlib.core.plot import Plot


def plot_hz_completeness(
    exosims_dir, ayo_dir, ax_kwargs={}, hline_kwargs={}, use_cyberpunk=False
):
    """Generate a scatter plot of the habitable zone completeness.

    Args:
        exosims_dir (EXOSIMSDirectory):
            EXOSIMSDirectory to plot.
        ayo_dir (AYODirectory):
            AYODirectory to plot.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        hline_kwargs (dict, optional):
            Keyword arguments to pass to ax.axhline().
        use_cyberpunk (bool, optional):
            Whether to use the mplcyberpunk style. Default is False.

    Returns:
        matplotlib.figure.Figure, matplotlib.axes.Axes:
            Figure and axes objects for the plot.
    """
    if use_cyberpunk:
        import mplcyberpunk  # noqa: F401

        plt.style.use("cyberpunk")

    # Generate the figure and axes and set super x and y labels.
    fig, axes = plt.subplots(1, 2, sharey=True)
    fig.supxlabel("d (pc)")
    fig.supylabel("Luminosity (L$_\odot$)")
    ayo_ax, exo_ax = axes

    # Create the inset colorbar axes object.
    cax = inset_axes(
        exo_ax,
        width="80%",  # width: 50% of parent_bbox width
        height="3%",  # height: 5%
        loc="upper center",
    )

    # Use the Plot base class to instantiate the AYO plot.
    ayo_plot = Plot(ax_kwargs=ax_kwargs)
    ayo_plot.ax = ayo_ax

    # Get the AYO data.
    ayo_data = [ayo_dir.get("star_dist"), ayo_dir.get("star_L")]
    colors = ayo_dir.get("star_comp_det")

    # Get the colors and sizes for the scatter points.
    plot_kwargs = {
        "c": colors,
        "alpha": [c + 0.1 if c == 0 else 1 for c in colors],
        "s": [15 if c == 0 else 40 for c in colors],
    }

    # Plot the AYO data.
    ayo_plot.generic_plot("scatter", data=ayo_data, plot_kwargs=plot_kwargs)

    # Plot the horizontal lines differentiating the spectral types.
    ayo_ax.axhline(y=5.5, **hline_kwargs)
    ayo_ax.axhline(y=2, **hline_kwargs)
    ayo_ax.axhline(y=0.65, **hline_kwargs)
    ayo_ax.axhline(y=0.085, **hline_kwargs)

    # Generate and format the colorbar.
    cmappable = ScalarMappable(Normalize(0, 1))
    cbar = fig.colorbar(cmappable, cax=cax, orientation="horizontal")
    cbar.set_label("HZ Completeness", loc="center", fontsize=11)
    cbar.ax.xaxis.set_label_position("bottom")
    cbar.ax.xaxis.set_ticks_position("bottom")
    cbar.ax.tick_params(labelsize=8, width=1.5)

    # Use the Plot base class to instantiate the EXOSIMS plot.
    exo_plot = Plot(ax_kwargs=ax_kwargs)
    exo_plot.ax = exo_ax

    # Get the EXOSIMS data.
    exosims_colors = exosims_dir.get("star_comp_det")
    exosims_data = [exosims_dir.get("star_dist"), exosims_dir.get("star_L")]

    # Get the colors and sizes for the scatter points.
    plot_kwargs = {
        "c": exosims_colors,
        "alpha": [c + 0.1 if c == 0 else 1 for c in exosims_colors],
        "s": [15 if c == 0 else 40 for c in exosims_colors],
    }

    # Plot the EXOSIMS data.
    exo_plot.generic_plot("scatter", data=exosims_data, plot_kwargs=plot_kwargs)

    # Plot the horizontal lines differentiating the spectral types
    exo_ax.axhline(y=5.5, **hline_kwargs)
    exo_ax.axhline(y=2, **hline_kwargs)
    exo_ax.axhline(y=0.65, **hline_kwargs)
    exo_ax.axhline(y=0.085, **hline_kwargs)

    # Add the spectral type labels.
    ayo_ax.text(
        0.07,
        0.83,
        "A",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
    )
    ayo_ax.text(
        0.07,
        0.73,
        "F",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
    )
    ayo_ax.text(
        0.07,
        0.61,
        "G",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
    )
    ayo_ax.text(
        0.07,
        0.4,
        "K",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
    )
    ayo_ax.text(
        0.07,
        0.01,
        "M",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
    )

    # Add AYO and EXOSIMS labels.
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    ayo_ax.text(
        0.9,
        0.08,
        "AYO",
        transform=ayo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
        bbox=props,
    )
    exo_ax.text(
        0.9,
        0.08,
        "EXOSIMS",
        transform=exo_ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
        bbox=props,
    )

    # Remove the white space between the two subplots.
    fig.subplots_adjust(wspace=0)
    exo_ax.tick_params(right=True, which="both")

    return fig, axes
