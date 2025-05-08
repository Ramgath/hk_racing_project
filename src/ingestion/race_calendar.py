import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_ID = "1gX48NYjjLT0WJrzbHEltbCUTVU1d9VHv3NsSRVJWLSs"
SHEET_NAME = "calendar"


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


def get_meeting_dates() -> list[dict]:
    """
    Reads all records from the race calendar Google Sheet.
    Returns a list of dictionaries, each with keys: "race_date", "race_venue", "num_of_races".
    """
    # Define the scope and authorize
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive.readonly",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)

    # Open the sheet and retrieve all records as list of dicts
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    records = sheet.get_all_records()  # List of dicts: keys are column headers
    return records


if __name__ == "__main__":
    print(get_meeting_dates())
