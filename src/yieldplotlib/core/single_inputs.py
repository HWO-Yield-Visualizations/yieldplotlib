"""The base `SingleInput` class.

`SingleInput` is a class designed to facilitate the reading, setting, and manipulation of
various types of yield inputs. It inherits from dict for direct access to
built-in dictionary functions such as get(), update(), etc.
"""


class SingleInput(dict):
    """Base class for all Inputs."""

    def __init__(self, *args, **kwargs):
        super(SingleInput, self).__init__(*args, **kwargs)

    def apply(self, key, func):
        """Apply a function to all values of a given key."""
        try:
            self[key] = func(self.get(key))
        except TypeError:
            raise TypeError(f'Could not apply function to {key}')

    def check_units(self, key, desired_unit):
        """Checks that all values of key have the appropriate desired unit."""
        try:
            for value in self.get(key):
                if value.unit != desired_unit:
                    raise AssertionError(f"Value {value} for {key} does not have desired "
                                         f"unit {desired_unit}")
        except AttributeError:
            raise AttributeError(f'{key} does not have a value of type astropy.units.Quantity')








