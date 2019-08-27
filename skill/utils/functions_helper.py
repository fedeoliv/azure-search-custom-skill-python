import json
import azure.functions as func
from skill.models.input import InputSkill
from skill.models.request import RequestResult
from skill.utils.schemas_helper import load_input

def load_request(req: func.HttpRequest) -> RequestResult:
    try:
        req_body = req.get_json()
        json_data = json.dumps(req_body)
        input_skill, error = load_input(json_data)
        if error:
            error_message = 'Invalid JSON properties'
            return RequestResult(valid=False, error=error_message)

        return RequestResult(input_skill=input_skill)
    except ValueError:
        error_message = 'JSON input data not found'
        return RequestResult(valid=False, error=error_message)


def bad_request(error: str) -> func.HttpResponse:
    return func.HttpResponse(error, status_code=400)

def ok(body) -> func.HttpResponse:
    return func.HttpResponse(body=body)
