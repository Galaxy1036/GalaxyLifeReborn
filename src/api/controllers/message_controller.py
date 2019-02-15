import json

from flask import request

from api.command_handler import handle_command


def message_route():
    user_post_data = json.loads(request.form['command'])

    payload = {}

    payload['command'] = user_post_data['command']
    payload['status'] = 'OK'
    payload['error'] = 0

    handle_command(user_post_data['command'], None, payload)

    return json.dumps(payload)
