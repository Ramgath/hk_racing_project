import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.race_calendar import get_meeting_dates

class TestRaceCalendar(unittest.TestCase):

    @patch('src.ingestion.race_calendar.os.path.isfile')
    @patch('src.ingestion.race_calendar.gspread.authorize')
    @patch('src.ingestion.race_calendar.ServiceAccountCredentials.from_json_keyfile_name')
    def test_get_meeting_dates(self, mock_from_json, mock_authorize, mock_isfile):
        # Mock the config
        config = {
            "google_sheets": {
                "spreadsheet_id": "test_spreadsheet_id",
                "sheet_name": "test_sheet_name"
            }
        }

        # Mock the gspread client and sheet
        mock_isfile.return_value = True
        mock_client = MagicMock()
        mock_spreadsheet = MagicMock()
        mock_worksheet = MagicMock()
        mock_authorize.return_value = mock_client
        mock_client.open_by_key.return_value = mock_spreadsheet
        mock_spreadsheet.worksheet.return_value = mock_worksheet
        mock_worksheet.get_all_records.return_value = [
            {"race_date": "2023-01-01", "race_venue": "Sha Tin", "num_of_races": 10},
            {"race_date": "2023-01-04", "race_venue": "Happy Valley", "num_of_races": 8}
        ]

        # Call the function
        result = get_meeting_dates(config)

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["race_date"], "2023-01-01")
        mock_client.open_by_key.assert_called_with("test_spreadsheet_id")
        mock_spreadsheet.worksheet.assert_called_with("test_sheet_name")

if __name__ == '__main__':
    unittest.main()
