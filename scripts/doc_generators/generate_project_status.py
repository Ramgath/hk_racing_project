#!/usr/bin/env python3
import os
import sys
import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tabulate import tabulate

# —– CONFIG —–
SPREADSHEET_ID = "1OPvpEvMCOxZeuoOOBOnvacRMXI-tXivczfYezKowtcY"
SHEET_NAME = "status"
MD_PATH = "/Users/yastherramgath/hk_racing_project/docs/project-status.md"
CRED_ENV = "GOOGLE_APPLICATION_CREDENTIALS"
START_MARKER = "<!-- TASKS_START -->"
END_MARKER = "<!-- TASKS_END -->"
# —– END CONFIG —–


def get_credentials():
    creds_file = os.environ.get(CRED_ENV) or os.path.expanduser(
        "~/gcp/credentials/hk_racing_sa_key.json"
    )
    if not os.path.isfile(creds_file):
        sys.exit(f"ERROR: Credentials file not found at {creds_file}")
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive.readonly",
    ]
    return ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)


def fetch_records(creds):
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    return sheet.get_all_records()


def make_md_table(records):
    if not records:
        return "_No tasks found in sheet._"
    headers = list(records[0].keys())
    rows = [list(r.values()) for r in records]
    return tabulate(rows, headers=headers, tablefmt="github")


def replace_block(original, table_md):
    # Build the replacement block
    new_block = (
        "## Detailed Tasks & Issues:\n"
        f"{START_MARKER}\n"
        f"{table_md}\n"
        f"{END_MARKER}"
    )
    # Regex to match from header through END_MARKER
    pattern = rf"## Detailed Tasks & Issues:[\s\S]*?{END_MARKER}"
    return re.sub(pattern, new_block, original)


def main():
    creds = get_credentials()
    records = fetch_records(creds)
    table = make_md_table(records)

    # Read existing MD
    with open(MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old table block
    updated = replace_block(content, table)

    # Write back
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print(
        f"✅ Updated {len(records)} rows under 'Detailed Tasks & Issues' in:\n   {MD_PATH}"
    )


if __name__ == "__main__":
    main()
