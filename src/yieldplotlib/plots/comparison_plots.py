"""Utilities for comparing data across multiple DirectoryNode objects.

This module provides functions for easily comparing data from multiple directory nodes
in a single plot or across multiple subplots.
"""

import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np


def _get_plot_method(ax, plot_type):
    """Get the appropriate plot method for the given plot type.

    Args:
        ax (matplotlib.axes.Axes):
            The axes to get the plot method from.
        plot_type (str):
            Type of plot to create. Options are 'scatter', 'plot', or 'hist'.

    Returns:
        callable:
            The plot method to use.

    Raises:
        ValueError:
            If plot_type is not supported.
    """
    plot_method = getattr(ax, f"ypl_{plot_type}")
    if plot_method is None:
        raise ValueError(
            (f"Unsupported plot_type: {plot_type}. Use 'scatter', 'plot', or 'hist'.")
        )
    return plot_method


def _calculate_consistent_bins(directories, x, bins_param=None):
    """Calculate consistent histogram bins across multiple directories.

    Args:
        directories (list):
            List of DirectoryNode objects.
        x (str):
            Key for data to calculate bins for.
        bins_param (int, sequence, or str, optional):
            Bins parameter to use. If None, auto-calculated bins will be used.

    Returns:
        array-like:
            Calculated bin edges to use for histograms.
    """
    all_data = []
    data_with_units = None

    # Collect all data from all directories
    for directory in directories:
        data = directory.get(x)
        if data is not None:
            all_data.extend(np.asarray(data).flatten())
            # Keep track of any Quantity objects to preserve units
            if isinstance(data, u.Quantity) and data_with_units is None:
                data_with_units = data

    if not all_data:
        return None

    # Calculate bins based on all data combined
    if bins_param is not None:
        bins = bins_param
    else:
        bins = np.histogram_bin_edges(all_data, bins="auto")

    # Preserve units if needed
    if data_with_units is not None:
        bins = bins * data_with_units.unit

    return bins


def _validate_y_parameter(plot_type, y):
    """Validate that y parameter is provided when needed.

    Args:
        plot_type (str):
            Type of plot to create.
        y (str):
            Key for y-axis data.

    Raises:
        ValueError:
            If y is required but not provided.
    """
    if plot_type in ["scatter", "plot"] and y is None:
        raise ValueError(f"y must be provided for {plot_type} plots")


def _handle_histogram(plot_method, directory, x, plot_kwargs):
    """Handle histogram plotting and legend.

    Args:
        plot_method (callable):
            The histogram plotting method.
        directory (DirectoryNode):
            The directory to plot data from.
        x (str):
            Key for x-axis data.
        plot_kwargs (dict):
            Keyword arguments for the plot.

    Returns:
        tuple:
            (n, bins, patches) from the histogram.
    """
    # Remove keys that are not valid for histogram plotting
    _kwargs = plot_kwargs.copy()
    _kwargs.pop("c", None)
    _kwargs.pop("cmap", None)
    _kwargs.pop("alpha", None)
    _kwargs.pop("s", None)
    _kwargs.pop("marker", None)

    _, _, patches = plot_method(directory, x=x, **_kwargs)
    # Store the first patch for legend purposes
    if "label" in plot_kwargs:
        patches[0].set_label(plot_kwargs["label"])
    else:
        patches[0].set_label(directory.__class__.__name__)
    return patches


def _setup_figure_layout(fig, suptitle=None):
    """Set up figure layout and adjust for suptitle if present.

    Args:
        fig (matplotlib.figure.Figure):
            The figure to adjust.
        suptitle (str, optional):
            Super title for the entire figure.
    """
    fig.tight_layout()
    if suptitle:
        fig.subplots_adjust(top=0.9)


