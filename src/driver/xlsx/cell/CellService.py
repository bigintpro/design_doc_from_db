from typing import Tuple

from openpyxl.styles import Alignment


class CellService:
    """单元格服务"""





    @classmethod
    def set_alignment_for_cell(cls,horizontal: str,vertical: str,cells: Tuple):
        """设置单元格对其模式"""
        if cells is None or len(cells) == 0:
            return

        alignment = Alignment(horizontal=horizontal, vertical=vertical)

        for cell in cells:
            cell.alignment = alignment




