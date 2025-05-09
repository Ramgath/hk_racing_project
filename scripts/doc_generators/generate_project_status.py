#!/usr/bin/env python3
import os
import sys
import re

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from tabulate import tabulate

# —– CONFIG —–
SPREADSHEET_ID = "1OPvpEvMCOxZeuoOOBOnvacRMXI-tXivczfYezKowtcY"
SHEET_NAME = "status"
MD_PATH = "/Users/yastherramgath/hk_racing_project/docs/project-status.md"
CRED_ENV = "GOOGLE_APPLICATION_CREDENTIALS"
START_MARKER = "<!-- TASKS_START -->"
END_MARKER = "<!-- TASKS_END -->"
# —– END CONFIG —–


def get_sheets_service():
    creds_file = os.environ.get(CRED_ENV) or os.path.expanduser(
        "~/gcp/credentials/hk_racing_sa_key.json"
    )
    if not os.path.isfile(creds_file):
        sys.exit(f"ERROR: Credentials file not found at {creds_file}")

    scope = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    return build("sheets", "v4", credentials=creds)


def fetch_grid_data(service):
    """Fetches the entire sheet, including formatting."""
    resp = (
        service.spreadsheets()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            ranges=[SHEET_NAME],
            includeGridData=True,
            fields="sheets(data(rowData(values(formattedValue,effectiveFormat/textFormat))))",
        )
        .execute()
    )
    return resp["sheets"][0]["data"][0].get("rowData", [])


def fmt_cell(cell):
    text = cell.get("formattedValue", "")
    tf = cell.get("effectiveFormat", {}).get("textFormat", {})
    bold = tf.get("bold", False)
    italic = tf.get("italic", False)

    # wrap in markdown
    if bold and italic:
        return f"***{text}***"
    if bold:
        return f"**{text}**"
    if italic:
        return f"*{text}*"
    return text


def make_md_table(row_data):
    """Convert the raw rowData (with formatting) into a Markdown table."""
    if not row_data:
        return "_No tasks found in sheet._"

    # header row
    header_cells = row_data[0].get("values", [])
    headers = [fmt_cell(c) for c in header_cells]

    # data rows
    rows = []
    for row in row_data[1:]:
        cells = row.get("values", [])
        rows.append([fmt_cell(c) for c in cells])

    return tabulate(rows, headers=headers, tablefmt="github")


def replace_block(md_content, table_md):
    new_block = (
        "## Detailed Tasks & Issues:\n"
        f"{START_MARKER}\n"
        f"{table_md}\n"
        f"{END_MARKER}"
    )
    pattern = rf"## Detailed Tasks & Issues:[\s\S]*?{END_MARKER}"
    return re.sub(pattern, new_block, md_content)


def main():
    service = get_sheets_service()
    grid = fetch_grid_data(service)
    table_md = make_md_table(grid)

    # load MD
    with open(MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # swap in the new table
    updated = replace_block(content, table_md)

    # overwrite
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print(
        f"✅ Updated table (with formatting) under 'Detailed Tasks & Issues' in {MD_PATH}"
    )


if __name__ == "__main__":
    main()
