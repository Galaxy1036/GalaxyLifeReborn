import json

from flask import request

from api.command_handler import handle_command


def social_route():
    user_post_data = json.loads(request.form['command'])

    payload = {}

    payload['status'] = 'OK'
    payload['command'] = user_post_data['command']

    handle_command(user_post_data['command'], user_post_data, payload)

    return json.dumps(payload)