def _create_subplot_titles(directories, specs=None):
    """Create titles for subplots.

    Args:
        directories (list):
            List of DirectoryNode objects.
        specs (list, optional):
            List of plot specifications. If provided, creates descriptive titles.

    Returns:
        list:
            List of titles for each subplot.
    """
    if specs is None:
        return [f"{d.__class__.__name__}" for d in directories]

    titles = []
    for d in directories:
        for s in specs:
            if "y" in s:
                titles.append(f"{s.get('x', 'x')} vs {s.get('y', 'y')}")
            else:
                titles.append(f"{s.get('x', 'x')} distribution")
    return titles


def _get_data_shape(directory, key):
    """Get the shape of data for a given key.

    Args:
        directory (DirectoryNode):
            The directory to get data from.
        key (str):
            The key to get data for.

    Returns:
        tuple:
            The shape of the data array.

    Raises:
        ValueError:
            If the key doesn't exist or the data shape is unexpected.
    """
    data = directory.get(key)
    if data is None:
        raise ValueError(f"Key {key} not found in {directory}")

    shape = np.asarray(data).shape
    if len(shape) == 0:
        raise ValueError(f"Unexpected data shape for key {key}: {shape}")
    return shape


def _validate_data_shapes(directory, x, y):
    """Validate that x and y data shapes are compatible for plotting.

    Args:
        directory (DirectoryNode):
            The directory to get data from.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.

    Raises:
        ValueError:
            If the data shapes are incompatible for plotting.
    """
    x_shape = _get_data_shape(directory, x)
    y_shape = _get_data_shape(directory, y)

    # For scatter and line plots, both must have the same number of points
    if x_shape[0] != y_shape[0]:
        raise ValueError(
            f"Data shapes are incompatible for plotting {x} vs {y}. "
            f"x has {x_shape[0]} points, y has {y_shape[0]} points. "
            "This usually indicates an invalid comparison."
        )


def _validate_histogram_data(directory, x):
    """Validate that data is suitable for histogram plotting.

    Args:
        directory (DirectoryNode):
            The directory to get data from.
        x (str):
            Key for x-axis data.

    Raises:
        ValueError:
            If the data is not suitable for histogram plotting.
    """
    x_shape = _get_data_shape(directory, x)

    # For histograms, we need multiple data points
    if x_shape[0] <= 1:
        raise ValueError(
            f"Data for {x} has only {x_shape[0]} point(s). "
            "Histograms require multiple data points."
        )


def _validate_color_key(directory, c):
    """Validate that color key data exists and has compatible shape.

    Args:
        directory (DirectoryNode):
            The directory to get data from.
        c (str):
            Key for color data.

    Raises:
        ValueError:
            If the color key data is invalid.
    """
    if c is None:
        return

    data = directory.get(c)
    if data is None:
        raise ValueError(f"Color key {c} not found in {directory}")

    shape = np.asarray(data).shape
    if len(shape) == 0:
        raise ValueError(f"Unexpected data shape for color key {c}: {shape}")


def _validate_color_data_shapes(directory, x, y, c):
    """Validate that color data shape is compatible with x and y data.

    Args:
        directory (DirectoryNode):
            The directory to get data from.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.
        c (str):
            Key for color data.

    Raises:
        ValueError:
            If the data shapes are incompatible.
    """
    if c is None:
        return

    x_shape = _get_data_shape(directory, x)
    c_shape = _get_data_shape(directory, c)

    # For scatter and line plots, color data must have same number of points as x/y
    if x_shape[0] != c_shape[0]:
        raise ValueError(
            f"Color data shape is incompatible for plotting {x} vs {y} with color {c}. "
            f"x has {x_shape[0]} points, color data has {c_shape[0]} points."
        )


