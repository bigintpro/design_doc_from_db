from openpyxl.styles import Side, Border
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

if __name__ == '__main__':
    wb: Workbook = Workbook()
    sheet: Worksheet = wb.active
    sheet.title = "testMergeCell"
    cell_range = 'A1:L5'  # 例如，选择A1到D5的单元格范围
    cells = sheet[cell_range]
    sheet["A1"].value = "abc"

    border_style = Side(border_style='thick', color='000000')  # 设置边框样式为粗线且颜色为黑色

    border = Border(top=border_style, right=border_style, bottom=border_style, left=border_style)  # 设置四个边框的样式

    for row in cells:
        for cell in row:
            cell.border = border  # 应用边框样式到每个单元格
            cell.value = "aa"

    sheet.merge_cells('A1:L1')
    sheet.append(["序号", "字段名称", "字段注释", "数据类型", "字段长度", "小数位数", "值域", "默认值", "约束", "键",
                  "非空性", "备注"])
    sheet.append(["1", "ID", "ID", "VARCHAR2", "32", "", "", "", "主键约束", "PK", "TRUE", ""])

    # ws.append(["1", "", ""])
    # ws.append(["1", "2", "3"])
    # ws.append(["1", "2", "3"])

    wb.save("testMergeCell.xlsx")
