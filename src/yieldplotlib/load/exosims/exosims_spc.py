"""Node for handling SPC-specific pickle files."""

from yieldplotlib.core.file_nodes import PickleFile


class SPCFile(PickleFile):
    """Node for handling SPC-specific pickle files."""

    def _get(self, key: str):
        """Custom logic for SPC files."""
        # TODO: Implement custom logic for SPC files.
        return super().get(key)
