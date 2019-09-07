from ..models.input import InputSkill

class RequestResult:
    def __init__(self, valid: bool = True, input_skill: InputSkill = None, error: str = None):
        self.valid = valid
        self.input_skill = input_skill
        self.error = error

