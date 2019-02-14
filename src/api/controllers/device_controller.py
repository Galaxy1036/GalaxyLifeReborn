import json


def device_route():
    payload = {}

    payload['uid'] = 'an_uid'
    payload['forced'] = 0
    payload['userId'] = 'an_userid'

    return json.dumps(payload)
