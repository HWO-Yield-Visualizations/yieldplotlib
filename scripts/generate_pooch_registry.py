"""Generate pooch registry with MD5 hashes for data files."""

import hashlib
import json
from pathlib import Path


def calculate_md5(file_path: Path) -> str:
    """Calculate MD5 hash of a file."""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def generate_registry(data_dir: Path) -> dict:
    """Generate registry dictionary for pooch."""
    registry = {}

    # Look for zip files in data directory
    for file_path in data_dir.glob("*.zip"):
        if file_path.is_file():
            # Calculate MD5 hash
            md5_hash = calculate_md5(file_path)
            # Add to registry
            registry[file_path.name] = f"md5:{md5_hash}"

    return registry


def main():
    """Main function to generate registry."""
    # Get the data directory
    data_dir = Path(__file__).parent.parent / "data"

    # Generate registry
    registry = generate_registry(data_dir)

    # Print registry as formatted JSON
    print(json.dumps(registry, indent=2))


if __name__ == "__main__":
    main()
