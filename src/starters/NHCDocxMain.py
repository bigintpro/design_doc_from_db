from typing import List

from docx import Document

from beans.ModuleTreeData import ModuleTreeData
from beans.TableBean import TableBean
from db.oracle.OracleDbService import OracleDbService
from driver.docx.impl.NHCDbDocxServiceImpl import NHCDbDocxServiceImpl
from service.nhc.NHCModuleClassifyService import NHCModuleClassifyService

if __name__ == '__main__':
    """自动生成nhc word文档"""

    dbService = OracleDbService()
    list: List[TableBean] = dbService.get_all_table_beans("CYY")
    # classify_list: Dict[str, List[TableBean]] = NHCModuleClassifyService.module_classify(list)
    #
    # docx: Document = Document()
    # service = NHCDbDocxServiceImpl(docx)
    # for key, value in classify_list.items():
    #     if len(value) > 0:
    #         service.insert_tables(key, value)
    #
    # docx.save("text.docx")
    classify_module_tree_data: List[ModuleTreeData] = NHCModuleClassifyService.module_tree_classify(list)

    docx: Document = Document()
    service = NHCDbDocxServiceImpl(docx)
    for value in classify_module_tree_data:
        service.insert_title(value.moduleName + "(" + value.modulePrefix + ")", 1)
        if value.children is not None and len(value.children) > 0:
            for sub_value in value.children:
                service.insert_tables(sub_value.moduleName + "(" + sub_value.modulePrefix + ")", sub_value.data)

    docx.save("text.docx")
