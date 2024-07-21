"""Base class for all plots."""

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

    def render(self):
        """Method to render the plot."""
        self.adjust_settings()

    def draw_plot(self, plot_kwargs=None):
        """Method to draw the plot.

        Args:
            plot_kwargs (dict, optional): Dictionary of kwargs to pass to the plot

        """
        self.generic_plot(self.data, plot_kwargs=plot_kwargs)

    def generic_plot(self, plot_method, data=None, plot_kwargs=None):
        """Generic plot method that can be used by any plot type.

        Args:
            plot_method (str):
                TODO
            data (tuple, optional):
                TODO
            plot_kwargs (dict, optional):
                TODO
        """
        # Plot method is a string like "plot" or "scatter"
        plot_method = getattr(self.ax, plot_method)

        if data is None:
            data = self.get_plot_data()

        if plot_kwargs is None:
            plot_kwargs = self.plot_kwargs
        plot_method(*data, **plot_kwargs)

        self.ax.set(**self.ax_kwargs)

    def get_plot_data(self, context=None):
        """Method to get the data required to plot."""
        sel = self.state.context_sel(context)
        data = self.data.sel(**sel)

        # Allows for 2 and 3 dimensional data with the same call
        separated_data = [
            data[self.axis_keys[axis_key]].values for axis_key in self.given_axis_keys
        ]
        return separated_data

    def adjust_settings(self):
        """Method to adjust the settings of the plot."""
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

        Currently sets the axis limits.
        """
        # Set the axis limits if they are not specified
        self.handle_axes_limits_and_ticks(equal=self.ax_kwargs.get("equal_lims"))

    def handle_axes_limits_and_ticks(self, data=None, equal=False):
        """TODO."""
        necessary_axes = ["x", "y"]
        if self.axis_keys.get("z") is not None:
            necessary_axes.append("z")

        using_set = [False] * len(necessary_axes)
        for i, ax_letter in enumerate(necessary_axes):
            if self.ax_kwargs.get(f"{ax_letter}lim") is not None:
                using_set[i] = True
        using_unset = [not val for val in using_set]
        if any(using_unset):
            lims_exist = self.ax_kwargs.get("lims") is not None
            if not lims_exist:
                self.ax_kwargs["lims"] = {}
        necessary_axes = np.array(necessary_axes)[using_unset]
        self.ax_lims_helper(necessary_axes, data=data, equal=equal)

    def ax_lims_helper(self, necessary_axes, data=None, equal=False):
        """TODO."""
        if data is None:
            data = self.data
        if equal:
            max_val = 0
            for ax_letter in necessary_axes:
                if ax_lims := self.ax_kwargs["lims"].get(ax_letter):
                    if len(ax_lims) == 2:
                        ax_lims = util.calculate_axis_limits_and_ticks(
                            *ax_lims, exact=True
                        )
                else:
                    ax_data = data[self.axis_keys.get(ax_letter)].values
                    max_val = max(max_val, np.abs(ax_data.max()))
                    max_val = max(max_val, np.abs(ax_data.min()))
                    ax_lims = util.calculate_axis_limits_and_ticks(-max_val, max_val)
            for ax_letter in necessary_axes:
                self.ax_kwargs["lims"][ax_letter] = ax_lims
        else:
            for ax_letter in necessary_axes:
                axlims = util.calculate_axis_limits_and_ticks(
                    data[self.axis_keys.get(ax_letter)].values.min(),
                    data[self.axis_keys.get(ax_letter)].values.max(),
                )

                self.ax_kwargs["lims"][ax_letter] = axlims

    def handle_unsettable_kwargs(self, kwargs):
        """TODO."""
        if "lims" in kwargs:
            # lims is a tuple of (val0, valf, dval, offset)
            # Check if the lims are already set
            for ax_letter in self.given_axis_keys:
                if self.ax_kwargs.get(f"{ax_letter}lim") is None:
                    axlims = kwargs["lims"][ax_letter]
                    use_minor = not self.is_3d
                    self.set_lims_and_ticks(*axlims, ax_letter, use_minor=use_minor)

    def set_lims_and_ticks(self, val0, valf, dval, offset, ax_letter, use_minor=True):
        """TODO."""
        # for ax_letter in self.given_axis_keys:
        set_lim = getattr(self.ax, f"set_{ax_letter}lim")
        set_ticks = getattr(self.ax, f"set_{ax_letter}ticks")
        set_lim([val0 - offset, valf + offset])
        set_ticks(np.arange(val0, valf + dval / 4, dval))
        if use_minor:
            set_ticks(np.arange(val0 + dval / 2, valf + dval / 4, dval), minor=True)
