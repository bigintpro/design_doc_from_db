from typing import Optional, List, Dict

from beans.TableBean import TableBean


class NHCTableService:
    """
    新和成服务
    """


    @classmethod
    def get_grouped_all_table_names(cls,names: List[str])->Dict[str,List[str]]:
        """获取一个分组后的表面"""

        result: Dict[str,List[str]] = {}

        if names is None:
            return result

        for name in names:
            # T_PM_SUBSYS 处理特殊表名
            if '_' in name:
                prefix = name[2:4]
                if prefix in result:
                    result[prefix].append(name)
                else:
                    result[prefix] = [name]

                pass
            else:
                prefix = name[1:3]
                if prefix in result:
                    result[prefix].append(name)
                else:
                    result[prefix] = [name]

        return result

    @classmethod
    def get_grouped_all_table_beans(cls, name_beans: List[TableBean]) -> Dict[str, List[TableBean]]:
        """获取一个分组后的表面"""

        result: Dict[str, List[TableBean]] = {}

        if name_beans is None:
            return result

        for bean in name_beans:
            if bean.table_name.startswith("PLATFORM_"):
                pass
            else:
                # T_PM_SUBSYS 处理特殊表名
                if '_' in bean.table_name:
                    prefix = bean.table_name[2:4]
                    if prefix in result:
                        result[prefix].append(bean)
                    else:
                        result[prefix] = [bean]

                    pass
                else:
                    prefix = bean.table_name[1:3]
                    if prefix in result:
                        result[prefix].append(bean)
                    else:
                        result[prefix] = [bean]

        return result