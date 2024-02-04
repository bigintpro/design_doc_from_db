from typing import Optional, List, Dict

from oracledb import Connection, Cursor

from beans.ColumnBean import ColumnBean
from beans.TableBean import TableBean
from db.oracle.connection.OracleConntionService import OracleConnectionService


class OracleDbService:
    """数据库服务"""

    _default_db_name = "CYY"

    """获取全部的表"""
    _get_table = r"SELECT TABLE_NAME FROM all_tables WHERE owner = '{}'"

    """获取全部表对象"""
    _get_table_beans = r"SELECT table_name, comments FROM all_tab_comments WHERE owner = '{0}' and table_name in (SELECT TABLE_NAME FROM all_tables WHERE owner ='{1}' )"

    """获取字段注释"""
    _get_column_comments = r"SELECT COLUMN_NAME,COMMENTS FROM all_col_comments WHERE owner = '{0}' and table_name='{1}'"

    """获取某个表的全部列定义"""
    _get_column_beans = r"""SELECT a.COLUMN_ID,a.COLUMN_NAME,a.DATA_TYPE,a.DATA_LENGTH,a.DATA_PRECISION,
    a.DATA_SCALE,a.NULLABLE,a.DATA_DEFAULT,b.COMMENTS 
    FROM all_tab_columns a left join all_col_comments b 
    on (a.OWNER = b.OWNER and a.TABLE_NAME = b.TABLE_NAME and a.COLUMN_NAME = b.COLUMN_NAME) 
    WHERE a.owner = '{0}' and a.table_name = '{1}' order by a.COLUMN_ID asc"""

    def get_all_table_names(self, db_name: Optional[str]) -> List[str]:
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

        db_name = db_name if db_name is not None else self._default_db_name
        sql = self._get_table_beans.format(db_name, db_name)

        con: Connection = OracleConnectionService.get_connection()
        cursor: Cursor = con.cursor()

        for row in cursor.execute(sql):
            table_name = row[0]
            table_comment = row[1]
            table_columns = self.get_table_column_beans(db_name,table_name)

            bean = TableBean(table_name,table_comment,table_columns)
            result.append(bean)

        return result

    def get_table_column_beans(self,db_name: str,table_name: str)->List[ColumnBean]:
        """获取一张表的列信息"""
        sql = None
        result: List[ColumnBean] = []
        if db_name is None:
            return result
        else:
            sql = self._get_column_beans.format(db_name, table_name)

        con: Connection = OracleConnectionService.get_connection()
        cursor: Cursor = con.cursor()
        for row in cursor.execute(sql):
            primary_column = True if row[1] == "ID" else False

            bean = ColumnBean(column_id=row[0],column_name=row[1],data_type=row[2],
                              data_length=row[3],data_precision=row[4],data_scale=row[5],
                              nullable=row[6],data_default=row[7],comment=row[8],primary_column=primary_column)

            result.append(bean)
        return result




    def get_table_columns_comment(self,db_name: str,table_name: str) -> Dict[str,str]:
        """获取一个表的全部注释字段 返回列名->字段注释名"""

        result = {}
        sql = self._get_column_comments.format(db_name,table_name)
        con: Connection = OracleConnectionService.get_connection()
        cursor: Cursor = con.cursor()

        for row in cursor.execute(sql):
            result[row[0]] = row[1]

        return result












