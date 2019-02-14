import json

from flask import request
from command.game_command.login_command import handle_login
from api.command_handler import handle_game_command_list, add_command_answer


def game_route():
    user_post_data = json.loads(request.form['data'])

    payload = {}

    payload['service'] = 'GamePacket'
    payload['czlb'] = "0"  # if set to true (1) the game will decompress our data field with base64 + zlib
    payload['chk'] = 0

    data = {}

    data['packetCount'] = -1
    data['list'] = []

    if user_post_data['packetType'] == 'login':
        add_command_answer(
                           handle_login,
                           'logOK',
                           user_post_data['packetData'],
                           data['list']
                           )

    elif user_post_data['packetType'] == 'cmdList':
        handle_game_command_list(user_post_data['packetData']['cmdList'], data['list'])

    payload['data'] = json.dumps(data)
    return json.dumps(payload)
