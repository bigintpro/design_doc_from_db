from typing import List

from beans.TableBean import TableBean
from driver.xlsx.XlsxService import XlsxService


class XlsxServiceImpl(XlsxService):

    def insert_tables(self, table_beans: List[TableBean]) -> None:
        pass

    def insert_table(self, table_bean: TableBean) -> None:
        """在excel中插入表格"""

        pass
