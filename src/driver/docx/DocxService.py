from abc import abstractmethod, ABC
from typing import List

from beans.TableBean import TableBean


class DocxService(ABC):
    """文档服务器"""

    @abstractmethod
    def insert_tables(self, module_name: str, table_beans: List[TableBean]) -> None:
        """插入多张表格"""

        pass

    @abstractmethod
    def insert_table(self, table_bean: TableBean):
        """插入一张表格"""
        pass

    @abstractmethod
    def insert_title(self):
        """插入一张"""
        pass

    @abstractmethod
    def save(self):
        pass
