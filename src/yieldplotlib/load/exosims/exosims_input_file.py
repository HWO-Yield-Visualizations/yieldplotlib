"""Node for handling input json files."""

from pathlib import Path

from yieldplotlib.core.file_nodes import JSONFile

# Define which nested keys correspond to the modes, systems, and instruments for parsing.
# Could also be added as a flag in the key_map
INSTRUMENT_KEYS = ['qe', 'cic', 'read_noise', 'dark_current', 'pixel_scale', 'texp', 'optics_throughput']
INSTRUMENT_KEYS += ['sc_' + k for k in INSTRUMENT_KEYS]

MODE_KEYS = ['obs_lam', 'snr']
MODE_KEYS += ['sc_' + k for k in MODE_KEYS]

SYSTEM_KEYS = ['coron_lam', 'iwa', 'owa', 'bw', 'optics']


class EXOSIMSInputFile(JSONFile):
    """Node for handling the EXOSIMS input JSON files."""

    def __init__(self, file_path: Path):
        """Initialize the EXOSIMSInputFile node with the file path."""
        super().__init__(file_path)
        self.is_input = True

    def get(self, key: str):
        """Custom logic for the input JSON files."""
        # TODO: Implement custom logic for these files.
        # Define which instruments, systems and modes are used. Will not return values for unused
        # but defined modes/instruments/systems.
        used_modes = super().get('modes')
        used_instruments = [m["instName"] for m in used_modes]
        used_systems = [m["systName"] for m in used_modes]

        values = super().get(key)
        # If only a single value, return.
        if not isinstance(values, dict):
            return values

        else:
            if key in INSTRUMENT_KEYS or MODE_KEYS:
                if key.startswith('sc'):  # indicates spectroscopy parameter.
                    for k in values.copy().keys():
                        if 'spectro' not in k or k not in used_instruments:
                            del values[k]
                else:
                    for k in values.copy().keys():
                        if 'spectro' in k or k not in used_instruments:
                            del values[k]

            if key in SYSTEM_KEYS:
                for k in values.copy().keys():
                    if k not in used_systems:
                        del values[k]

        return values
