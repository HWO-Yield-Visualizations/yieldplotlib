"""Node for handling input json files."""

from yieldplotlib.core.file_nodes import JSONFile


class EXOSIMSInputFile(JSONFile):
    """Node for handling the EXOSIMS input JSON files."""

    def get(self, key: str):
        """Custom logic for the input JSON files."""
        # TODO: Implement custom logic for these files.
        return super().get(key)
