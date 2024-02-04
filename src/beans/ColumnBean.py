from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ColumnBean:
    """列名"""

    column_id: int
    column_name: str
    data_type: str
    data_length: Optional[int]
    data_precision: Optional[int]
    data_scale: Optional[int]
    primary_column: bool
    data_default: Optional[str]
    nullable: str  # 是否为null Y | N
    comment: Optional[str]  # 字段评论
