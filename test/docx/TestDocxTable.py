from docx import Document
from docx.table import Table, _Cell

if __name__ == '__main__':
    document = Document()
    table: Table = document.add_table(3,4)
    cell:_Cell = table.cell(0,0)
    cell.add_paragraph("abc")

    document.save("abc.docx")
