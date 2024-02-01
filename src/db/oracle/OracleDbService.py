from typing import Tuple, Optional, List

from oracledb import Connection, Cursor

from beans.TableBean import TableBean
from db.oracle.OracleConntionService import OracleConnectionService


class OracleDbService:
    """数据库服务"""

    _default_db_name = "CYY"

    """获取全部的表"""
    _get_table = r"SELECT TABLE_NAME FROM all_tables WHERE owner = '{}'"

    """获取全部表对象"""
    _get_table_beans = r"SELECT table_name, comments FROM all_tab_comments WHERE owner = '{0}' and table_name in (SELECT TABLE_NAME FROM all_tables WHERE owner ='{1}' )"

    """获取某个表的全部列定义"""
    _get_column = "SELECT * FROM all_tab_columns WHERE table_name = '{0}'"

    def get_all_table_names(self, db_name: Optional[str]) -> List:
        """
        获取全部表名,返回一个列表数组
        """
        sql = None
        result = []
        if db_name is None:
            sql = self._get_table.format(self._default_db_name)
        else:
            sql = self._get_table.format(db_name)

        con: Connection = OracleConnectionService.get_connection()
        cursor: Cursor = con.cursor()

        for row in cursor.execute(sql):
            result.append(row[0])

        return result

    def get_all_table_beans(self,db_name: Optional[str]) ->List[TableBean]:
        """
        获取全部表名,返回一个列表数组
        """
        sql = None
        result: List[TableBean] = []
        if db_name is None:
            sql = self._get_table_beans.format(self._default_db_name,self._default_db_name)
        else:
            sql = self._get_table_beans.format(db_name,db_name)

        con: Connection = OracleConnectionService.get_connection()
        cursor: Cursor = con.cursor()

        for row in cursor.execute(sql):
            bean = TableBean(row[0],row[1])
            result.append(bean)

        return result

