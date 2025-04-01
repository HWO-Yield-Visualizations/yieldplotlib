"""yieldplotlib - A library for plotting yield data."""

__all__ = [
    "__version__",
    "fetch_ayo_data",
    "fetch_exosims_data",
    "fetch_yip_data",
    "KEY_MAP",
    "logger",
    "calculate_axis_limits_and_ticks",
    "get_nice_number",
    "subplots",
    "compare",
    "multi",
    "panel",
    "ypl_cmap",
    "ypl_colors",
    "ypl_cycler",
    "ypl_rainbow",
    "xy_grid",
]

from importlib.resources import as_file, files

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

# Using the new files() API
with as_file(files("yieldplotlib").joinpath("style")) as path:
    ypl_stylesheets = plt.style.core.read_style_directory(path)
    plt.style.core.update_nested_dict(plt.style.library, ypl_stylesheets)
    # Set the default style to ypl_default
    plt.style.use("yieldplotlib")
