import marshmallow.validate
from dataclasses import field
from marshmallow_dataclass import dataclass
from typing import List

@dataclass
class InputData:
    contractText: str = field(metadata={'validate': marshmallow.validate.Length(min=1)})

@dataclass
class InputRecord:
    recordId: str = field(metadata={'validate': marshmallow.validate.Length(min=1)})
    data: InputData = field(default_factory=lambda: {})

@dataclass
class Input:
    values: List[InputRecord] = field(default_factory=lambda: [])
