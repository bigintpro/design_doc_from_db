from abc import abstractmethod
from typing import List

from beans.TableBean import TableBean


class XlsxService:
    """excel服务"""



    @abstractmethod
    def insert_tables(self, table_beans: List[TableBean]) -> None:
        """插入多张表格"""

        pass

    @abstractmethod
    def insert_table(self,table_bean: TableBean)->None:
        """在excel中插入表格"""
        pass