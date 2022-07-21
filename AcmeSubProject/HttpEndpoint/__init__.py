import logging
import uuid
import json
import time
import azure.functions as func


def main(request: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")

    rowKey = str(uuid.uuid4())

    data = {
        "Name": "Output binding message",
        "PartitionKey": "message",
        "RowKey": rowKey
    }

    message.set(json.dumps(data))

    end = time.time()
    processingTime = end - start

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translation is: {subtitle}, Message created with the rowKey: {rowKey}",
        status_code=200
    )