def _plot_data(ax, directory, x, y, plot_type, plot_kwargs):
    """Plot data using the appropriate method.

    Args:
        ax (matplotlib.axes.Axes):
            The axes to plot on.
        directory (DirectoryNode):
            The directory to plot data from.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.
        plot_type (str):
            Type of plot to create.
        plot_kwargs (dict):
            Keyword arguments for the plot.

    Returns:
        The plot object(s) created.

    Raises:
        ValueError:
            If the data shapes are incompatible for the requested plot type.
    """
    plot_method = _get_plot_method(ax, plot_type)
    _validate_y_parameter(plot_type, y)

    # Extract color key if present
    c = plot_kwargs.pop("c", None)
    if c is not None:
        _validate_color_key(directory, c)
        _validate_color_data_shapes(directory, x, y, c)
        plot_kwargs["c"] = directory.get(c)

    if plot_type == "hist":
        # Validate histogram data
        _validate_histogram_data(directory, x)
        return _handle_histogram(plot_method, directory, x, plot_kwargs)
    else:
        # Validate scatter/line plot data
        _validate_data_shapes(directory, x, y)
        return plot_method(directory, x=x, y=y, **plot_kwargs)


def compare(
    ax,
    directories,
    x,
    y=None,
    plot_type="scatter",
    labels=None,
    colors=None,
    markers=None,
    linestyles=None,
    legend=True,
    **kwargs,
):
    """Plot data from multiple directories on a single axes.

    Args:
        ax (matplotlib.axes.Axes):
            The axes to plot on.
        directories (list):
            List of DirectoryNode objects to plot.
        x (str):
            Key for x-axis data.
        y (str):
            Key for y-axis data.
        plot_type (str, optional):
            Type of plot to create. Options are 'scatter', 'plot', or 'hist'.
            Default is 'scatter'.
        labels (list, optional):
            List of labels for each directory node. If None, uses the directory node
            class names.
        colors (list, optional):
            List of colors for each directory. If None, uses default color cycle.
        markers (list, optional):
            List of markers for scatter plots. Ignored for other plot types.
        linestyles (list, optional):
            List of linestyles for line plots. Ignored for other plot types.
        legend (bool, optional):
            Whether to add a legend. Default is True.
        **kwargs:
            Additional keyword arguments passed to the plot method. Can include 'c' for
            color key data.

    Returns:
        matplotlib.axes.Axes:
            The axes with the plot.
    """
    # Generate labels if not provided
    if labels is None:
        labels = [d.__class__.__name__ for d in directories]
    elif not isinstance(labels, list):
        labels = [labels]

    # Ensure we have enough labels
    if len(labels) < len(directories):
        labels.extend([d.__class__.__name__ for d in directories[len(labels) :]])

    # Default markers and linestyles
    default_markers = ["o", "s", "^", "D", "v", "<", ">", "p", "*", "h", "H", "+", "x"]
    default_linestyles = ["-", "--", "-.", ":"]

    # Set up markers if needed for scatter
    if markers is None and plot_type == "scatter":
        markers = default_markers

    # Set up linestyles if needed for plot
    if linestyles is None and plot_type == "plot":
        linestyles = default_linestyles

    # For histograms, calculate consistent bins across all directories
    if plot_type == "hist":
        bins = _calculate_consistent_bins(directories, x, kwargs.get("bins"))
        if bins is not None:
            kwargs["bins"] = bins

    # Plot each dataset
    for i, (directory, label) in enumerate(zip(directories, labels)):
        # Create plot kwargs for this dataset
        plot_kwargs = kwargs.copy()

        # Add label
        plot_kwargs["label"] = label

        # Add color if provided (only if not using color key)
        if colors is not None and i < len(colors) and "c" not in plot_kwargs:
            plot_kwargs["color"] = colors[i]

        # Add marker or linestyle depending on plot type
        if plot_type == "scatter" and markers is not None:
            plot_kwargs["marker"] = markers[i % len(markers)]
        elif plot_type == "plot" and linestyles is not None:
            plot_kwargs["linestyle"] = linestyles[i % len(linestyles)]

        # Plot the data
        _plot_data(ax, directory, x, y, plot_type, plot_kwargs)

    # Add legend if requested
    if legend:
        ax.legend()

    return ax


