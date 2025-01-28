"""Node for handling input json files."""

from pathlib import Path

from astropy import units as u

from yieldplotlib.core.file_nodes import FitsFile, JSONFile
from yieldplotlib.key_map import KEY_MAP
from yieldplotlib.logger import logger

# Define which nested keys correspond to the modes, systems, and
# instruments for parsing.
# Could also be added as a flag in the key_map
INSTRUMENT_KEYS = [
    "qe",
    "cic",
    "read_noise",
    "dark_current",
    "pixel_scale",
    "texp",
    "optics_throughput",
]
INSTRUMENT_KEYS += ["sc_" + k for k in INSTRUMENT_KEYS]

MODE_KEYS = ["obs_lam", "snr"]
MODE_KEYS += ["sc_" + k for k in MODE_KEYS]

SYSTEM_KEYS = ["coron_lam", "iwa", "owa", "bw", "optics", "core_thruput"]


class EXOSIMSInputFile(JSONFile):
    """Node for handling the EXOSIMS input JSON files."""

    def __init__(self, file_path: Path):
        """Initialize the EXOSIMSInputFile node with the file path."""
        super().__init__(file_path)
        self.is_input = True

    def get_unit(self, key: str):
        """Get the associated unit for a given key."""
        entry = KEY_MAP[key]
        unit = entry["EXOSIMSInputFile"]["unit"]

        if unit:
            astropy_unit = u.Unit(unit)
            return astropy_unit

        return None

    def get(self, key: str):
        """Custom logic for the input JSON files."""
        # TODO: Implement custom logic for these files.
        # Define which instruments, systems and modes are used. Will not
        # return values for unused but defined modes/instruments/systems.
        used_modes = super().get("modes")
        used_instruments = [m["instName"] for m in used_modes]
        used_systems = [m["systName"] for m in used_modes]

        values = super().get(key)
        unit = self.get_unit(key) if values else None

        # If only a single value, return.
        if not isinstance(values, dict):
            if unit:
                return values * unit
            else:
                return values

        else:
            if key in INSTRUMENT_KEYS or key in MODE_KEYS:
                if key.startswith("sc"):  # indicates spectroscopy parameter.
                    for k in values.copy().keys():
                        if "spectro" not in k or k not in used_instruments:
                            del values[k]
                else:
                    for k in values.copy().keys():
                        if "spectro" in k or k not in used_instruments:
                            del values[k]

            if key in SYSTEM_KEYS:
                for k in values.copy().keys():
                    if k not in used_systems:
                        del values[k]

        for k, v in values.items():
            if unit:
                values[k] = v * unit
            if v.endswith(".fits"):
                try:
                    values[k] = FitsFile(Path(v))
                except FileNotFoundError:
                    logger.info(
                        f"File path {v} does not exist on the local machine. "
                        f"Could not create FitsFile object"
                    )

        return values
