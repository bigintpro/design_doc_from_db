from typing import List, Dict

from openpyxl.workbook import Workbook

from beans.TableBean import TableBean
from db.oracle.OracleDbService import OracleDbService
from driver.xlsx.impl.XlsxServiceImpl import XlsxServiceImpl
from service.nhc.NHCModuleClassifyService import NHCModuleClassifyService

if __name__ == '__main__':
    """自动生成nhc xlsx文档"""

    dbService = OracleDbService()
    list: List[TableBean] = dbService.get_all_table_beans("CYY")
    classify_list: Dict[str, List[TableBean]] = NHCModuleClassifyService.module_classify(list)

    wb = Workbook()
    service = XlsxServiceImpl(wb)

    for key, value in classify_list.items():
        if len(value) > 0:
            service.insert_tables(key, value)

    wb.save("test.xlsx")
