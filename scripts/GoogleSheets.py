import gspread

class googleSheets():
    def __init__(self, url, spreadsheet_id, credentials_path) -> None:
        gc = gspread.service_account(credentials_path)
        spreadsheet = gc.open_by_url(url)

        self.ws = spreadsheet.get_worksheet_by_id(spreadsheet_id)

        self.column_count = self.ws.column_count
        pass
    def get_all_values(self):
        return self.ws.get_all_values()
    def getColumn(self, column):
        cells = self.get_all_values()
        columnList = []
        for i in range(3, len(cells)):
            columnList.append(cells[i][column-1])
        return columnList
    
    def cell(self, row, col):
        return self.ws.cell(row, col)
