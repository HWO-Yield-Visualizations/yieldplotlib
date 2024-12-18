"""Generate plots for yield input packages"""

import os
import glob
from yieldplotlib.load.yip_directory import YIPDirectory
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import imageio.v2 as imageio


def make_offax_psf_movie(
        yip_folder, temp_folder, save_name, ax_kwargs={}, plot_kwargs={}
                         ):
    """ Generate a movie of the off-axis stellar PSF moving as a function of lambda/D.

    Args:
        yip_folder (str):
            File path to the yield input package folder.
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
    yip_path = yip_folder
    yip = YieldInputPackage(Path(yip_path))

    offax_psf_data = yip.get("offax_psf")
    offax_psf_offsets_list = yip.get("offax_psf_offset_list")

    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    for i, im in enumerate(offax_psf_data):
        im = np.log(im)
        im[~np.isfinite(im)] = -20
        fig = plt.figure(**plot_kwargs)
        ax = fig.add_subplot()
        ax.imshow(im)

        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax.text(0.95, 0.9, f'$\lambda / D$ = {offax_psf_offsets_list[i]:.2f}',
                transform=ax.transAxes, fontsize=12, verticalalignment='bottom',
                horizontalalignment='right', bbox=props)

        ax.set(**ax_kwargs)
        f_name = os.path.join(temp_folder, f'{i}'.zfill(3) + '_image.png')
        plt.savefig(f_name, bbox_inches='tight')

    files = sorted(glob.glob(os.path.join(temp_folder, '*')))
    images = [imageio.imread(file) for file in files]
    imageio.mimsave(save_name, images, fps=2)
