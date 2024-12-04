"""File to generate key_map.py when given the google sheet as a csv.

It should be called from the command line like this:
```
python generate_key_map.py input_csv
```
and it will write the key_map.py file to the current directory.
"""

import argparse
import csv
import sys
from collections import OrderedDict


def parse_csv(input_csv):
    """Parses the input CSV and constructs the KEY_MAP dictionary.

    Args:
        input_csv (str): Path to the input CSV file.

    Returns:
        OrderedDict: The constructed KEY_MAP with prioritized ordering.
    """
    key_map = OrderedDict()

    # Lists to hold categorized rows
    both_libs = []
    only_ayo = []
    only_exo = []

    with open(input_csv, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row_num, row in enumerate(
            reader, start=2
        ):  # Start at 2 to account for header
            yield_name = row.get("yieldplotlib name", "").strip()
            exo_name = row.get("EXOSIMS name", "").strip()
            exo_file = row.get("EXOSIMS file", "").strip()
            exo_class = row.get("EXOSIMS Class", "").strip()
            ayo_name = row.get("AYO name", "").strip()
            ayo_file = row.get("AYO file", "").strip()
            ayo_class = row.get("AYO Class", "").strip()
            comment = row.get("Comment", "").strip()

            # New columns for transformation
            # e.g., "index"
            exo_transform_type = row.get("EXOSIMS transform type", "").strip().lower()
            # e.g., "2"
            exo_transform_value = row.get("EXOSIMS transform value", "").strip()
            # e.g., "sum"
            ayo_transform_type = row.get("AYO transform type", "").strip().lower()
            # e.g., "1,2"
            ayo_transform_value = row.get("AYO transform value", "").strip()

            # Determine the yieldplotlib key
            if yield_name:
                key = yield_name
            else:
                if exo_name and not ayo_name:
                    key = exo_name
                elif ayo_name and not exo_name:
                    key = ayo_name
                elif exo_name and ayo_name:
                    # Prefer EXOSIMS name as the key
                    key = exo_name
                else:
                    print(
                        (
                            f"Warning: Row {row_num} has no 'yieldplotlib name'"
                            " and no clear library names. Skipping."
                        )
                    )
                    continue  # Skip rows that don't meet criteria

            # Categorize the row based on available libraries
            has_exo = bool(exo_name and exo_file and exo_class)
            has_ayo = bool(ayo_name and ayo_file and ayo_class)

            row_entry = {
                "key": key,
                "EXOSIMS": {
                    "class": exo_class,
                    "file": exo_file,
                    "name": exo_name,
                    "transform": {
                        "type": exo_transform_type if exo_transform_type else "none",
                        "value": exo_transform_value if exo_transform_value else None,
                    },
                }
                if has_exo
                else None,
                "AYO": {
                    "class": ayo_class,
                    "file": ayo_file,
                    "name": ayo_name,
                    "transform": {
                        "type": ayo_transform_type if ayo_transform_type else "none",
                        "value": ayo_transform_value if ayo_transform_value else None,
                    },
                }
                if has_ayo
                else None,
                "comment": comment if comment else "",
            }

            if has_exo and has_ayo:
                both_libs.append(row_entry)
            elif has_ayo:
                only_ayo.append(row_entry)
            elif has_exo:
                only_exo.append(row_entry)
            else:
                # If neither library has complete info, skip the row
                print(
                    (
                        f"Warning: Row {row_num} does not have complete "
                        "information for either library. Skipping."
                    )
                )
                continue

    # Function to add entries to key_map with duplicate checking
    def add_to_key_map(entry, context):
        key = entry["key"]
        exo_entry = entry["EXOSIMS"]
        ayo_entry = entry["AYO"]
        comment = entry["comment"]

        # Initialize the entry
        map_entry = {}

        # Add EXOSIMS entry if present
        if exo_entry:
            exo_class = exo_entry["class"]
            map_entry[exo_class] = {
                "file": exo_entry["file"],
                "name": exo_entry["name"],
                "transform": {
                    "type": exo_entry["transform"]["type"],
                    "value": exo_entry["transform"]["value"],
                },
            }

        # Add AYO entry if present
        if ayo_entry:
            ayo_class = ayo_entry["class"]
            map_entry[ayo_class] = {
                "file": ayo_entry["file"],
                "name": ayo_entry["name"],
                "transform": {
                    "type": ayo_entry["transform"]["type"],
                    "value": ayo_entry["transform"]["value"],
                },
            }

        # Add comment
        map_entry["comment"] = comment

        if key in key_map:
            print(
                (
                    f"Warning: Duplicate key '{key}' found in {context}."
                    " Overwriting previous entry."
                )
            )

        key_map[key] = map_entry

    # Process entries in prioritized order
    # 1. Both EXOSIMS and AYO
    for entry in both_libs:
        add_to_key_map(entry, "Both Libraries")

    # 2. Only AYO
    for entry in only_ayo:
        add_to_key_map(entry, "AYO Only")

    # 3. Only EXOSIMS
    for entry in only_exo:
        add_to_key_map(entry, "EXOSIMS Only")

    return key_map


def write_key_map(key_map, output_py):
    """Writes the KEY_MAP dictionary to a Python file with a docstring.

    Args:
        key_map (OrderedDict):
            The KEY_MAP dictionary.
        output_py (str):
            Path to the output Python file.
    """
    docstring = '"""Key mapping for yieldplotlib library."""\n\n'
    with open(output_py, "w", encoding="utf-8") as f:
        f.write(docstring)
        f.write("KEY_MAP = {\n")
        for key, value in key_map.items():
            f.write(f'    "{key}": {{\n')
            # Add library-specific entries
            for lib_class in ["EXOSIMSCSVFile", "AYOCSVFile"]:
                if lib_class in value:
                    lib_entry = value[lib_class]
                    f.write(f'        "{lib_class}": {{\n')
                    f.write(f'            "file": "{lib_entry["file"]}",\n')
                    f.write(f'            "name": "{lib_entry["name"]}",\n')
                    # Handle transformation details
                    transform_type = lib_entry["transform"]["type"]
                    transform_value = lib_entry["transform"]["value"]
                    # For `None` values, represent them as `None` without quotes
                    if transform_value is None:
                        transform_value_repr = "None"
                    elif (
                        isinstance(transform_value, str)
                        and transform_value.lower() == "none"
                    ):
                        transform_value_repr = "None"
                    else:
                        # Determine if transform_value should be int, float, or string
                        try:
                            # Try to convert to integer
                            transform_value_int = int(transform_value)
                            transform_value_repr = str(transform_value_int)
                        except ValueError:
                            try:
                                # Try to convert to float
                                transform_value_float = float(transform_value)
                                transform_value_repr = str(transform_value_float)
                            except ValueError:
                                # Keep as string, ensure it's properly quoted
                                transform_value_repr = f'"{transform_value}"'

                    f.write('            "transform": {\n')
                    f.write(f'                "type": "{transform_type}",\n')
                    f.write(f'                "value": {transform_value_repr}\n')
                    f.write("            }\n")
                    f.write("        },\n")
            # Add comment
            comment = value.get("comment", "").replace('"', '\\"')
            f.write(f'        "comment": "{comment}"\n')
            f.write("    },\n")
        f.write("}\n")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate key_map.py from a CSV file for yieldplotlib."
    )
    parser.add_argument("input_csv", help="Path to the input CSV file.")
    parser.add_argument(
        "output_py",
        nargs="?",
        default="key_map.py",
        help="Path to the output key_map.py file (default: key_map.py).",
    )
    args = parser.parse_args()

    try:
        key_map = parse_csv(args.input_csv)
        write_key_map(key_map, args.output_py)
        print(f"Successfully wrote KEY_MAP to '{args.output_py}'.")
    except FileNotFoundError:
        print(f"Error: The file '{args.input_csv}' does not exist.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
