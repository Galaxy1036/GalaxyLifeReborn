def handle_get_my_alliance(command_data, answer_command_data):
    answer_command_data['alliance'] = {}

    answer_command_data['alliance']['name'] = 'a_name'
    answer_command_data['alliance']['id'] = 0
    answer_command_data['alliance']['logo'] = []
    answer_command_data['alliance']['messageOfTheDay'] = 'nomessage'
    answer_command_data['alliance']['motdUpdatedAt'] = 0

    answer_command_data['alliance']['rank'] = 0
    answer_command_data['alliance']['warsLost'] = 0
    answer_command_data['alliance']['warsWon'] = 0
    answer_command_data['alliance']['totalWarScore'] = 0
    answer_command_data['alliance']['currentWarDamage'] = 0
    answer_command_data['alliance']['totalMembers'] = 0
    answer_command_data['alliance']['enemyAllianceId'] = 0
    answer_command_data['alliance']['warStartTime'] = 0
    answer_command_data['alliance']['warEndTime'] = 0
    answer_command_data['alliance']['postWarShield'] = 0

    answer_command_data['alliance']['members'] = []
