"""The base `Plot` class.

`Plot` is a class designed to facilitate the creation and customization of
various types of plots using Matplotlib. It provides a flexible framework for
managing plot settings, axis configurations, and rendering options.
"""

import inspect

import numpy as np

import yieldplotlib.util as util


class Plot:
    """Base class for all plots."""

    def __init__(self, plot_kwargs=None, ax_kwargs=None):
        """Base class for all plots."""
        self.ax = None

        # Set the default plot_kwargs, then update with any user-specified
        # kwargs. The plot_kwargs are used in the plot call.
        default_plot_kwargs = {}
        self.plot_kwargs = default_plot_kwargs
        if plot_kwargs is not None:
            self.plot_kwargs.update(plot_kwargs)

        # Set the default ax_kwargs, then update with any user-specified
        # kwargs. The ax_kwargs are used to set the axes properties with the
        # ax.set method. Instead of using all the ax.set_xlabel, ax.set_title,
        # ax.set_yticks, etc. functions we can pass in a dictionary that has
        # {'xlabel': 'my_xlabel', 'xlim': (0, 10), 'title': "My title"}.
        default_ax_kwargs = {"xlabel": "x", "ylabel": "y"}
        self.ax_kwargs = default_ax_kwargs
        if ax_kwargs is not None:
            self.ax_kwargs.update(ax_kwargs)

        # Initialize alt text for the plot.
        self._alt_text = ""

    def render(self):
        """Method to render the plot."""
        self.adjust_settings()

    def draw_plot(self, plot_kwargs=None):
        """Method to draw the plot.

        Args:
            plot_kwargs (dict, optional):
                Dictionary of kwargs to pass to the plot

        """
        self.generic_plot(self.data, plot_kwargs=plot_kwargs)

    def generic_plot(self, plot_method, data, plot_kwargs=None):
        """Generic plot method that can be used by any plot type.

        Args:
            plot_method (str):
                Method to use to plot the data. For example, "plot" or "scatter".
            data (tuple, optional):
                Tuple of data to plot, e.g. (x, y) or (x, y, z).
            plot_kwargs (dict, optional):
                Dictionary of kwargs to pass to the plot
        """
        # Plot method is a string like "plot" or "scatter"
        plot_method = getattr(self.ax, plot_method)

        if plot_kwargs is None:
            plot_kwargs = self.plot_kwargs
        plot_method(*data, **plot_kwargs)

        self.ax.set(**self.ax_kwargs)

    def adjust_settings(self):
        """Method to adjust the settings of the plot.

        This method exists to be overridden by subclasses of Plot that need
        more customization than the generic_settings method.
        """
        self.generic_settings()

    def generic_settings(self):
        """Method to set the generic settings of the plot."""
        # Evaulate any f-strings provided in ax_kwargs
        original_kwargs = {}
        for key, val in self.ax_kwargs.items():
            if isinstance(val, str):
                if "animation_value" in val:
                    original_kwargs[key] = val
                    self.ax_kwargs[key] = eval(f"f{val}")

        # Get the keys that are settable with ax.set
        ax_set_keys = inspect.signature(self.ax.set).parameters.keys()
        settable_kwargs = {
            key: val for key, val in self.ax_kwargs.items() if key in ax_set_keys
        }
        # Set all the axes properties based on ax_kwargs
        self.ax.set(**settable_kwargs)

        unsettable_kwargs = {
            key: val for key, val in self.ax_kwargs.items() if key not in ax_set_keys
        }
        self.handle_unsettable_kwargs(unsettable_kwargs)

        # replace original kwargs
        self.ax_kwargs.update(original_kwargs)

        if self.is_3d:
            n_vals = self.data[self.animation_key].size
            current_index = np.argmax(
                self.data[self.animation_key].values
                == self.state.context[self.animation_key]
            )
            frame_view = self.calc_frame_view(current_index, n_vals)
            self.ax.view_init(**frame_view)

    def create_axes_config(self):
        """Method that fills ax_kwargs with defaults for things not already specified.

        Currently only sets the axis limits.
        """
        # Set the axis limits if they are not specified
        self.handle_axes_limits_and_ticks(equal=self.ax_kwargs.get("equal_lims"))

    def handle_axes_limits_and_ticks(self, data=None, equal=False):
        """Handles the setting of axis limits and ticks based on the provided data.

        Args:
            data (optional):
                The data used to calculate axis limits if they are not explicitly set.
            equal (bool, optional):
                If True, ensures that all axes have the same limits.

        This method identifies which axes need their limits set, checks if any
        axis limits are not explicitly provided, and then calculates and sets
        the necessary limits.
        """
        # Define the necessary axes, starting with "x" and "y"
        necessary_axes = ["x", "y"]

        # If a "z" axis is present, add it to the list of necessary axes
        if self.axis_keys.get("z") is not None:
            necessary_axes.append("z")

        # Initialize a list to track which axes have their limits explicitly set
        using_set = [False] * len(necessary_axes)

        # Check if limits are set for each necessary axis
        for i, ax_letter in enumerate(necessary_axes):
            if self.ax_kwargs.get(f"{ax_letter}lim") is not None:
                using_set[i] = True

        # Create a list that indicates which axes do not have their limits set
        using_unset = [not val for val in using_set]

        # If any axes do not have their limits set
        if any(using_unset):
            # Check if the 'lims' key already exists in self.ax_kwargs
            lims_exist = self.ax_kwargs.get("lims") is not None

            # If 'lims' doesn't exist, create an empty dictionary for it
            if not lims_exist:
                self.ax_kwargs["lims"] = {}

        # Create array of axes that need to have the limits calculated
        necessary_axes = np.array(necessary_axes)[using_unset]

        # Call the helper function to calculate and set limits for the necessary axes
        self.ax_lims_helper(necessary_axes, data=data, equal=equal)

    def ax_lims_helper(self, necessary_axes, data=None, equal=False):
        """Helper function to calculate and set axis limits.

        Args:
            necessary_axes (list):
                List of axes (e.g., ['x', 'y', 'z']) that require limits to be set.
            data (optional):
                Data used to calculate axis limits if they are not explicitly set.
            equal (bool, optional):
                If True, ensures that all axes have the same limits.

        This function calculates the appropriate axis limits based on the data
        and whether the limits should be equal across all axes. The calculated
        limits are then stored in `self.ax_kwargs["lims"]`.
        """
        # Use the provided data if available; otherwise, default to the Plot's data
        if data is None:
            data = self.data

        # If 'equal' is True, set all axes to have the same limits
        if equal:
            max_val = 0  # Initialize a variable to track the maximum absolute value

            # Iterate over each axis that needs limits set
            for ax_letter in necessary_axes:
                # Check if limits for this axis are already stored in self.ax_kwargs
                if ax_lims := self.ax_kwargs["lims"].get(ax_letter):
                    # If limits exist and contain two values, calculate exact
                    # limits and ticks
                    if len(ax_lims) == 2:
                        ax_lims = util.calculate_axis_limits_and_ticks(
                            *ax_lims, exact=True
                        )
                else:
                    # If limits do not exist, calculate the max and min values
                    # from the data
                    ax_data = data[self.axis_keys.get(ax_letter)].values

                    # Update max_val with the maximum value
                    max_val = max(max_val, np.abs(ax_data.max()))

                    # Update max_val with the minimum value
                    max_val = max(max_val, np.abs(ax_data.min()))

                    # Calculate limits based on the max absolute value
                    ax_lims = util.calculate_axis_limits_and_ticks(-max_val, max_val)

            # Store the calculated limits for each axis in self.ax_kwargs
            for ax_letter in necessary_axes:
                self.ax_kwargs["lims"][ax_letter] = ax_lims
        else:
            # If 'equal' is False, calculate and set limits individually for each axis
            for ax_letter in necessary_axes:
                # Calculate limits based on the minimum and maximum values from the data
                axlims = util.calculate_axis_limits_and_ticks(
                    data[self.axis_keys.get(ax_letter)].values.min(),
                    data[self.axis_keys.get(ax_letter)].values.max(),
                )

                # Store the calculated limits in self.ax_kwargs
                self.ax_kwargs["lims"][ax_letter] = axlims

    def handle_unsettable_kwargs(self, kwargs):
        """Handles kwargs that are not settable with ax.set.

        Args:
            kwargs (dict):
                Dictionary containing information about the unsettable kwargs.
        """
        if "lims" in kwargs:
            # 'lims' is expected to be a dictionary with each axis's limits
            # Limits are specified as a tuple: (val0, valf, dval, offset)

            # Iterate over each axis key in given_axis_keys
            for ax_letter in self.given_axis_keys:
                # Check if the limits for the current axis are not already set
                if self.ax_kwargs.get(f"{ax_letter}lim") is None:
                    # Retrieve the limits for the current axis from kwargs
                    axlims = kwargs["lims"][ax_letter]

                    # Use minor only for 2D plots
                    use_minor = not self.is_3d

                    # Set the limits and ticks
                    self.set_lims_and_ticks(*axlims, ax_letter, use_minor=use_minor)

    def set_lims_and_ticks(self, val0, valf, dval, offset, ax_letter, use_minor=True):
        """Sets the limits and ticks for a specific axis.

        Args:
            val0 (float):
                The initial value for the axis.
            valf (float):
                The final value for the axis.
            dval (float):
                The interval between ticks on the axis.
            offset (float):
                The offset to apply to the axis limits.
            ax_letter (str):
                The axis identifier (e.g., 'x', 'y', 'z').
            use_minor (bool, optional):
                If True, sets minor ticks on the axis.

        This function sets the limits and tick marks on the specified axis based on
        the provided values. It optionally adds minor ticks if `use_minor` is True.
        """
        # Get the function to set the axis limits using the specified axis letter
        set_lim = getattr(self.ax, f"set_{ax_letter}lim")

        # Get the function to set the axis ticks using the specified axis letter
        set_ticks = getattr(self.ax, f"set_{ax_letter}ticks")

        # Set the limits for the axis, adjusting for the provided offset
        set_lim([val0 - offset, valf + offset])

        # Set the major ticks on the axis using the specified interval (dval)
        set_ticks(np.arange(val0, valf + dval / 4, dval))

        # If minor ticks are to be used, set them at halfway points between the
        # major ticks
        if use_minor:
            set_ticks(np.arange(val0 + dval / 2, valf + dval / 4, dval), minor=True)

    def update_alt_text(self, text):
        """Updates the alt text for the plot."""
        self._alt_text = text
