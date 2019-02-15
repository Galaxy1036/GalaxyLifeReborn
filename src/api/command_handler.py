available_game_commands = {
    'updateMisc': handle_update_misc,
    'obtainNpcList': handle_obtain_npc_list,
    'obtainUniverse': handle_obtain_universe,
    'obtainCustomizer': handle_obtain_customizer,
    'obtainHangarsHelp': handle_obtain_hangars_help,
    'obtainSocialItems': handle_obtain_social_items,
    'obtainAttackerLog': handle_obtain_attacker_log,
    'obtainNeighborsList': handle_obtain_neighbors_list
}

available_commands = {
    # Social command
    'get-neighbours': handle_get_neighbours,
    'get-incoming-gifts': handle_get_incoming_gifts,

    # Message command
    'get-messages': handle_get_messages,

    # Alliance command
    'getNews': handle_get_news,
    'getAlliance': handle_get_alliance,
    'getAlliances': handle_get_alliances,
    'getMyAlliance': handle_get_my_alliance,
    'getAllianceRequests': handle_get_alliance_requests
}


def handle_game_command_list(command_list, answer_list):
    for command in command_list:
        command_name = command['cmdName']
        command_data = command['cmdData']

        if command_name in available_game_commands:
            print('Game command {} handled !'.format(command_name))

            handler = available_game_commands[command_name]

            add_command_answer(handler, command_name, command_data, answer_list)
        else:
            print('Game command {} not handled !'.format(command_name))


def handle_command(command_name, command_data, answer_command):
    if command_name in available_commands:
        print('Command {} handled !'.format(command_name))

        handler = available_commands[command_name]
        handler(command_data, answer_command)

    else:
        print('Command {} not handled !'.format(command_name))


def add_command_answer(handler, answer_command_name, command_data, answer_list):
    answer_command = {}
    answer_command['cmdData'] = {}
    answer_command['cmdName'] = answer_command_name

    handler(command_data, answer_command['cmdData'])

    answer_list.append(answer_command)
