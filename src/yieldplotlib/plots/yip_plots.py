"""Generate plots for yield input packages."""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from optixstuff.apertures import Circular
from yippy import YIPPackage


def make_offax_psf_movie(yip: YIPPackage, save_name, ax_kwargs=None, plot_kwargs=None):
    """Generate a movie of the off-axis stellar PSF moving as a function of lambda/D.

    Args:
        yip: Native yield input package.
        save_name (str):
            File path to where the output movie will be saved.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        plot_kwargs (dict, optional):
            Keyword arguments to pass to plt.figure().

    Returns:
        matplotlib.animation.FuncAnimation: The saved animation.
    """
    # Get the off-axis stellar PSF data from the YIP.
    if plot_kwargs is None:
        plot_kwargs = {}
    if ax_kwargs is None:
        ax_kwargs = {}
    psfs = yip.offaxis_psfs
    offsets = yip.offsets_xy_lod

    def log_psf(frame):
        with np.errstate(divide="ignore", invalid="ignore"):
            data = np.log(psfs[frame])
        return np.where(np.isfinite(data), data, -20)

    def offset_label(frame):
        x, y = offsets[frame]
        return rf"$(x, y) = ({x:.2f}, {y:.2f})\,\lambda/D$"

    # Set up the figure and axis.
    fig, ax = plt.subplots(**plot_kwargs)

    # Prepare the initial image.
    im_obj = ax.imshow(log_psf(0))
    fig.tight_layout()

    # Add an inset text with the current lambda/D value.
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    text_obj = ax.text(
        0.95,
        0.9,
        offset_label(0),
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment="bottom",
        horizontalalignment="right",
        bbox=props,
    )

    # Apply any additional axis settings.
    ax.set(**ax_kwargs)

    # Update frames
    def update(frame):
        im_obj.set_data(log_psf(frame))
        text_obj.set_text(offset_label(frame))
        return im_obj, text_obj

    # Create the animation.
    ani = animation.FuncAnimation(fig, update, frames=len(psfs), blit=True)

    # Save the animation to file.
    ani.save(save_name, fps=2, writer="ffmpeg")
    plt.close(fig)
    return ani


def plot_core_throughtput(
    runs,
    run_labels,
    yip: YIPPackage | None = None,
    ax=None,
    ax_kwargs=None,
    use_cyberpunk=False,
    title=None,
    aperture_radius=0.85,
):
    """Plot the core throughput as a function of lambda/D.

    Args:
        runs (list):
            List of EXOSIMSDirectories and AYODirectories to plot.
        run_labels (list):
            List of labels for each run.
        yip: Optional native yield input package for the reference throughput.
        ax (matplotlib.axes.Axes, optional):
            Axes to plot on. If None, a new figure is created.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        use_cyberpunk (bool, optional):
            Whether to use the mplcyberpunk style. Default is False.
        title (str, optional):
             Title for the plot.
        aperture_radius (float):
            Radius of the photometric aperture to use for the YIP throughput
            calculation.

    Returns:
        matplotlib.figure.Figure, matplotlib.axes.Axes:
            Figure and axes objects for the plot.
    """
    if ax_kwargs is None:
        ax_kwargs = {}
    if use_cyberpunk:
        import mplcyberpunk
        from cycler import cycler

        plt.style.use("cyberpunk")
        prop_cycle = plt.rcParams["axes.prop_cycle"]
        colors = prop_cycle.by_key()["color"]
        custom_cycler = cycler(linestyle=["-", "--", ":", "-."]) + cycler(
            color=colors[:4]
        )
        plt.rc("axes", prop_cycle=custom_cycler)

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()

    if yip is not None:
        rule = Circular(aperture_radius)
        coro = yip.prepare(rules=(rule,))
        performance_metrics = coro.curves(rule)
        separations = performance_metrics.separation_lod
        core_thruput_from_yip = performance_metrics.throughput
        ax.plot(separations, core_thruput_from_yip, label="yippy")

    for i, run in enumerate(runs):
        data = run.get("core_thruput")
        ax.plot(data["sep"], data["thruput"], label=f"{run_labels[i]}")

    ax.set(**ax_kwargs)
    plt.xlabel("Separation ($\\lambda/D$)")
    plt.ylabel("Throughput")

    plt.legend()

    if use_cyberpunk:
        mplcyberpunk.add_glow_effects()

    if title:
        plt.title(title)

    return fig, ax
