import json

from flask import request

from api.command_handler import handle_command


def alliance_route():
    user_post_data = json.loads(request.form['data'])

    payload = {}

    data = {}

    data['action'] = user_post_data['action']
    data['error'] = 0

    handle_command(user_post_data['action'], user_post_data, data)

    payload['data'] = json.dumps(data)

    return json.dumps(payload)
