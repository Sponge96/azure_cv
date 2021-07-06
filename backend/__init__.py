import logging

import azure.functions as func


def main(req: func.HttpRequest, inputDoc: func.DocumentList, outputDoc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    counter = new_counter_val(inputDoc[0]['count'])
    inputDoc[0]['count'] = counter
    outputDoc.set(func.Document.from_json(inputDoc[0].to_json()))

    if counter:
        return func.HttpResponse(f"{counter}", status_code=200)
    else:
        return func.HttpResponse(
            "Error",
            status_code=500)


def new_counter_val(value: int):
    return value + 1