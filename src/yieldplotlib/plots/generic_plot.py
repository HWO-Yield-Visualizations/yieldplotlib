"""Generic plotting utilities that work with any DirectoryNode.

This module extends matplotlib's Axes class with methods for plotting data directly
from DirectoryNode objects using key-based access.
"""

import inspect
import sys

import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize


def ypl_plot(self, directory_node, x, y, c=None, autolabel=True, **kwargs):
    """Plot data from a DirectoryNode.

    Args:
        self (matplotlib.axes.Axes):
            The axes to plot the data on.
        directory_node (DirectoryNode):
            The data source to extract plotting variables from.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.
        c (str, optional):
            Key for color data.
        autolabel (bool, optional):
            Whether to automatically label the axes.
        **kwargs:
            Additional keyword arguments passed to the plot method.

    Returns:
        matplotlib.lines.Line2D: The line(s) created.
    """
    # Extract data
    x_data = directory_node.get(x) if x else None
    y_data = directory_node.get(y) if y else None

    # Basic validation
    if x_data is None:
        raise ValueError(f"Could not find data for key: x='{x}'")
    if y_data is None:
        raise ValueError(f"Could not find data for key: y='{y}'")

    plot_kwargs = kwargs.copy()

    # Handle units for x and y data
    x_unit, y_unit = None, None

    if isinstance(x_data, u.Quantity):
        x_unit, x_data = x_data.unit, x_data.value

    if isinstance(y_data, u.Quantity):
        y_unit, y_data = y_data.unit, y_data.value

    # Set axis labels with units if available
    if autolabel:
        _xlabel = x.replace("_", " ").title()
        _ylabel = y.replace("_", " ").title()
        _xlabel += f" ({x_unit})" if x_unit else ""
        _ylabel += f" ({y_unit})" if y_unit else ""
        self.set_xlabel(_xlabel)
        self.set_ylabel(_ylabel)

    # Handle additional data parameters
    if c:
        if isinstance(c, str):
            c_data = directory_node.get(c)
        else:
            c_data = c
        if c_data is not None:
            # Handle units for color data
            _clabel = c.replace("_", " ").title()
            if isinstance(c_data, u.Quantity):
                c_unit = c_data.unit
                c_data = c_data.value
                _clabel += f" [{c_unit}]"

            plot_kwargs["c"] = c_data

            # Add colorbar if requested
            if kwargs.get("colorbar", True):
                cmap = plot_kwargs.get("cmap", plt.cm.viridis)
                norm = Normalize(vmin=np.min(c_data), vmax=np.max(c_data))
                sm = ScalarMappable(cmap=cmap, norm=norm)
                sm.set_array([])
                cbar = plt.colorbar(sm, ax=self)
                cbar.set_label(_clabel)

    # Use the standard plot method with our extracted data
    return self.plot(x_data, y_data, **plot_kwargs)


def ypl_scatter(self, directory_node, x, y, c=None, autolabel=True, **kwargs):
    """Create a scatter plot from DirectoryNode data.

    Args:
        self (matplotlib.axes.Axes):
            The axes to plot the scatter on.
        directory_node (DirectoryNode):
            The data source to extract plotting variables from.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.
        c (str or array-like, optional):
            Key for color data or an array of color values.
        autolabel (bool, optional):
            Whether to automatically label the axes.
        **kwargs:
            Additional keyword arguments passed to the scatter method.

    Returns:
        matplotlib.collections.PathCollection: The scatter plot created.
    """
    # Extract data
    x_data = directory_node.get(x) if x else None
    y_data = directory_node.get(y) if y else None

    # Basic validation
    if x_data is None:
        raise ValueError(f"Could not get key '{x}' from {directory_node}")
    if y_data is None:
        raise ValueError(f"Could not get key '{y}' from {directory_node}")

    scatter_kwargs = kwargs.copy()

    # Handle units for x and y data
    x_unit = None
    y_unit = None

    if isinstance(x_data, u.Quantity):
        x_unit, x_data = x_data.unit, x_data.value

    if isinstance(y_data, u.Quantity):
        y_unit, y_data = y_data.unit, y_data.value

    # Set axis labels with units if available
    if autolabel:
        _xlabel = x.replace("_", " ").title()
        _ylabel = y.replace("_", " ").title()
        _xlabel += f" ({x_unit})" if x_unit else ""
        _ylabel += f" ({y_unit})" if y_unit else ""
        self.set_xlabel(_xlabel)
        self.set_ylabel(_ylabel)

    # Handle additional data parameters
    if c is not None:
        if isinstance(c, str):
            c_data = directory_node.get(c)
        else:
            c_data = c
        if c_data is not None:
            # Handle units for color data
            if isinstance(c, str):
                _clabel = c.replace("_", " ").title()
                if isinstance(c_data, u.Quantity):
                    c_unit, c_data = c_data.unit, c_data.value
                    _clabel += f" [{c_unit}]"
            else:
                # If c was passed as an array, we don't know the unit
                # or label, so we don't add anything
                pass

            scatter_kwargs["c"] = np.array(c_data)

            # Add colorbar if requested
            if kwargs.get("colorbar", False):
                cmap = scatter_kwargs.get("cmap", plt.cm.viridis)
                norm = Normalize(vmin=np.min(c_data), vmax=np.max(c_data))
                sm = ScalarMappable(cmap=cmap, norm=norm)
                sm.set_array([])
                cbar = plt.colorbar(sm, ax=self)
                cbar.set_label(_clabel)
                # Remove the colorbar from the kwargs
                scatter_kwargs.pop("colorbar", None)

    # Use the standard scatter method with our extracted data
    return self.scatter(x_data, y_data, **scatter_kwargs)


