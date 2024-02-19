from typing import List

from beans.ColumnBean import ColumnBean


class NHCDBXlsxTemplate:
    """nhc xlsx的模版"""

    title = ["序号", "字段名称", "字段注释", "数据类型", "字段长度", "小数位数", "值域", "默认值", "约束", "键",
             "非空性", "备注"]

    @classmethod
    def parse_table_column(cls, table_columns: List[ColumnBean]):
        if table_columns is None:
            raise Exception("table_column cannot be None")

        data = []
        for index, table_column in enumerate(table_columns):
            tmp = []
            tmp.append(str(index + 1))
            tmp.append(table_column.column_name)
            tmp.append(table_column.comment if table_column.comment is not None else "")
            tmp.append(table_column.data_type)
            tmp.append(str(table_column.data_length) if table_column.data_length is not None else "")
            tmp.append(str(table_column.data_precision) if table_column.data_precision is not None else "")
            tmp.append(str(table_column.data_scale) if table_column.data_scale is not None else "")
            tmp.append("")
            tmp.append(str(table_column.data_default) if table_column.data_default is not None else "")
            tmp.append("TRUE" if table_column.primary_column else "FALSE")
            tmp.append("FALSE" if table_column.nullable == 'Y' else "TRUE")
            tmp.append("")
            data.append(tmp)
        return data
