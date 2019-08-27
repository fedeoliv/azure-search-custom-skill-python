import marshmallow.validate
from dataclasses import field
from marshmallow_dataclass import dataclass
from typing import List

def output_dumps(values: List[OutputRecord]):
    output = OutputSkill(values=values)
    return OutputSkill.Schema().dumps(output)

@dataclass
class OutputData:
    contractTextProcessed: str = field(metadata={'validate': marshmallow.validate.Length(min=1)})

@dataclass
class OutputRecord:
    recordId: str = field(metadata={'validate': marshmallow.validate.Length(min=1)})
    data: OutputData = field(default_factory=lambda: {})

@dataclass
class OutputSkill:
    values: List[OutputRecord] = field(default_factory=lambda: [])
