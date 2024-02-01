from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TableBean:

    table_name: str

    table_comment: str

