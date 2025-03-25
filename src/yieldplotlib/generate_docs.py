"""Generate parameter table documentation from Google Sheets data.

This script downloads a specified Google Sheet and generates a markdown table
from its contents, focusing on parameter names and descriptions. The table
is generated without a header so it can be included in other documentation files.

Usage Examples:
1. Generate from a local CSV file:
   ```
   python generate_docs.py --csv sheet.csv --output ../../docs/user/parameters_table.md
   ```

2. Download from Google Sheets using temporary credentials:
   ```
   python generate_docs.py --sheets SHEET_ID \
       --output ../../docs/user/parameters_table.md \
       --temp
   ```
"""

import argparse
import base64
import csv
import io
import os
import sys
from typing import Optional

import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate YPL parameters table from Google Sheets"
    )

    # Create a mutually exclusive group for input source
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--csv", help="Path to local CSV file")
    group.add_argument("--sheets", help="Google Sheet ID to download from")

    parser.add_argument("--output", required=True, help="Output markdown file path")
    parser.add_argument(
        "--temp",
        action="store_true",
        help="Use temporary credentials from environment variable",
    )

    return parser.parse_args()


def download_from_google_sheets(
    sheet_id: str, credentials_json_path: Optional[str] = None
) -> str:
    """Download a CSV file from Google Sheets.

    Args:
        sheet_id:
          The ID of the Google Sheet to download.
        credentials_json_path:
          Path to a service account credentials JSON file. If None,
          credentials will be loaded from GOOGLE_CREDENTIALS_B64
          environment variable.

    Returns:
        CSV content as a string.
    """
    # Set up credentials
    if credentials_json_path:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_json_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
        )
    else:
        # Get credentials from environment variable
        try:
            credentials_b64 = os.environ.get("GOOGLE_CREDENTIALS_B64")
            if not credentials_b64:
                raise ValueError("GOOGLE_CREDENTIALS_B64 environment variable not set")

            credentials_json = base64.b64decode(credentials_b64).decode("utf-8")
            credentials = service_account.Credentials.from_service_account_info(
                eval(credentials_json),
                scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
            )
        except Exception as e:
            print(f"Error loading credentials: {e}")
            sys.exit(1)

    # Build the Sheets API client
    service = build("sheets", "v4", credentials=credentials)

    # Call the Sheets API to get all values
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=sheet_id,
            range="A:Z",  # Get all columns
        )
        .execute()
    )

    values = result.get("values", [])
    if not values:
        print("No data found in the Google Sheet")
        sys.exit(1)

    # Convert to CSV
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(values)

    return output.getvalue()


def read_csv_file(file_path: str) -> str:
    """Read a CSV file from disk.

    Args:
        file_path:
          Path to the CSV file to read.

    Returns:
        CSV content as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)


def generate_markdown_table(csv_content: str) -> str:
    """Generate a markdown table from CSV content without a header.

    Args:
        csv_content:
          CSV content as a string.

    Returns:
        Markdown table as a string.
    """
    # Parse CSV into DataFrame
    df = pd.read_csv(io.StringIO(csv_content))

    # Filter to only include rows with non-empty yieldplotlib name
    # (excluding rows without a parameter name)
    df = df[df["yieldplotlib name"].notna() & (df["yieldplotlib name"] != "")]

    # Sort alphabetically by parameter name
    df = df.sort_values("yieldplotlib name")

    # Select only the relevant columns and rename them for the documentation
    params_df = df[["yieldplotlib name", "description"]].rename(
        columns={"yieldplotlib name": "Parameter", "description": "Description"}
    )

    # Return just the table without a header
    return params_df.to_markdown(index=False)


def main():
    """Main function to generate docs."""
    args = parse_args()

    # Get CSV content either from local file or Google Sheets
    try:
        if args.csv:
            # Read from local CSV file
            csv_content = read_csv_file(args.csv)
            print(f"Read CSV data from {args.csv}")
        elif args.sheets:
            # Download from Google Sheets
            if args.temp:
                csv_content = download_from_google_sheets(args.sheets)
            else:
                csv_content = download_from_google_sheets(
                    args.sheets, "credentials.json"
                )
            print(f"Downloaded CSV data from Google Sheet {args.sheets}")
    except Exception as e:
        print(f"Error obtaining CSV data: {e}")
        sys.exit(1)

    # Generate markdown
    try:
        markdown = generate_markdown_table(csv_content)
    except Exception as e:
        print(f"Error generating markdown: {e}")
        sys.exit(1)

    # Write to file
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(args.output), exist_ok=True)

        with open(args.output, "w") as f:
            f.write(markdown)
        print(f"Successfully wrote parameter table to {args.output}")
    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
