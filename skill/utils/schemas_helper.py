from typing import List
from skill.models.input import InputSkill
from skill.models.output import OutputSkill, OutputRecord
from marshmallow.schema import MarshalResult, UnmarshalResult

def load_input(json_data: str):
    return InputSkill.Schema().loads(json_data=json_data)

def output_dumps(values: List[OutputRecord]) -> MarshalResult:
    output = OutputSkill(values=values)
    return OutputSkill.Schema().dumps(output)
