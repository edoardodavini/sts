import requests
import filler

VALID_HTTP_METHODS = {
    'GET':      ['url'],
    'PATCH':    ['url', 'data'],
    'PUT':      ['url', 'data'],
    'POST':     ['url', 'data'],
    'DELETE':   ['url'],
}


# http calls with string building:
def call(req, responses):
    validate_request(req)
    method = req.get('method', None)
    url = filler.fill_regex(req['url'], responses)
    payload = req.get('data', None)
    headers = None

    print('Calling {method} @ {url}'.format(method=method, url=url))

    return requests.request(method=method, url=url, json=payload, headers=headers).json()


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
