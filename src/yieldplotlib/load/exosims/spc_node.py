"""Node for handling SPC-specific pickle files."""

from yieldplotlib.core.pickle_node import PickleNode


class SPCNode(PickleNode):
    """Node for handling SPC-specific pickle files."""

    def get(self, key: str):
        """Custom logic for SPC files."""
        # TODO: Implement custom logic for SPC files.
        return super().get(key)
