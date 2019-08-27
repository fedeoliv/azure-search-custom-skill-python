import logging
import azure.functions as func
from skill.utils.request_helper import load_request
from skill.models.output import output_dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom kill processed a request.')

    req_result: RequestResult = load_request(req)

    if not req_result.valid:
        return func.HttpResponse(
            req_result.error,
            status_code=400
        )

    input_skill: InputSkill = req_result.input_skill

    # YOUR CODE HERE

    values: List[OutputRecord] = [] # Update your values property
    output_json, error = output_dumps(values)

    if error:
        return func.HttpResponse(
            'Invalid output format',
            status_code=400
        )
    
    return func.HttpResponse(output_json)
