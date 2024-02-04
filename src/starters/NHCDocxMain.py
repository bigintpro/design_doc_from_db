from typing import List

from docx import Document

from beans.TableBean import TableBean
from db.oracle.OracleDbService import OracleDbService
from driver.docx.impl.NHCDbDocxServiceImpl import NHCDbDocxServiceImpl

if __name__ == '__main__':
    """自动生成nhc word文档"""

    dbService = OracleDbService()
    list: List[TableBean] = dbService.get_all_table_beans("CYY")

    docx: Document = Document()
    service = NHCDbDocxServiceImpl(docx)
    service.insert_tables(list)
    docx.save("text.docx")

