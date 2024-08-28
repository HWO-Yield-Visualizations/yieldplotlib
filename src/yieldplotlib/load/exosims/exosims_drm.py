"""Custom node for handling DRM pickle files."""

import astropy.units as u
import numpy as np

from yieldplotlib.core.file_nodes import PickleFile
from yieldplotlib.logger import logger


class DRMFile(PickleFile):
    """Node for handling DRM-specific pickle files."""

    def load(self):
        """Load the DRM file as a list of dictionaries."""
        pass

    def _get(self, key: str):
        """Custom logic for DRM files."""
        # TODO: Implement custom logic for DRM files.
        return None

        # DRM files are a list of dictionaries.
        # We want to return a list of values for the given key.
        drm_dict_keys = [
            "star_ind",
            "star_name",
            "arrival_time",
            "OB_nb",
            "ObsNum",
            "plan_inds",
            "det_time",
            "det_status",
            "det_SNR",
            "det_fZ",
            "det_params",
            "det_mode",
            "det_comp",
        ]
        if key in drm_dict_keys:
            vals = []
            for obs in self.data:
                try:
                    val = obs[key]
                    if isinstance(val, u.Quantity):
                        vals.append(val.value)
                    else:
                        vals.append(val)
                except KeyError:
                    logger.warning(f"Key {key} not found in DRM file.")
                    continue
            return np.array(vals)
        else:
            return None
