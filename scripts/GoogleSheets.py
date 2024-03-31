import gspread
from gspread.utils import finditem
from google.auth import exceptions
from google.oauth2.service_account import Credentials


class googleSheets(gspread.Worksheet):
    def __init__(self, url, spreadsheet_id, credentials_path) -> None:
        # Set the path to your credentials JSON file
        credentials_path = '../credentials.json'
        try:
            # Try to get credentials from the file
            credentials = Credentials.from_service_account_file(credentials_path, scopes=[
                                                                'https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
        except exceptions.DefaultCredentialsError:
            print("Credentials not found or invalid. Make sure to provide a valid path to your credentials JSON file.")
            exit()

        # Authorize the client
        gc = gspread.authorize(credentials)

        # Open the Google Sheet by title
        spreadsheet = gc.open_by_url(url)
        # Select a specific worksheet
        worksheet_id_int = int(spreadsheet_id)

        item = finditem(
            lambda x: x["properties"]["sheetId"] == worksheet_id_int,
            spreadsheet.fetch_sheet_metadata()["sheets"],
        )

        super().__init__(spreadsheet, item["properties"])
        pass

    def getColumn(self, column):
        cells = super().get_all_values()
        columnList = []
        for i in range(3, len(cells)):
            columnList.append(cells[i][column-1])
        return columnList
