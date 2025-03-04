"""Generate plots for yield input packages."""

from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from yieldplotlib.load.yip_directory import YIPDirectory


def make_offax_psf_movie(yip_folder, save_name, ax_kwargs={}, plot_kwargs={}):
    """Generate a movie of the off-axis stellar PSF moving as a function of lambda/D.

    Args:
        yip_folder (str):
            File path to the yield input package folder.
        save_name (str):
            File path to where the output movie will be saved.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        plot_kwargs (dict, optional):
            Keyword arguments to pass to plt.figure().

    Returns:
        None
    """
    # Define the YIPDirectory.
    yip = YIPDirectory(Path(yip_folder))

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
