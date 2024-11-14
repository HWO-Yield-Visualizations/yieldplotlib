"""Node for handling input json files."""

from pathlib import Path

from yieldplotlib.core.file_nodes import JSONFile


class EXOSIMSInputFile(JSONFile):
    """Node for handling the EXOSIMS input JSON files."""

    def __init__(self, file_path: Path):
        """Initialize the EXOSIMSInputFile node with the file path."""
        super().__init__(file_path)
        self.is_input = True

    def get(self, key: str):
        """Custom logic for the input JSON files."""
        # TODO: Implement custom logic for these files.
        return super().get(key)
