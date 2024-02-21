from typing import List, Dict

from beans.TableBean import TableBean
from core.Config import Config


class NHCModuleClassifyService:
    """"分类服务"""
    pass
    # PMSV -> 模块名称
    map: Dict[str, str] = None

    @classmethod
    def module_classify(cls, table_beans: List[TableBean]) -> Dict[str, List[TableBean]]:
        """根据配置的分类"""
        cls.init_map()
        result = dict()
        if table_beans is None:
            return result
        result["其他"] = []
        for table_bean in table_beans:
            module_name = table_bean.table_name[1:5].upper()
            if module_name in cls.map:
                module_cn_name = cls.map[module_name]
                if module_cn_name not in result:
                    result[module_cn_name] = []
                    result[module_cn_name].append(table_bean)
                else:
                    result[module_cn_name].append(table_bean)
            else:
                result["其他"].append(table_bean)

        return result

    @classmethod
    def init_map(cls):
        if cls.map is not None:
            return

        cls.map = dict()
        config = Config.get_by_key("config")
        if config is not None and "xhc" in config:
            for key, value in config["xhc"].items():
                cls.map[key] = value["moduleName"]
