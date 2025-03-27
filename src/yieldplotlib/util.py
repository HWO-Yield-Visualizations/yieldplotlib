"""Utility functions."""

import functools

import matplotlib as mpl
import numpy as np
from astropy import units as u

from yieldplotlib.key_map import KEY_MAP


def get_nice_number(value, round=False):
    """Calculates a "nice" number for labeling axes in a plot.

    Args:
        value (float):
            The value to be transformed into a "nice" number.
        round (bool, optional):
            If True, rounds the number to the nearest "nice" number. If False,
            the number is only scaled to be a "nice" number.

    Returns:
        float:
            A "nice" number that is a rounded or scaled version of the input value.
    """
    if value == 0:
        return 0

    # Calculate the exponent of the base 10 representation of the value
    exponent = np.floor(np.log10(value))

    # Calculate the fractional part of the value
    fraction = value / 10**exponent

    # Determine the "nice" fraction based on whether rounding is required
    if round:
        if fraction < 1.5:
            nice_fraction = 1
        elif fraction < 3:
            nice_fraction = 2
        elif fraction < 7:
            nice_fraction = 5
        else:
            nice_fraction = 10
    else:
        if fraction <= 1:
            nice_fraction = 1
        elif fraction <= 2:
            nice_fraction = 2
        elif fraction <= 5:
            nice_fraction = 5
        else:
            nice_fraction = 10

    # Return the "nice" number by scaling the nice fraction by the exponent
    return nice_fraction * 10**exponent


def calculate_axis_limits_and_ticks(data_min, data_max, num_ticks=5, exact=False):
    """Calculates the axis limits and tick spacing for a plot.

    Args:
        data_min (float):
            The minimum value of the data.
        data_max (float):
            The maximum value of the data.
        num_ticks (int, optional):
            The desired number of tick marks on the axis. Default is 5.
        exact (bool, optional):
            If True, use exact min and max values for the limits. If False, the
            limits are adjusted to "nice" values.

    Returns:
        tuple:
            nice_min (float):
                The adjusted minimum axis limit.
            nice_max (float):
                The adjusted maximum axis limit.
            tick_spacing (float):
                The spacing between ticks.
            offset (float):
                A small offset to apply to the axis limits for better visualization.
    """
    # Calculate the "nice" range span of the data
    range_span = get_nice_number(data_max - data_min, round=True)

    # Calculate the "nice" tick spacing based on the range span and desired
    # number of ticks
    tick_spacing = get_nice_number(range_span / (num_ticks - 1), round=True)

    if exact:
        # Use exact min and max values if specified
        nice_min = data_min
        nice_max = data_max
    else:
        # Adjust the min and max values to "nice" numbers
        nice_min = np.floor(data_min / tick_spacing) * tick_spacing
        nice_max = np.ceil(data_max / tick_spacing) * tick_spacing

    # Calculate a small offset for better visualization of the axis limits
    offset = 0.025 * tick_spacing

    return nice_min, nice_max, tick_spacing, offset


def is_monotonic(x):
    """Checks if an array is monotonic."""
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)


def rgetattr(obj, attr, *args):
    """Recursively get attributes of an object."""

    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def discretize_colormap(num_colors, colormap_name, start_frac=0.1, end_frac=0.9):
    """Returns evenly spaced discrete colors from a matplotlib colormap."""
    cmap = mpl.colormaps[colormap_name]
    colors = cmap(np.linspace(start_frac, end_frac, num_colors))
    return colors


def find_unit_for_module_key(module_key, module_name, key_map):
    """Find the unit for a given module-specific key.

    Searches through the KEY_MAP to find a mapping where the provided module key
    matches the 'name' field for the specified module. If found, returns the
    corresponding unit.

    Args:
        module_key (str):
            The module-specific key (e.g., 'Angdiam (mas)' for AYO,
            'pixelScale' for EXOSIMS).
        module_name (str):
            The name of the module (e.g., 'AYOCSVFile', 'EXOSIMSInputFile').
        key_map (dict):
            The key mapping dictionary to use for lookups.

    Returns:
        str or None:
            The unit string if found, None otherwise.
    """
    for yieldplotlib_key, module_data in key_map.items():
        # Check if this entry has data for the specified module
        if module_name in module_data:
            module_info = module_data[module_name]
            # Check if the 'name' field matches the module key
            if module_info.get("name") == module_key:
                return module_info.get("unit", "")

    return None


def get_unit(key, module_name, find_unit_func=None):
    """Get the associated unit for a given key.

    This generic method handles both yieldplotlib keys and module-specific keys:
    1. First tries a direct lookup in KEY_MAP (assuming key is a yieldplotlib key)
    2. If not found, tries to find the corresponding yieldplotlib key by looking up
       the module-specific key in KEY_MAP

    Args:
        key (str):
            The key to look up the unit for (can be either a yieldplotlib key
            or a module-specific key).
        module_name (str):
            The name of the module making the request (used for KEY_MAP lookup).
        find_unit_func (callable, optional):
            Optional custom fallback function that takes a key and returns a
            unit string. If None, the built-in find_unit_for_module_key
            function will be used.

    Returns:
        astropy.units.Unit or None:
            The astropy Unit object if found, None otherwise.
    """
    # First try direct lookup (for yieldplotlib keys)
    if key in KEY_MAP and module_name in KEY_MAP[key]:
        unit = KEY_MAP[key][module_name].get("unit", "")
    elif find_unit_func is not None:
        # If not found, try to find the corresponding yieldplotlib key
        # by using the provided custom fallback function
        unit = find_unit_func(key)
    else:
        # Use the built-in generic function as a fallback
        unit = find_unit_for_module_key(key, module_name, KEY_MAP)

    if unit:
        astropy_unit = u.Unit(unit)
        return astropy_unit

    return None
