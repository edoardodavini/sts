import requests
import json
import filler

VALID_HTTP_METHODS = {
    'GET':      ['url'],
    'PATCH':    ['url', 'data'],
    'PUT':      ['url', 'data'],
    'POST':     ['url', 'data'],
    'DELETE':   ['url'],
}


# http calls with string building:
def call(req, responses, config = {}):
    validate_request(req)
    base_url = config.get('baseUrl', '')

    method = req.get('method', None)
    url = filler.fill_regex(req['url'].replace('{{baseUrl}}', base_url), responses)
    payload = req.get('data', None)
    if payload is not None:
        payload_clean = filler.fill_regex(payload, responses)
        payload = json.loads(payload_clean)
    headers = None

    print('Calling {method} @ {url}'.format(method=method, url=url))
    response_raw = requests.request(method=method, url=url, json=payload, headers=headers)
    response = {
        "headers": response_raw.headers,
        "body": response_raw.text,
        "status": response_raw.status_code,
        "request": response_raw.request
    }
    try:
        response["json"] = response_raw.json()
    except json.JSONDecodeError:
        print('Unable to parse json response')
        response["json"] = None
    print('Response ({number}) {status}: {response}'.format(number=len(responses), status=response['status'], response=json.dumps(response.get('json', 'No Json Available'))))
    return response


# simple validation
def validate_request(req):
    name = req.get('name', 'UNNAMED REQUEST')
    method = req.get('method', None)
    if method is None:
        raise Exception('MISSING METHOD')
    if method not in VALID_HTTP_METHODS.keys():
        raise Exception('INVALID METHOD {method}'.format(method=method))

    configs = VALID_HTTP_METHODS.get(method)
    for config in configs:
        if req.get(config, None) is None:
            raise Exception('MISSING {config} FROM {name}'.format(config=config, name=name))

    return True
