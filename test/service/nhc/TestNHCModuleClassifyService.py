from unittest import TestCase

from beans.TableBean import TableBean
from service.nhc.NHCModuleClassifyService import NHCModuleClassifyService


class TestNHCModuleClassifyService(TestCase):
    def test_module_classify(self):
        bean_str = '[{"table_name":"TNMBL01","table_comment":"能源平衡组配置","table_columns":[{"column_id":1,"column_name":"ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":true,"data_default":null,"nullable":"N","comment":"主键"},{"column_id":2,"column_name":"BAL_NAME","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"平衡组名称"},{"column_id":3,"column_name":"MA_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"能源介质（物料ID）"},{"column_id":4,"column_name":"DEV_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"区域（单体ID）"},{"column_id":5,"column_name":"PRIORITY","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"优先级"},{"column_id":6,"column_name":"ACTIVE_STATUS","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"是否激活"},{"column_id":7,"column_name":"REMARKS","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"备注"},{"column_id":8,"column_name":"CREATE_USER","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"创建人"},{"column_id":9,"column_name":"CREATE_TIME","data_type":"TIMESTAMP(6)","data_length":11,"data_precision":null,"data_scale":6,"primary_column":false,"data_default":null,"nullable":"Y","comment":"创建时间"},{"column_id":10,"column_name":"UPDATE_USER","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"最后修改人"},{"column_id":11,"column_name":"UPDATE_TIME","data_type":"TIMESTAMP(6)","data_length":11,"data_precision":null,"data_scale":6,"primary_column":false,"data_default":null,"nullable":"Y","comment":"最后修改时间"},{"column_id":12,"column_name":"DELETE_FLAG","data_type":"CHAR","data_length":1,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":"0","nullable":"Y","comment":"删除标记"},{"column_id":13,"column_name":"TENANT_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"租户ID"}]},{"table_name":"TNMBL02","table_comment":"能源平衡组模型（平衡项）","table_columns":[{"column_id":1,"column_name":"ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":true,"data_default":"0  ","nullable":"N","comment":"主键"},{"column_id":2,"column_name":"BAL_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"平衡组ID"},{"column_id":3,"column_name":"MODELITEM_NAME","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"平衡项名称"},{"column_id":4,"column_name":"SOUCE_TYPE","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"来源"},{"column_id":5,"column_name":"SOUCE_ITEM_ID","data_type":"VARCHAR2","data_length":64,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"项目号"},{"column_id":6,"column_name":"ITEM_TYPE","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"类型"},{"column_id":7,"column_name":"IS_FIX","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"是否固定值"},{"column_id":8,"column_name":"DEPT_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"部门ID"},{"column_id":9,"column_name":"PARENT_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"N","comment":"能源平衡组配置"},{"column_id":10,"column_name":"SORT","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"排序"},{"column_id":11,"column_name":"MA_ID","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":null,"nullable":"Y","comment":"能介"},{"column_id":12,"column_name":"COVERTF","data_type":"NUMBER","data_length":22,"data_precision":18,"data_scale":6,"primary_column":false,"data_default":null,"nullable":"Y","comment":"系数"},{"column_id":13,"column_name":"IS_MAIN","data_type":"VARCHAR2","data_length":32,"data_precision":null,"data_scale":null,"primary_column":false,"data_default":"0","nullable":"Y","comment":"关注项"}]}]'

        beans = TableBean.schema().loads(bean_str, many=True)

        result = NHCModuleClassifyService.module_classify(beans)
        print(result)

        self.assertEquals(True, True)
