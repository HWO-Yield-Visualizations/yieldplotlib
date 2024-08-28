"""Represents a directory containing multiple nodes (files or subdirectories)."""

from pathlib import Path

from tqdm import tqdm

from yieldplotlib.core.file_nodes import CSVFile, JSONFile, PickleFile
from yieldplotlib.core.node import Node
from yieldplotlib.logger import logger


class DirectoryNode(Node):
    """Represents a directory containing multiple nodes (files or subdirectories)."""

    def __init__(self, directory_path: Path):
        """Initialize the directory node with a list of children."""
        super().__init__(directory_path)

        # Aliasing file_path to directory_path for consistency
        self.directory_path = self.file_path
        self.directory_name = self.directory_path.name
        self._children = []
        self.load()

    def load(self):
        """Recursively scan directories and load all child nodes."""
        paths = list(self.directory_path.iterdir())
        with tqdm(
            total=len(paths),
            desc=f"Loading {self.__class__.__name__} {self.directory_path.name}",
            unit="item",
        ) as pbar:
            for path in paths:
                if path.is_dir():
                    # directory_node = DirectoryNode(path)
                    # self.add(directory_node)
                    self.add(self._create_directory_node(path))
                else:
                    self.add(self._create_file_node(path))
                pbar.update(1)

    def add(self, node: Node):
        """Add a child node to the directory."""
        if node is not None:
            self._children.append(node)

    def get(self, key: str):
        """Recursively search for data associated with the given key."""
        for child in self._children:
            result = child.get(key)
            if result is not None:
                return result
        return None

    def display_tree(self, level=0, max_children=5, prefix=""):
        """Recursively display the tree structure.

        Args:
            level (int):
                The current level of the tree.
            max_children (int):
                The maximum number of children to display.
            prefix (str):
                The prefix to display at the current level.
        """
        repr_str = f"{prefix}{self.__repr__()}\n"

        # Adjust prefix for children
        child_prefix = prefix.replace("├── ", "│   ").replace("└── ", "    ")

        for i, child in enumerate(self._children):
            # Adjust connector based on whether this is the last child
            last_before_cutoff = i == max_children - 1
            last_child = i == len(self._children) - 1

            # Determine the connector based on the child's position
            if last_before_cutoff and not last_child:
                connector = "├── "
            elif last_child:
                connector = "└── "
            else:
                connector = "├── "

            if i < max_children:
                repr_str += child.display_tree(
                    level + 1, max_children, child_prefix + connector
                )
            else:
                repr_str += (
                    f"{child_prefix}└── ... and"
                    f" {len(self._children) - max_children} more\n"
                )
                break

        return repr_str

    def _create_directory_node(self, path: Path) -> Node:
        """Create a directory node for the given path."""
        return self.create_base_directory(path)

    def _create_file_node(self, path: Path) -> Node:
        """Create a file node for the given path."""
        return self.create_base_file(path)

    def create_base_file(self, path: Path):
        """Create a base file node for the given path."""
        if path.suffix == ".csv":
            return CSVFile(path)
        elif path.suffix == ".json":
            return JSONFile(path)
        elif path.suffix == ".pkl":
            return PickleFile(path)
        else:
            logger.warning(f"Unknown file type: {path.suffix}")
            return None

    def create_base_directory(self, path: Path):
        """Create a directory node for the given path."""
        return DirectoryNode(path)
