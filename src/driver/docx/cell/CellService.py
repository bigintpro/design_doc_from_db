from typing import Tuple, List

from docx.enum.table import WD_ROW_HEIGHT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from docx.table import _Rows, _Columns


class CellService:
    """单元格服务"""

    @classmethod
    def set_background_color_for_cells(cls, color: str, cells: Tuple) -> None:
        """设置单元格的背景颜色"""
        if cells is None:
            return
        for cell in cells:
            CellService.set_background_color_for_cell(cell,color)

    @classmethod
    def set_background_color_for_cell(cls, cell, color):
        """设置单元格背景颜色"""
        tcPr = cell._tc.get_or_add_tcPr()
        tcVAlign = OxmlElement("w:shd")
        tcVAlign.set(qn("w:fill"), color)
        tcPr.append(tcVAlign)


    @classmethod
    def set_height_for_row(cls, height, rows: List[_Rows]):
        """设置行高"""
        if rows is None:
            return

        for row in rows:
            row.height_rule = WD_ROW_HEIGHT.EXACTLY
            row.height = Cm(height)  # 设置行高为1.5厘米

    @classmethod
    def set_width_for_column(cls,width, columns: List[_Columns]):
        """设置列宽"""
        if columns is None:
            return

        for column in columns:
            column.width = Cm(width)

    @classmethod
    def set_font_size_for_cells(cls, font_size: int, cells: Tuple):
        """设置字体大小"""
        if cells is None:
            return

        for cell in cells:
            if cell.paragraphs is None or len(cell.paragraphs) == 0:
                continue
            paragraph = cell.paragraphs[0]

            if paragraph.runs is None or len(paragraph.runs) == 0:
                continue

            run = paragraph.runs[0]
            font = run.font
            font.size = Pt(font_size)  # 设置字体大小为磅