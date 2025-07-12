import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.common.config_loader import load_config

def get_meeting_dates(config: dict) -> list[dict]:
    """
    Reads all records from the race calendar Google Sheet.
    Returns a list of dictionaries, each with keys: "race_date", "race_venue", "num_of_races".
    """
    # Determine credentials path, with fallback to ~/gcp/credentials/hk_racing_sa_key.json
    CREDENTIALS_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not CREDENTIALS_PATH:
        # Fallback path based on your GCP folder
        fallback = os.path.expanduser("~/gcp/credentials/hk_racing_sa_key.json")
        CREDENTIALS_PATH = fallback

    # Diagnostic check for credentials path
    print(f"DEBUG: Using credentials path: {CREDENTIALS_PATH}", file=sys.stderr)
    if not os.path.isfile(CREDENTIALS_PATH):
        sys.exit(f"ERROR: Credentials file not found at: {CREDENTIALS_PATH}")

    # Define the scope and authorize
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive.readonly",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)

    # Open the sheet and retrieve all records as list of dicts
    sheet = client.open_by_key(config["google_sheets"]["spreadsheet_id"]).worksheet(config["google_sheets"]["sheet_name"])
    records = sheet.get_all_records()  # List of dicts: keys are column headers
    return records


if __name__ == "__main__":
    config = load_config()
    print(get_meeting_dates(config))
