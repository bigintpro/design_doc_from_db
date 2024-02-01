import json
import unittest

from dataclasses_json import DataClassJsonMixin

from beans.TableBean import TableBean
from service.NHCTableService import NHCTableService


class TestNHCTableService(unittest.TestCase):
    def test_get_grouped_all_table_names(self):
        names = ['TPMDE01', 'TPMDE02', 'TPMIM02', 'TPMIM03', 'TPMSF07', 'TPMSF05', 'TPMSY01', 'TPMSM02', 'TODOITEM', 'TNMCG01', 'TPMSM12', 'TPMSM13', 'TPMSM06', 'TPMSM07', 'TPMSM08', 'TPMSM09', 'TSYCG01', 'TSYCG02', 'TPMMA01', 'TPMMA03', 'TPMMA04', 'TPMUN01', 'TNMBL01', 'TNMBL02', 'T_PM_SUBSYS', 'TPMSF01', 'TPMSF02', 'TPMSF03', 'TPMSF04', 'TPMUD01', 'TPMDE03', 'TPMSF06', 'TPSXD04', 'TPSXD05', 'TPSXD01', 'TPSXD02', 'TPSXD03', 'TPMIM01', 'TPMSM50']
        dict = NHCTableService.get_grouped_all_table_names(names)
        print(dict)
        self.assertIsNotNone(dict)

    def test_get_grouped_all_table_beans(self):
        bean_str = '[{"table_name": "PLATFORM_TENANT", "table_comment": "租户表"}, {"table_name": "PLATFORM_TENANT_DEPT_REL", "table_comment": "租户组织机构关联表"}, {"table_name": "TNMBL01", "table_comment": "能源平衡组配置"}, {"table_name": "TNMBL02", "table_comment": "能源平衡组模型（平衡项）"}, {"table_name": "TNMCG01", "table_comment": "能源折标系数表"}, {"table_name": "TODOITEM", "table_comment": null}, {"table_name": "TPMDE01", "table_comment": "单体属性表"}, {"table_name": "TPMDE02", "table_comment": "单体树形关系表"}, {"table_name": "TPMDE03", "table_comment": "单体子系统关系表"}, {"table_name": "TPMIM01", "table_comment": "仪表点表"}, {"table_name": "TPMIM02", "table_comment": "仪表基础类型关系表"}, {"table_name": "TPMIM03", "table_comment": "仪表周期关系表"}, {"table_name": "TPMMA01", "table_comment": "物料表"}, {"table_name": "TPMMA03", "table_comment": "物料种类关系表"}, {"table_name": "TPMMA04", "table_comment": "物料与子系统关系表"}, {"table_name": "TPMSF01", "table_comment": "排班管理"}, {"table_name": "TPMSF02", "table_comment": "排班班次"}, {"table_name": "TPMSF03", "table_comment": "排班班组"}, {"table_name": "TPMSF04", "table_comment": "排班循环"}, {"table_name": "TPMSF05", "table_comment": "排班循环"}, {"table_name": "TPMSF06", "table_comment": "周期配置管理"}, {"table_name": "TPMSF07", "table_comment": "周期配置月份表"}, {"table_name": "TPMSM02", "table_comment": "统计项目配置表"}, {"table_name": "TPMSM06", "table_comment": "统计实例表"}, {"table_name": "TPMSM07", "table_comment": "统计公式定义表"}, {"table_name": "TPMSM08", "table_comment": "计算配置表"}, {"table_name": "TPMSM09", "table_comment": "表缩写信息配置表"}, {"table_name": "TPMSM12", "table_comment": "统计数据表"}, {"table_name": "TPMSM13", "table_comment": "日志信息表"}, {"table_name": "TPMSM50", "table_comment": "xx表"}, {"table_name": "TPMSY01", "table_comment": "单体导入文件表"}, {"table_name": "TPMUD01", "table_comment": "用户区域表"}, {"table_name": "TPMUN01", "table_comment": "工程单位表"}, {"table_name": "TPSXD01", "table_comment": "行动项表"}, {"table_name": "TPSXD02", "table_comment": "行动项任务详情表"}, {"table_name": "TPSXD03", "table_comment": "任务检查内容表"}, {"table_name": "TPSXD04", "table_comment": "会议管理"}, {"table_name": "TPSXD05", "table_comment": "会议人员"}, {"table_name": "TSYCG01", "table_comment": "数据字典管理表"}, {"table_name": "TSYCG02", "table_comment": "数据字典表"}, {"table_name": "T_PM_SUBSYS", "table_comment": "子系统表"}]'
        beans = json.loads(bean_str, object_hook=lambda d: TableBean(**d))

        # beans = DataClassJsonMixin.schema().loads(bean_str, many=True)

        dict = NHCTableService.get_grouped_all_table_beans(beans)
        print(dict)
        self.assertIsNotNone(dict)


if __name__ == '__main__':
    unittest.main()