def multi(
    directories,
    x,
    y=None,
    plot_type="scatter",
    figsize=None,
    suptitle=None,
    layout=None,
    sharex=True,
    sharey=True,
    titles=None,
    **kwargs,
):
    """Create a multi-panel figure with one subplot per directory.

    Args:
        directories (list):
            List of DirectoryNode objects to plot.
        x (str):
            Key for x-axis data.
        y (str, optional):
            Key for y-axis data. Not required for histogram plots.
        plot_type (str, optional):
            Type of plot to create. Options are 'scatter', 'plot', or 'hist'.
            Default is 'scatter'.
        figsize (tuple, optional):
            Figure size (width, height) in inches.
        suptitle (str, optional):
            Super title for the entire figure.
        layout (tuple, optional):
            Layout for subplots as (rows, cols). If None, will be set automatically.
        sharex (bool, optional):
            Whether to share the x-axis across subplots. Default is True.
        sharey (bool, optional):
            Whether to share the y-axis across subplots. Default is True.
        titles (list, optional):
            List of titles for each subplot. If None, uses directory names.
        **kwargs:
            Additional keyword arguments passed to the plot method. Can include 'c' for
            color key data.

    Returns:
        tuple:
            (fig, axes) - The figure and array of axes created.
    """
    n_plots = len(directories)

    # Determine layout if not provided
    if layout is None:
        # Try to make it as square as possible
        n_cols = int(np.ceil(np.sqrt(n_plots)))
        n_rows = int(np.ceil(n_plots / n_cols))
        layout = (n_rows, n_cols)
    else:
        n_rows, n_cols = layout

    # Create subplot titles if not provided
    if titles is None:
        titles = _create_subplot_titles(directories)

    # Ensure we have the right number of titles
    if len(titles) < n_plots:
        titles.extend([f"Directory {i + 1}" for i in range(len(titles), n_plots)])

    # Create figure and axes
    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        squeeze=False,
    )

    # For histograms, calculate consistent bins across all directories
    if plot_type == "hist":
        bins = _calculate_consistent_bins(directories, x, kwargs.get("bins"))
        if bins is not None:
            kwargs["bins"] = bins

    # Flatten axes for easy iteration
    axes_flat = axes.flatten()

    # Plot each directory in its own subplot
    for i, (directory, title) in enumerate(zip(directories, titles)):
        if i < len(axes_flat):
            ax = axes_flat[i]

            # Create plot kwargs for this dataset
            plot_kwargs = kwargs.copy()

            # Plot the data
            _plot_data(ax, directory, x, y, plot_type, plot_kwargs)

            # Set title for this subplot
            ax.set_title(title)

    # Hide any unused subplots
    for i in range(n_plots, len(axes_flat)):
        axes_flat[i].set_visible(False)

    # Add super title if provided
    if suptitle:
        fig.suptitle(suptitle)

    # Adjust layout
    _setup_figure_layout(fig, suptitle)

    return fig, axes


