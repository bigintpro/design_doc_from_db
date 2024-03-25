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
    def insert_title(self, title_name: str, level: int):
        """插入level等级标题 h1 对应 1 h2 对应 2"""
        pass

    @abstractmethod
    def save(self):
        pass
