from typing import Tuple, Dict

import yaml


class Config:
    """
    配置类


    """
    """配置数据"""
    data: Dict[str, Tuple] = None

    @staticmethod
    def get_by_key(key: str) -> Tuple:
        """通过key获取配置数据"""
        if Config.data is not None:
            return Config.data[key]
        else:
            with open('/Users/joy/Documents/workshop/python_projects/projects/documentExport/application.yaml',
                      'r') as file:
                data = yaml.safe_load(file)
                # 打印加载的数据
                Config.data = data if data is not None else {}
                return Config.data[key]
