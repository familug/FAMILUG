#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import subprocess as spr
import sys
import time

APP_NAME = 'PmP: Poor man Pomodoro'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def write_finish_page(start, stop):
    import tempfile
    _, name = tempfile.mkstemp()
    html = """<html><body><h1>DONE POMODORO</h1>
    <h2>Start at: {}</h2>
    <h2>End at: {}</h2>
    </body></html>""".format(start, stop)
    with open(name, 'w') as fd:
        fd.write(html)

    import webbrowser
    webbrowser.open("file:///{}".format(name))


def generate_sound_file():
    import wave
    import struct
    import random
    LEN = 3
    SAMPLE_LEN = 44100 * LEN

    noise_output = wave.open('noise2.wav', 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    values = []

    for i in range(0, SAMPLE_LEN):
            value = random.randint(-32767, 32767)
            packed_value = struct.pack('h', value)
            values.append(packed_value)
            values.append(packed_value)

    value_str = ''.join(values)
    noise_output.writeframes(value_str)

    noise_output.close()
    pass


def play_sound():
    # TODO: generate a simple sound file and play it
    SOUND_FILE = os.path.expanduser("~/pomo.mp3")

    try:
        if sys.platform == 'darwin':
            spr.call(["afplay", SOUND_FILE])
        elif 'win' in sys.platform:
            spr.call(["start", SOUND_FILE])
        else:
            # Linux or other non-tested platform such as BSD*
            spr.call(["xdg-open", SOUND_FILE])

    except Exception as e:
        print("Play sound error", e)


def send_notification(messages):
    if isinstance(messages, str):
        messages = [messages]

    assert isinstance(messages, list)

    try:
        spr.call(['notify-send',
                  '--app-name', 'POMODORO',
                  '--icon', 'dialog-information',
                  ] + messages)
    except OSError:
        # notify-send not installed, skip
        pass


def notify_start(start):
    start_msg = 'Start new Pomodoro!'

    play_sound()
    send_notification(start_msg)


def notify_end(start, end):
    start_str = start.strftime("%H:%M:%S")
    duration = (end - start).total_seconds() // 60
    end_msg = 'POMO: {0:.0f} minute passed.\tFrom {1}'.format(duration, start_str)

    play_sound()
    send_notification(end_msg)
    write_finish_page(start, end)


def main():
    start = datetime.datetime.now()
    DURATION = 30
    ONE_MINUTE_IN_SEC = 60

    notify_start(start)

    for minute in range(DURATION, 0, -1):
        print("{}: remaining {} minutes".format(APP_NAME, minute))
        time.sleep(ONE_MINUTE_IN_SEC)
        clear_screen()

    end = datetime.datetime.now()

    notify_end(start=start, end=end)


if __name__ == "__main__":
    main()
