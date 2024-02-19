from abc import abstractmethod
from typing import List

from beans.TableBean import TableBean


class XlsxService:
    """excel服务"""

    @abstractmethod
    def insert_tables(self, sheet_name: str, table_beans: List[TableBean]) -> None:
        """插入多张表格"""

        pass

    @abstractmethod
    def insert_table(self, sheet_name: str, row_offset: int, table_bean: TableBean) -> None:
        """在excel中插入表格"""
        pass
