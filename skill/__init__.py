import logging
import azure.functions as func
from skill.utils.request_helper import load_request

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom kill processed a request.')

    req_result = load_request(req)

    if not req_result.valid:
        return func.HttpResponse(
            req_result.error,
            status_code=400
        )

    return func.HttpResponse('OK')
