
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

if __name__ == '__main__':
    # 创建一个新的文档
    document = Document()

    # 添加一个表格
    table = document.add_table(rows=3, cols=3)

    # 定义一个函数来设置单元格的背景颜色
    def set_cell_background_color(cell, color):
        tcPr = cell._tc.get_or_add_tcPr()
        tcVAlign = OxmlElement("w:shd")
        tcVAlign.set(qn("w:fill"), color)
        tcPr.append(tcVAlign)

    # 设置不同单元格的背景颜色
    set_cell_background_color(table.cell(0, 0), "#99badd")  # unc
    set_cell_background_color(table.cell(0, 1), "#CC0000")  # nc state
    set_cell_background_color(table.cell(0, 2), "#001A57")  # duke

    # 保存文档
    document.save("tableColor.docx")