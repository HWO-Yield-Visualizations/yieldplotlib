r"""Generate key_map.py from CSV data or directly from Google Sheets.

This script creates a key_map.py file that maps parameters between different exoplanet
simulation libraries (EXOSIMS and AYO). It can either use a local CSV file or directly
download from a Google Sheet.

Usage Examples:
1. Generate from a local CSV file:
   ```
   python generate_key_map.py --csv input_data.csv
   ```

2. Download from Google Sheets using a service account credentials file:
   ```
   python generate_key_map.py --sheets SHEET_ID --credentials path/to/credentials.json
   ```

3. Download from Google Sheets using Base64-encoded credentials from environment:
   ```
   # First set the environment variable:
   export GOOGLE_CREDENTIALS_B64=$(cat service-account.json | base64 | tr -d '\n')

   # Then run:
   python generate_key_map.py --sheets SHEET_ID
   ```

4. Use a temporary file for the downloaded CSV (cleaned up afterward):
   ```
   python generate_key_map.py --sheets SHEET_ID --temp
   ```

Output:
------
The script creates a key_map.py file in the current directory with a KEY_MAP
dictionary that maps parameter names to their locations and transformations
in the EXOSIMS and AYO libraries.
"""

import argparse
import base64
import csv
import json
import os
import sys
import tempfile
from collections import OrderedDict

import pandas as pd


def download_from_google_sheets(sheet_id, output_path, credentials_json_path=None):
    """Download data from Google Sheets and save as CSV.

    This function authenticates with Google Sheets API using service account credentials
    and downloads the specified sheet as a CSV file.

    Args:
        sheet_id:
            The ID of the Google Sheet to download. This is the string from the URL:
            https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit

        output_path:
            Path where the CSV file should be saved.

        credentials_json_path:
            Optional path to a service account credentials JSON file.
            If not provided, will use GOOGLE_CREDENTIALS_B64 environment variable,
            which should contain the Base64-encoded JSON credentials.

    Returns:
        None. The sheet data is saved to the output_path as a CSV file.

    Raises:
        SystemExit: If credentials cannot be loaded or sheet cannot be accessed.
    """
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        print(
            (
                "Error: Google API libraries not installed. "
                "Run: pip install google-auth google-auth-oauthlib"
                " google-api-python-client"
            )
        )
        sys.exit(1)

    credentials = None

    # First check for credentials file path
    if credentials_json_path:
        try:
            with open(credentials_json_path, "r") as f:
                credentials_info = json.load(f)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_info,
                scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
            )
            print(f"Using credentials from file: {credentials_json_path}")
        except Exception as e:
            print(f"Error loading credentials from {credentials_json_path}: {e}")
            sys.exit(1)
    else:
        # Try using Base64-encoded credentials from environment variable
        credentials_b64 = os.environ.get("GOOGLE_CREDENTIALS_B64")
        if not credentials_b64:
            print(
                (
                    "Error: No credentials provided. Either set GOOGLE_CREDENTIALS_B64"
                    " or provide --credentials"
                )
            )
            sys.exit(1)

        try:
            # Decode Base64 string to JSON
            credentials_json = base64.b64decode(credentials_b64).decode("utf-8")
            credentials_info = json.loads(credentials_json)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_info,
                scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
            )
            print("Using Base64-encoded credentials from environment variable")
        except Exception as e:
            print(f"Error decoding Base64 credentials: {e}")
            sys.exit(1)

    print(f"Downloading sheet {sheet_id}...")

    service = build("sheets", "v4", credentials=credentials)
    sheets = service.spreadsheets()

    # Get the spreadsheet
    try:
        sheet = sheets.values().get(spreadsheetId=sheet_id, range="Sheet1").execute()
        # Get the values
        values = sheet.get("values", [])
        if not values:
            print("Error: No data found in the Google Sheet")
            sys.exit(1)

        # Convert to DataFrame
        df = pd.DataFrame(values[1:], columns=values[0])

        # Save to CSV
        df.to_csv(output_path, index=False)
        print(f"Sheet downloaded and saved to {output_path}")
    except Exception as e:
        print(f"Error downloading sheet: {e}")
        sys.exit(1)


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
            exo_unit = row.get("EXOSIMS unit", "").strip()
            ayo_unit = row.get("AYO unit", "").strip()
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
                    "unit": exo_unit,
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
                    "unit": ayo_unit,
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
                "unit": exo_entry["unit"],
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
                "unit": ayo_entry["unit"],
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
            for lib_class in [
                "EXOSIMSCSVFile",
                "AYOCSVFile",
                "EXOSIMSInputFile",
                "AYOInputFile",
            ]:
                if lib_class in value:
                    lib_entry = value[lib_class]
                    f.write(f'        "{lib_class}": {{\n')
                    f.write(f'            "file": "{lib_entry["file"]}",\n')
                    f.write(f'            "name": "{lib_entry["name"]}",\n')
                    f.write(f'            "unit": "{lib_entry["unit"]}",\n')
                    # elif lib_class.startswith("AYO"):
                    #     f.write(f'            "unit": "{lib_entry["unit"]}",\n')
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
    """Process command line arguments and run the appropriate functions.

    This function parses command line arguments, downloads from Google Sheets if
    requested, processes the CSV file, and generates the key_map.py output file.

    Command-line arguments:
    ----------------------
    --csv: Path to a local CSV file to process
    --sheets: Google Sheet ID to download and process
    --credentials: Path to Google service account credentials JSON file (optional)
    --temp: Use a temporary file for the downloaded CSV (deleted after processing)

    Environment variables:
    --------------------
    GOOGLE_CREDENTIALS_B64: Base64-encoded Google service account JSON (required if
                            using --sheets without --credentials)
    """
    parser = argparse.ArgumentParser(description="Generate key_map.py from data")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--csv", help="Path to CSV file")
    group.add_argument("--sheets", help="Google Sheet ID to download from")

    # Add optional arguments
    parser.add_argument(
        "--credentials", help="Path to Google service account credentials JSON file"
    )
    parser.add_argument(
        "--temp", action="store_true", help=("Download to a temporary file")
    )

    args = parser.parse_args()

    csv_path = None
    temp_file = None

    try:
        if args.sheets:
            # Download from Google Sheets to a temporary or specific file
            if args.temp:
                # Create a temporary file that will be automatically cleaned up
                temp_file = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
                csv_path = temp_file.name
                temp_file.close()  # Close it so we can write to it
            else:
                # Use a fixed name in the current directory
                csv_path = "_sheet_download.csv"

            download_from_google_sheets(args.sheets, csv_path, args.credentials)
        elif args.csv:
            # Use the provided CSV file
            csv_path = args.csv

        # Parse the CSV and write the key_map.py file
        if csv_path:
            key_map = parse_csv(csv_path)
            write_key_map(key_map, "key_map.py")
            print(f"Successfully generated key_map.py from {csv_path}")

    finally:
        # Clean up the temporary file if we created one
        if temp_file and os.path.exists(csv_path):
            os.unlink(csv_path)
            print(f"Temporary file {csv_path} removed")


if __name__ == "__main__":
    main()
