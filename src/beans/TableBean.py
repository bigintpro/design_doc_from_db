from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json

from beans.ColumnBean import ColumnBean


@dataclass_json
@dataclass
class TableBean:

    """表名"""
    table_name: str

    """表评论"""
    table_comment: Optional[str]

    """表字典"""
    table_columns: List[ColumnBean]




