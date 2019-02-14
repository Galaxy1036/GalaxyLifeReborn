import time


def handle_login(command_data, answer_command_data):
    answer_command_data['version'] = '1.22.1'
    answer_command_data['sync'] = 0
    answer_command_data['userId'] = 'an_userid'
    answer_command_data['token'] = 'atoken'

    answer_command_data['myAccountIsLocked'] = 0
    answer_command_data['tutorialCompleted'] = 0  # Switch that to 1 if you don't want the intro to start
    answer_command_data['levelBasedOnScore'] = 1
    answer_command_data['currentTimeMillis'] = str(int(time.time() * 1000))
    answer_command_data['timeFromLastLogin'] = 0
    answer_command_data['timeFromLastUpdate'] = 0
    answer_command_data['androidPublicKey'] = 'someuselesskey'
    answer_command_data['androidGCMRegistrationID'] = ''
    answer_command_data['androidGCMRegistrationLastVersion'] = '1.7.0'
    answer_command_data['androidGPlayMainPassword'] = 'apassword'
    answer_command_data['androidGPlayPatchPassword'] = 'apassword'
    answer_command_data['services'] = []
