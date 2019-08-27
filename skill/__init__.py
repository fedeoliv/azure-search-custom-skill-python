import logging
import azure.functions as func
from typing import List
from skill.models.output import OutputRecord
from skill.utils.schemas_helper import output_dumps
from skill.utils.functions_helper import load_request, bad_request, ok

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom kill processed a request.')

    req_result: RequestResult = load_request(req)

    if not req_result.valid:
        return bad_request(req_result.error)

    input_skill: InputSkill = req_result.input_skill

    # YOUR CODE HERE

    values: List[OutputRecord] = [] # Update your values property
    output_json, error = output_dumps(values)

    if error:
        return bad_request('Invalid output format')
    
    return ok(output_json)
