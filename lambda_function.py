import json


def build_response(isBase64Encoded=False, statusCode=200, headers=None, data=None, **kwargs):
    body = json.dumps(dict(**(data or dict()), **kwargs))
    return dict(isBase64Encoded=isBase64Encoded, statusCode=statusCode, headers=headers or dict(), body=body)


def lambda_handler(event, context):
    body = json.loads(event['body'])
    payload = [body['message'] for _ in range(body['count'])]
    return build_response(message=payload)
