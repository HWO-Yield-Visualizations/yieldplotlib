"""Node for handling AYO's CSV files."""

import numpy as np
import pandas as pd
from astropy import units as u

from yieldplotlib.core import CSVFile
from yieldplotlib.key_map import KEY_MAP

OVERRIDE_KEYS = {
    "blind_comp_det": "_get_blind_comp",
}


class AYOCSVFile(CSVFile):
    """Node for handling reduced AYO CSV files."""

    def transform_star_name(self, data):
        """Add a prefix to the star_name data."""
        return np.array(["HIP " + str(int(name)) for name in data])

    def transform_WDS_sep(self, data):
        """Convert the WDS separation to floats."""
        return np.array(data, dtype=float)

    def transform_WDS_dmag(self, data):
        """Convert the WDS dMag to floats."""
        return np.array(data, dtype=float)

    def find_unit_for_ayo_key(self, ayo_key):
        """Find the unit for a given AYO key.

        Searches through the KEY_MAP to find a mapping where the provided AYO key
        matches the 'name' field for the specified module. If found, returns the
        corresponding unit.

        Args:
            ayo_key (str):
                The AYO key (e.g., 'Angdiam (mas)').

        Returns:
            str or None:
                The unit string if found, None otherwise.
        """
        module_name = self.__class__.__name__
        for yieldplotlib_key, module_data in KEY_MAP.items():
            # Check if this entry has data for the specified module
            if module_name in module_data:
                module_info = module_data[module_name]
                # Check if the 'name' field matches the AYO key
                if module_info.get("name") == ayo_key:
                    return module_info.get("unit", "")

        return None

    def get_unit(self, key):
        """Get the associated unit for a given key.

        This method handles both yieldplotlib keys and AYO keys:
        1. First tries a direct lookup in KEY_MAP (assuming key is a yieldplotlib key)
        2. If not found, tries to find the corresponding yieldplotlib key by looking up
           the AYO key in KEY_MAP

        Args:
            key (str):
                The key to look up the unit for (can be either a yieldplotlib key
                or an AYO key).

        Returns:
            astropy.units.Unit or None:
                The astropy Unit object if found, None otherwise.
        """
        # First try direct lookup (for yieldplotlib keys)
        if key in KEY_MAP and "AYOCSVFile" in KEY_MAP[key]:
            unit = KEY_MAP[key]["AYOCSVFile"].get("unit", "")
        else:
            # If not found, try to find the corresponding yieldplotlib key
            # by looking up the AYO key
            unit = self.find_unit_for_ayo_key(key)

        if unit:
            astropy_unit = u.Unit(unit)
            return astropy_unit

        return None

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        if key in OVERRIDE_KEYS:
            return getattr(self, OVERRIDE_KEYS[key])()
        unit = self.get_unit(key)

        if key in self.data.columns:
            if unit:
                return self.data[key].values * unit
            else:
                return self.data[key].values
        return None

    def _get_blind_comp(self):
        """Get the blind completeness data from first visits.

        Returns:
            np.ndarray:
                A structured array with completeness, star names, and integration times
                for all first visits.
        """
        # Filter data to only include first visits
        first_visits = self.data[self.data["Visit #"] == 1]

        # Extract the required data
        completeness = first_visits["exoEarth candidate yield"].values.astype(float)
        hip_ids = first_visits["HIP"].values
        integration_times = first_visits["Exp Time (days)"].values.astype(float)

        # Create star names with HIP prefix
        star_names = np.array([f"HIP {int(hip)}" for hip in hip_ids])

        # Create a structured array with the data
        result = pd.DataFrame(
            {
                "completeness": completeness,
                "star_name": star_names,
                "integration_time": integration_times,
            },
        )

        return result
