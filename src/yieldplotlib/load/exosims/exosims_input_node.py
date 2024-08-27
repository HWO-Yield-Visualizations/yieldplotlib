"""Node for handling input json files."""

from yieldplotlib.core.json_node import JSONNode


class EXOSIMSInputNode(JSONNode):
    """Node for handling the EXOSIMS input JSON files."""

    def get(self, key: str):
        """Custom logic for the input JSON files."""
        # TODO: Implement custom logic for these files.
        return super().get(key)
