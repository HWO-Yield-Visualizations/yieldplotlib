"""Generate plots for yield input packages."""

import glob
import os

import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np


def make_offax_psf_movie(yip, temp_folder, save_name, ax_kwargs={}, plot_kwargs={}):
    """Generate a movie of the off-axis stellar PSF moving as a function of lambda/D.

    Args:
        yip (YIPDirectory):
            Yield input package to use to generate the movie.
        temp_folder (str):
            File path to the folder in which to store the intermediate movie images.
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

    # If the specified temp folder doesn't exist, make it.
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    # Plot and save each off-axis PSF image.
    for i, im in enumerate(offax_psf_data):
        im = np.log(im)
        im[~np.isfinite(im)] = -20
        fig = plt.figure(**plot_kwargs)
        ax = fig.add_subplot()
        ax.imshow(im)

        # Add an inset with the current offset lambda/D value.
        props = dict(boxstyle="round", facecolor="white", alpha=0.5)
        ax.text(
            0.95,
            0.9,
            f"$\lambda / D$ = {offax_psf_offsets_list[i]:.2f}",
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment="bottom",
            horizontalalignment="right",
            bbox=props,
        )

        ax.set(**ax_kwargs)
        f_name = os.path.join(temp_folder, f"{i}".zfill(3) + "_image.png")
        plt.savefig(f_name, bbox_inches="tight")

    # Gather all the saved files and make and save the movie.
    files = sorted(glob.glob(os.path.join(temp_folder, "*")))
    images = [imageio.imread(file) for file in files]
    imageio.mimsave(save_name, images, fps=2)


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
    plt.xlabel("Separation ($\lambda/D$)")
    plt.ylabel("Throughput")

    plt.legend()

    if use_cyberpunk:
        mplcyberpunk.add_glow_effects()

    if title:
        plt.title(title)

    return fig, ax
