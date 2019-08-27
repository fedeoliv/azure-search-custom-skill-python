import marshmallow.validate
from dataclasses import field
from marshmallow_dataclass import dataclass
from typing import List

@dataclass
class InputData:
    contractText: str

@dataclass
class InputRecord:
    recordId: str
    data: InputData

@dataclass
class InputSkill:
    values: List[InputRecord]