def ypl_hist(self, directory_node, x, autolabel=True, reference_unit=None, **kwargs):
    """Create a histogram from DirectoryNode data.

    Args:
        self (matplotlib.axes.Axes):
            The axes to plot the histogram on.
        directory_node (DirectoryNode):
            The data source to extract plotting variables from.
        x (str):
            Key for the data to be histogrammed.
        autolabel (bool, optional):
            Whether to automatically label the axes.
        reference_unit (astropy.units.Unit, optional):
            Reference unit to convert data to. If provided, all data will be converted
            to this unit before plotting. This ensures unit consistency across
            multiple datasets.
        **kwargs:
            Additional keyword arguments passed to the hist method.

    Returns:
        tuple: (n, bins, patches) as returned by hist
    """
    # Extract data
    x_data = directory_node.get(x) if x else None

    # Basic validation
    if x_data is None:
        raise ValueError(f"Could not get key '{x}' from {directory_node}")

    hist_kwargs = kwargs.copy()

    # Handle units for the data
    x_unit = None

    if isinstance(x_data, u.Quantity):
        # Save the original unit for labeling
        x_unit = x_data.unit

        # If reference unit provided, convert the data
        if reference_unit is not None:
            if x_data.unit != reference_unit:
                x_data = x_data.to(reference_unit)
                # Update the display unit
                x_unit = reference_unit

        # Extract numerical values for histogram
        x_data = x_data.value
        if "bins" in hist_kwargs and isinstance(hist_kwargs["bins"], u.Quantity):
            hist_kwargs["bins"] = hist_kwargs["bins"].to(x_unit).value.astype(int)

    # Set axis label with unit if available
    if autolabel:
        _xlabel = x.replace("_", " ").title()
        _xlabel += f" ({x_unit})" if x_unit else ""
        self.set_xlabel(_xlabel)

    # Use the standard hist method with our extracted data
    return self.hist(x_data, **hist_kwargs)


def extend_matplotlib():
    """Extend matplotlib's Axes class with our DirectoryNode methods.

    This automatically adds all functions with the 'ypl_' prefix in this file
    to the matplotlib Axes class, so they can be used directly on any axes.
    """
    # Get all objects in the current module
    current_module = sys.modules[__name__]

    # Find all functions with the ypl_ prefix
    for name, obj in inspect.getmembers(current_module):
        # Check if it's a function and starts with ypl_
        if inspect.isfunction(obj) and name.startswith("ypl_"):
            # Only add if it doesn't already exist on Axes
            if not hasattr(Axes, name):
                setattr(Axes, name, obj)


def subplots(*args, **kwargs):
    """A simple wrapper around plt.subplots().

    Ensures our extensions are applied before returning.

    Args:
        *args: Arguments to pass to plt.subplots().
        **kwargs: Keyword arguments to pass to plt.subplots().

    Returns:
        tuple: (fig, ax) as returned by plt.subplots()
    """
    extend_matplotlib()
    return plt.subplots(*args, **kwargs)
