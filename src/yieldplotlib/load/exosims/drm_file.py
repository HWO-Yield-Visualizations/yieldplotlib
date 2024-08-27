"""Custom node for handling DRM pickle files."""

from yieldplotlib.core.file_nodes import PickleFile


class DRMFile(PickleFile):
    """Node for handling DRM-specific pickle files."""

    def get(self, key: str):
        """Custom logic for DRM files."""
        # TODO: Implement custom logic for DRM files.
        return super().get(key)
