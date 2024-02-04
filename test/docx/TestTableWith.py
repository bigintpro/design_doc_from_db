from docx import Document
from docx.enum.style import WD_BUILTIN_STYLE
from docx.enum.table import WD_ROW_HEIGHT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Cm
from docx.table import Table, _Cell

if __name__ == '__main__':
    document = Document()
    table: Table = document.add_table(3, 4)
    # 遍历表格的每一行，设置行高
    for row in table.rows:
        row.height_rule = WD_ROW_HEIGHT.EXACTLY
        row.height = Cm(0.5)  # 设置行高为1.5厘米

    for column in table.columns:
        column.width = Cm(1)

    document.save("tableWidth.docx")