import os
import sys
import time
import frida

from colorama import Fore, init


script_name = 'gl_hook.js'
package_name = 'com.digitalchocolate.igalaxy'
MAX_FRIDA_RETRY = 10

log_color_dict = {
    'info': Fore.LIGHTCYAN_EX,
    'verbose': Fore.LIGHTBLUE_EX,
    'error': Fore.LIGHTRED_EX,
    'debug': Fore.LIGHTGREEN_EX,
    'warning': Fore.LIGHTYELLOW_EX,
    'native': Fore.LIGHTMAGENTA_EX
}


def message(message, data):
    if message.get('payload'):
        log_type, log_message = message['payload'].split(':::')
        print('{}{}{}'.format(log_color_dict.get(log_type, ''), log_message, Fore.RESET))

    else:
        print(message)


def start_frida_script():
    try:
        device = frida.get_usb_device()

    except Exception as exception:
        print('[*] Can\'t connect to your device ({}) !'.format(exception.__class__.__name__))
        exit()

    print('[*] Successfully connected to frida server !')

    pid = device.spawn([package_name])

    retry_count = 0
    process = None

    while not process:
        try:
            process = device.attach(pid)

        except Exception as exception:
            if retry_count == MAX_FRIDA_RETRY:
                print('[*] Can\'t attach frida to the game ({}) ! Start the frida server on your device'.format(exception.__class__.__name__))
                exit()

            retry_count += 1
            time.sleep(0.5)

    print('[*] Frida attached !')

    if os.path.isfile(script_name):
        script = process.create_script(open(script_name).read())

    else:
        print('[*] {} script is missing, cannot inject the script !'.format(script_name))
        exit()

    script.on('message', message)
    script.load()
    device.resume(pid)
    print('[*] Script injected !')


if __name__ == '__main__':
    init()
    start_frida_script()
    sys.stdin.read()
