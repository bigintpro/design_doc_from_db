from typing import Tuple, Dict, List

import yaml

from beans.ModuleTree import ModuleTree


class Config:
    """
    配置类


    """
    """配置数据"""
    data: Dict[str, Tuple] = None
    module_true_list: List[ModuleTree] = None

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

    @staticmethod
    def get_module_tree() -> List[ModuleTree]:
        if Config.module_true_list is not None:
            return Config.module_true_list
        else:
            with open('/Users/joy/Documents/workshop/python_projects/projects/documentExport/tree.json',
                      'r') as file:
                json_str = file.read()
                data = ModuleTree.schema().loads(json_str, many=True)

                # data = yaml.safe_load(file)
                # 打印加载的数据
                Config.module_true_list = data if data is not None else []
                return Config.module_true_list

    @staticmethod
    def get_module_tree_by_key(key: str) -> ModuleTree:
        if Config.module_true_list is None:
            Config.get_module_tree()

            if Config.module_true_list is not None:
                for value in Config.module_true_list:
                    if value.modulePrefix == key:
                        return value
        else:
            for value in Config.module_true_list:
                if value.modulePrefix == key:
                    return value
