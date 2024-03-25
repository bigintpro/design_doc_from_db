from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ModuleNameNode:
    """模块名称"""
    module_name: str

    """模块前缀"""
    module_prefix: str
