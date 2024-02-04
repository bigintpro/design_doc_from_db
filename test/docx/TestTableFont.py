from docx import Document
from docx.shared import Pt
from docx.table import _Cell

if __name__ == '__main__':

    # 创建一个新文档
    document = Document()

    # 添加一个表格，1行1列
    table = document.add_table(rows=10, cols=3)

    # 获取表格中的单元格
    cell: _Cell = table.cell(0, 0)

    # 设置单元格中文本的字体大小
    paragraph = cell.paragraphs[0]
    paragraph.add_run(text="123")
    run = paragraph.runs[0]
    font = run.font
    font.size = Pt(6)  # 设置字体大小为12磅

    # 保存文档
    document.save('tableFont1.docx')