def panel(
    directories,
    *specs,
    figsize=None,
    suptitle=None,
    layout=None,
    sharex=True,
    sharey=True,
    titles=None,
    **kwargs,
):
    """Create a multi-panel figure with customizable plotting specifications.

    Args:
        directories (list):
            List of DirectoryNode objects to plot.
        *specs:
            Variable number of plot specifications. Each spec is a dictionary with keys:
            - 'x': Key for x-axis data
            - 'y': Key for y-axis data (not required for histograms)
            - 'plot_type': Type of plot ('scatter', 'plot', 'hist')
            - 'c': Key for color data (optional)
            - Any other kwargs specific to that plot
        figsize (tuple, optional):
            Figure size (width, height) in inches.
        suptitle (str, optional):
            Super title for the entire figure.
        layout (tuple, optional):
            Layout for subplots as (rows, cols). If None, will be determined
            automatically.
        sharex (bool, optional):
            Whether to share the x-axis across subplots. Default is True.
        sharey (bool, optional):
            Whether to share the y-axis across subplots. Default is True.
        titles (list, optional):
            List of titles for each subplot. If None, uses descriptive titles.
        **kwargs:
            Additional keyword arguments passed to all plot methods.

    Returns:
        tuple:
            (fig, axes) - The figure and array of axes created.

    Example:
        fig, axes = ypl.panel(
            [exosims, ayo],
            {'x': 'star_dist', 'y': 'star_L', 'plot_type': 'scatter', 'c': 'star_L',
            'alpha': 0.7},
            {'x': 'wavelength', 'y': 'core_thruput', 'plot_type': 'plot', 'lw': 2},
            titles=['Star Properties', 'Throughput Curve']
        )
    """
    # Validate input
    if not specs:
        raise ValueError("At least one plot specification must be provided")

    n_dirs = len(directories)
    n_specs = len(specs)
    n_plots = n_dirs * n_specs

    # Determine layout if not provided
    if layout is None:
        # Default: one row per directory, one column per spec
        n_rows = n_dirs
        n_cols = n_specs
        layout = (n_rows, n_cols)
    else:
        n_rows, n_cols = layout

    # Create figure and axes
    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        squeeze=False,
    )

    # Create subplot titles if not provided
    if titles is None:
        titles = _create_subplot_titles(directories, specs)

    # Ensure we have the right number of titles
    if len(titles) < n_plots:
        titles.extend([f"Plot {i + 1}" for i in range(len(titles), n_plots)])

    # Prepare consistent bins for each spec if it's a histogram
    spec_bins = {}
    for j, spec in enumerate(specs):
        plot_type = spec.get("plot_type", "scatter")
        x = spec.get("x")

        if plot_type == "hist" and x:
            # Combine all kwargs: global kwargs + spec-specific
            combined_kwargs = kwargs.copy()
            for k, v in spec.items():
                if k not in ["x", "y", "plot_type"]:
                    combined_kwargs[k] = v

            spec_bins[j] = _calculate_consistent_bins(
                directories, x, combined_kwargs.get("bins")
            )

    # Plot each directory-spec combination
    plot_idx = 0
    for i, directory in enumerate(directories):
        for j, spec in enumerate(specs):
            # Get axes - we can use a 2D layout or a flattened 1D layout
            if n_rows == 1:
                ax = axes[0, j]
            elif n_cols == 1:
                ax = axes[i, 0]
            else:
                ax = axes[i, j]

            # Extract plot type and x, y keys
            plot_type = spec.get("plot_type", "scatter")
            x = spec.get("x")
            y = spec.get("y", None)

            if not x:
                raise ValueError(f"Plot specification must include 'x' key: {spec}")

            if plot_type in ["scatter", "plot"] and not y:
                raise ValueError(
                    f"Plot specification for '{plot_type}' must include 'y' key: {spec}"
                )

            # Combine global kwargs with spec-specific kwargs
            plot_kwargs = kwargs.copy()
            for k, v in spec.items():
                if k not in ["x", "y", "plot_type"]:
                    plot_kwargs[k] = v

            # Apply consistent bins if this is a histogram
            if plot_type == "hist" and j in spec_bins and spec_bins[j] is not None:
                plot_kwargs["bins"] = spec_bins[j]

            # Plot the data
            _plot_data(ax, directory, x, y, plot_type, plot_kwargs)

            # Set title for this subplot
            title = (
                titles[plot_idx] if plot_idx < len(titles) else f"Plot {plot_idx + 1}"
            )
            ax.set_title(title)
            plot_idx += 1

    # Add super title if provided
    if suptitle:
        fig.suptitle(suptitle)

    # Adjust layout
    _setup_figure_layout(fig, suptitle)

    return fig, axes


