import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HIDevOps function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        if req_body:
            name = req_body.get('name')

    if not name:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )

    greeting = f"Hi, {name}} team! welcome to DevOps Learning Series"
    return func.HttpResponse(greeting, status_code=200, mimetype="text/plain")
