from typing import List, Dict

from docx import Document

from beans.TableBean import TableBean
from db.oracle.OracleDbService import OracleDbService
from driver.docx.impl.NHCDbDocxServiceImpl import NHCDbDocxServiceImpl
from service.nhc.NHCModuleClassifyService import NHCModuleClassifyService

if __name__ == '__main__':
    """自动生成nhc word文档"""

    dbService = OracleDbService()
    list: List[TableBean] = dbService.get_all_table_beans("CYY")
    classify_list: Dict[str, List[TableBean]] = NHCModuleClassifyService.module_classify(list)

    docx: Document = Document()
    service = NHCDbDocxServiceImpl(docx)
    for key, value in classify_list.items():
        if len(value) > 0:
            service.insert_tables(key, value)
    
    docx.save("text.docx")
