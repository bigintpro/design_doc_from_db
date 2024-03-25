from dataclasses import dataclass
from typing import List, TypeVar

from dataclasses_json import dataclass_json

T = TypeVar('T')


@dataclass_json
@dataclass
class ModuleTreeData:
    """模块名称"""
    moduleName: str

    """模块前缀"""
    modulePrefix: str

    """模块挂在数据"""
    children: List['ModuleTreeData']

    data: List[T]