def xy_grid(
    directories,
    x_keys,
    y_keys,
    plot_type="scatter",
    figsize=None,
    suptitle=None,
    legend=True,
    sharex=False,
    sharey=False,
    titles=None,
    **kwargs,
):
    """Create a grid of plots where each subplot corresponds to a set of (x, y) keys.

    Each subplot will plot all of the provided DirectoryNode objects using the
    specified plot type.

    Args:
        directories (list):
            List of DirectoryNode objects.
        x_keys (list):
            List of keys for x-axis data.
        y_keys (list):
            List of keys for y-axis data.
        plot_type (str, optional):
            Type of plot to create. Options are 'scatter', 'plot', or 'hist'.
             Default is 'scatter'.
        figsize (tuple, optional):
            Figure size in inches.
        suptitle (str, optional):
            Super title for the entire figure.
        legend (bool, optional):
            Whether to add a legend to each subplot. Default is True.
        sharex (bool, optional):
            Whether to share the x-axis across subplots. Default is True.
        sharey (bool, optional):
            Whether to share the y-axis across subplots. Default is True.
        titles (list, optional):
            List of titles for each subplot. Must have length equal to
            len(x_keys) * len(y_keys) if provided.
        **kwargs:
            Additional keyword arguments passed to the plotting method. Can
            include 'c' for color key data.

    Returns:
        tuple:
            (fig, axes) where fig is the matplotlib Figure and axes is a 2D
            array of Axes.
    """
    if not isinstance(x_keys, list):
        raise ValueError("x_keys must be a list.")
    if y_keys is not None and not isinstance(y_keys, list):
        raise ValueError("y_keys must be a list or None.")

    # For histograms all y keys are None
    if y_keys is None:
        n_rows = 1
        y_keys = [None]
    else:
        n_rows = len(y_keys)
    n_cols = len(x_keys)

    if figsize is None:
        figsize = (n_cols * 5, n_rows * 5)

    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=figsize, sharex=sharex, sharey=sharey, squeeze=False
    )

    # Generate default titles if not provided
    default_titles = []
    if y_keys[0] is None:
        for x_key in x_keys:
            default_titles.append(x_key)
    else:
        for y_key in y_keys:
            for x_key in x_keys:
                default_titles.append(f"{y_key} vs {x_key}")

    if titles is None:
        titles = default_titles
    else:
        if len(titles) < n_rows * n_cols:
            titles.extend(default_titles[len(titles) :])

    # Default markers and linestyles
    default_markers = ["o", "s", "^", "D", "v", "<", ">", "p", "*", "h", "H", "+", "x"]
    default_linestyles = ["-", "--", "-.", ":"]

    # For each x_key, calculate consistent bins if histogram
    if plot_type == "hist":
        x_key_bins = {}
        for j, x_key in enumerate(x_keys):
            x_key_bins[j] = _calculate_consistent_bins(
                directories, x_key, kwargs.get("bins")
            )

    # Loop over each grid cell and plot
    for i, y_key in enumerate(y_keys):
        for j, x_key in enumerate(x_keys):
            ax = axes[i, j]

            # If histogram, set consistent bins for this x_key
            if plot_type == "hist" and j in x_key_bins and x_key_bins[j] is not None:
                local_kwargs = kwargs.copy()
                local_kwargs["bins"] = x_key_bins[j]
            else:
                local_kwargs = kwargs

            # For each directory, plot on this axis
            for idx, directory in enumerate(directories):
                plot_kwargs = local_kwargs.copy()
                # Use the directory class name as default label if not provided
                if "label" not in plot_kwargs:
                    plot_kwargs["label"] = directory.__class__.__name__

                # Add marker or linestyle depending on plot type
                if plot_type == "scatter":
                    plot_kwargs["marker"] = default_markers[idx % len(default_markers)]
                elif plot_type == "plot":
                    plot_kwargs["linestyle"] = default_linestyles[
                        idx % len(default_linestyles)
                    ]

                # Plot the data
                _plot_data(ax, directory, x_key, y_key, plot_type, plot_kwargs)

            idx = i * n_cols + j
            ax.set_title(titles[idx])
            if legend:
                ax.legend()

    if suptitle:
        fig.suptitle(suptitle)
    _setup_figure_layout(fig, suptitle)

    return fig, axes
