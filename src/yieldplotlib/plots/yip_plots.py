"""Generate plots for yield input packages."""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def make_offax_psf_movie(yip, save_name, ax_kwargs={}, plot_kwargs={}):
    """Generate a movie of the off-axis stellar PSF moving as a function of lambda/D.

    Args:
        yip (YIPDirectory):
            YIPDirectory to plot.
        save_name (str):
            File path to where the output movie will be saved.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        plot_kwargs (dict, optional):
            Keyword arguments to pass to plt.figure().

    Returns:
        None
    """
    # Get the off-axis stellar PSF data from the YIP.
    offax_psf_data = yip.get("offax.data")
    offax_psf_offsets_list = yip.get("offax_offset_list.data")

    # Set up the figure and axis.
    fig, ax = plt.subplots(**plot_kwargs)

    # Prepare the initial image.
    initial_image = np.log(offax_psf_data[0])
    initial_image[~np.isfinite(initial_image)] = -20
    ax.imshow(initial_image)
    fig.tight_layout()

    # Add an inset text with the current λ/D value.
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    text_obj = ax.text(
        0.95,
        0.9,
        f"$\\lambda / D$ = {offax_psf_offsets_list[0]:.2f}",
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
        im_data = np.log(offax_psf_data[frame])
        im_data[~np.isfinite(im_data)] = -20
        im_obj = ax.imshow(im_data)
        # Update the text
        text_obj.set_text(f"$\\lambda / D$ = {offax_psf_offsets_list[frame]:.2f}")
        return im_obj, text_obj

    # Create the animation.
    ani = animation.FuncAnimation(fig, update, frames=len(offax_psf_data), blit=True)

    # Save the animation to file.
    ani.save(save_name, fps=2, writer="ffmpeg")
    plt.close(fig)


def plot_core_throughtput(
    runs,
    run_labels,
    yip=None,
    ax=None,
    ax_kwargs={},
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
        yip (YIPDirectory):
            YIPDirectory to plot. If None, the throughput directly from the YIP
            (accessed via yippy) will not be plotted.
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
    if use_cyberpunk:
        import mplcyberpunk  # noqa: F401
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

    if yip:
        separations, core_thruput_from_yip = yip.coronagraph.get_throughput_curve(
            plot=False, aperture_radius_lod=aperture_radius, oversample=1
        )
        ax.plot(separations, core_thruput_from_yip, label="yippy")

    for i, run in enumerate(runs):
        fits = run.get("core_thruput")
        if isinstance(fits, dict):
            for name in fits:
                thruput_data = fits[name].get("data")
                ax.plot(thruput_data[:, 0], thruput_data[:, 1], label=run_labels[i])
        else:
            thruput_data = fits.get("data")
            ax.plot(thruput_data[:, 0], thruput_data[:, 1], label=f"{run_labels[i]}")

    ax.set(**ax_kwargs)
    plt.xlabel("Separation ($\\lambda/D$)")
    plt.ylabel("Throughput")

    plt.legend()

    if use_cyberpunk:
        mplcyberpunk.add_glow_effects()

    if title:
        plt.title(title)

    return fig, ax
