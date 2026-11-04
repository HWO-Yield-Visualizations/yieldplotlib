"""yieldplotlib - A library for plotting yield data."""

__all__ = [
    "KEY_MAP",
    "__version__",
    "calculate_axis_limits_and_ticks",
    "compare",
    "fetch_ayo_data",
    "fetch_exosims_data",
    "fetch_yip_data",
    "get_nice_number",
    "logger",
    "multi",
    "panel",
    "subplots",
    "xy_grid",
    "ypl_cmap",
    "ypl_colors",
    "ypl_cycler",
    "ypl_rainbow",
]

from importlib.resources import as_file, files

import matplotlib as mpl
import matplotlib.pyplot as plt

from ._version import __version__
from .datasets import fetch_ayo_data, fetch_exosims_data, fetch_yip_data
from .key_map import KEY_MAP
from .logger import logger
from .plots.comparison_plots import compare, multi, panel, xy_grid
from .plots.generic_plot import extend_matplotlib, subplots
from .style import ypl_cmap, ypl_colors, ypl_cycler, ypl_rainbow
from .util import calculate_axis_limits_and_ticks, get_nice_number

# Automatically extend matplotlib with our custom methods
extend_matplotlib()

# Register packaged styles by name using Matplotlib's public APIs.
with as_file(files("yieldplotlib").joinpath("style")) as path:
    for style_path in path.glob("*.mplstyle"):
        params = mpl.rc_params_from_file(style_path, use_default_template=False)
        plt.style.library.setdefault(style_path.stem, {}).update(params)
    # Set the default style to yieldplotlib.
    plt.style.use("yieldplotlib")
