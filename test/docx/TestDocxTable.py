from docx import Document
from docx.enum.style import WD_BUILTIN_STYLE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.table import Table, _Cell

if __name__ == '__main__':
    document = Document()
    table: Table = document.add_table(3,4)
    cell:_Cell = table.cell(0,0)
    # cell.add_paragraph("abc")
    paragraph = cell.paragraphs[0]
    # paragraph.style(WD_BUILTIN_STYLE.TABLE_COLORFUL_GRID)
    # paragraph.("Colorful Grid.")
    paragraph.add_run("acb")
    paragraph.alignment=WD_ALIGN_PARAGRAPH.CENTER

    run = paragraph.runs[0]
    run.font.size = Pt(8)

    document.save("abc.docx")
