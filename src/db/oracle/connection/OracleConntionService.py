import oracledb
from oracledb import Connection
from core.Config import Config



class OracleConnectionService:
    """
    oracle数据库连接服务


    """
    """连接对象"""
    _connection: Connection = None


    @classmethod
    def get_connection(cls)->Connection:
        """获取一个连接"""
        if cls._connection != None:
            return cls._connection
        else:
            config_data = Config.get_by_key("db")
            cls._connection = oracledb.connect(**config_data)
            return cls._connection


