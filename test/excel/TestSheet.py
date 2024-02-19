from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

if __name__ == '__main__':
    wb: Workbook = Workbook()
    ws: Worksheet = wb.active
    ws.title = "SA"

    ws.append(["1", "2", "3"])
    ws.append(["1", "2", "3"])
    ws.append(["1", "2", "3"])

    wb.save("testSheet.xlsx")
