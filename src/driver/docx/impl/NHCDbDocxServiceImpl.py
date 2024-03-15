from typing import List

from docx.document import Document
from docx.shared import RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

from beans.TableBean import TableBean
from driver.docx.DocxService import DocxService
from driver.docx.cell.CellService import CellService
from driver.docx.template.NHCDbTemplate import NHCDbTemplate


class NHCDbDocxServiceImpl(DocxService):
    """新和成文档服务"""

    table_template: NHCDbTemplate = None

    docx: Document = None

    def __init__(self, docx: Document):
        self.docx = docx

    def insert_tables(self, module_name: str, table_beans: List[TableBean]) -> None:
        """插入多张表格"""
        if table_beans is None or len(table_beans) == 0:
            return
        # 添加模块名称
        header: Paragraph = self.docx.add_heading(text=module_name, level=1)
        header.runs[0].font.color.rgb = RGBColor(0, 0, 0)
        for table_bean in table_beans:
            self.insert_table(table_bean)

    def insert_table(self, table_bean: TableBean) -> None:
        """插入一张表格"""

        if table_bean is None:
            return
        # 添加表标题
        header: Paragraph = self.docx.add_heading(
            text="{0}({1})".format(table_bean.table_comment, table_bean.table_name), level=2)
        header.runs[0].font.color.rgb = RGBColor(0, 0, 0)

        # 添加表格第一行title
        table: Table = self.docx.add_table(rows=0, cols=10)
        cells = table.add_row().cells
        for index, tile in enumerate(NHCDbTemplate.second_title):
            cells[index].text = tile

        # 设置标题的背景颜色
        CellService.set_background_color_for_cells("#D2D2D2", cells)
        CellService.set_font_size_for_cells(8, cells)

        # 添加具体数据
        for column_bean in table_bean.table_columns:
            cells = table.add_row().cells
            cells[0].text = str(column_bean.column_id)
            cells[1].text = column_bean.comment if column_bean.comment is not None else ""
            cells[2].text = column_bean.column_name
            cells[3].text = column_bean.data_type
            cells[4].text = str(column_bean.data_length) if column_bean.data_length is not None else ""
            cells[5].text = str(column_bean.data_precision) if column_bean.data_precision is not None else ""
            cells[6].text = "TRUE" if column_bean.nullable == "Y" else "FALSE"
            cells[7].text = "TRUE" if column_bean.primary_column else "FALSE"
            cells[8].text = "FALSE"
            cells[9].text = ""
            CellService.set_font_size_for_cells(6, cells)

        # 设置表格的宽度和高度
        CellService.set_height_for_row(0.5, table.rows)
        CellService.set_width_for_column(0.1, [table.columns[0]])
        CellService.set_width_for_column(0.4, [table.columns[1]])
        CellService.set_width_for_column(0.4, [table.columns[2]])
        CellService.set_width_for_column(0.3, [table.columns[3]])
        CellService.set_width_for_column(0.2, [table.columns[4]])
        CellService.set_width_for_column(0.2, [table.columns[5]])
        CellService.set_width_for_column(0.2, [table.columns[6]])
        CellService.set_width_for_column(0.2, [table.columns[7]])
        CellService.set_width_for_column(0.3, [table.columns[8]])
        CellService.set_width_for_column(1, [table.columns[9]])

        # 设置

    def insert_title(self):
        pass

    def save(self):
        self.docx.save("/Users/joy/Desktop/test.docx")
        pass
