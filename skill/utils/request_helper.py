import json
import azure.functions as func
from skill.models.input import InputSkill
from skill.models.request import RequestResult

def load_request(req: func.HttpRequest) -> RequestResult:
    try:
        req_body = req.get_json()
        json_data = json.dumps(req_body)
        input_skill, error = InputSkill.Schema().loads(json_data=json_data)

        if error:
            error_message = 'Invalid JSON properties'
            return RequestResult(valid=False, error=error_message)

        return RequestResult(input_skill=input_skill)
    except ValueError:
        error_message = 'JSON input data not found'
        return RequestResult(valid=False, error=error_message)
