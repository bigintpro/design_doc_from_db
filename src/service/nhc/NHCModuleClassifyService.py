from typing import List, Dict

from beans.ModuleTree import ModuleTree
from beans.ModuleTreeData import ModuleTreeData
from beans.TableBean import TableBean
from core.Config import Config


class NHCModuleClassifyService:
    """"分类服务"""
    pass
    # PMSV -> 模块名称
    map: Dict[str, str] = None

    # # 模块树 一级模块PM -> 模块树
    # module_tree_map: Dict[str, ModuleTree] = None

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
    def module_tree_classify(cls, table_beans: List[TableBean]) -> List[ModuleTreeData]:
        """分类模块树"""
        result: List[ModuleTreeData] = list()

        subOther = ModuleTreeData(moduleName="other", modulePrefix="", children=[], data=[])
        other = ModuleTreeData(moduleName="其他", modulePrefix="other", children=[subOther], data=[])
        result.append(other)

        if table_beans is None:
            return result
        for table_bean in table_beans:
            # PM
            firstModuleName = table_bean.table_name[1:3].upper()
            moduleTree = Config.get_module_tree_by_key(firstModuleName)
            if moduleTree is not None:
                firstModuleTreeData = cls._find_module_tree_data_by_key(result, moduleTree.modulePrefix)
                if firstModuleTreeData is None:
                    firstModuleTreeData = ModuleTreeData(moduleName=moduleTree.moduleName,
                                                         modulePrefix=moduleTree.modulePrefix, children=[], data=[])
                    result.append(firstModuleTreeData)

                # SS
                secondModuleName = table_bean.table_name[3:5].upper()

                secondModuleTree = cls._find_sub_module_tree(moduleTree.children, secondModuleName)
                if secondModuleTree is None:
                    subOther.data.append(table_bean)
                else:

                    secondModuleTreeData = cls._find_sub_module_tree_data(firstModuleTreeData.children,
                                                                          firstModuleName + secondModuleName)
                    if secondModuleTreeData is None:
                        secondModuleTreeData = ModuleTreeData(moduleName=secondModuleTree.moduleName,
                                                              modulePrefix=moduleTree.modulePrefix + secondModuleTree.modulePrefix,
                                                              data=[table_bean], children=[])
                        firstModuleTreeData.children.append(secondModuleTreeData)
                    else:
                        secondModuleTreeData.data.append(table_bean)
            else:
                ## 处理没有分类数据的情况
                subOther.data.append(table_bean)

        return result

    @classmethod
    def _find_module_tree_data_by_key(cls, list: List[ModuleTreeData], key: str):
        if list is None:
            return
        for value in list:
            if value.modulePrefix == key:
                return value

    @classmethod
    def _find_sub_module_tree(cls, children: List[ModuleTree], key: str) -> ModuleTree:
        if children is not None:
            for child in children:
                if child.modulePrefix == key:
                    return child

    @classmethod
    def _find_sub_module_tree_data(cls, children: List[ModuleTreeData], key: str) -> ModuleTreeData:
        if children is not None:
            for child in children:
                if child.modulePrefix == key:
                    return child

    @classmethod
    def init_map(cls):
        if cls.map is not None:
            return

        cls.map = dict()
        moduleTreeList = Config.get_module_tree()
        if moduleTreeList is not None:
            for value in moduleTreeList:
                for sub_value in value.children:
                    cls.map[value.modulePrefix + sub_value.modulePrefix] = sub_value.moduleName
