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


def _generate_sound_file(filename='noise.wav'):
    RATE = 44100

    def get_note(note, length=None):
        import struct
        from math import sin, pi

        if length is None:
            length = int(RATE/4)

        wv_data = b""
        for i in range(0, length):
            max_vol = 2 ** 15 - 1.0
            raw = round(max_vol * sin(i * 2 * pi * note / RATE))
            wv_data += struct.pack('h', raw)
            wv_data += struct.pack('h', raw)
        return wv_data

    import wave

    noise_output = wave.open(filename, 'wb')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    A6 = 1760
    B6 = 1975.53
    C7 = 2093.00
    wv_data = b"".join([get_note(n) for n in [A6, B6, C7]])

    noise_output.writeframes(wv_data)

    noise_output.close()


def play_sound():
    dirname = os.path.expanduser("~/.local/share/pomop")
    try:
        os.mkdir(dirname)
    except Exception:
        pass

    filepath = os.path.join(dirname, 'sound.wav')
    _generate_sound_file(filepath)

    try:
        if sys.platform == 'darwin':
            spr.call(["afplay", filepath])
        elif 'win' in sys.platform:
            spr.call(["start", filepath])
        else:
            # Linux or other non-tested platform such as BSD*
            try:
                spr.call(["aplay", filepath])
            except Exception:
                spr.call(["xdg-open", filepath])

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
    end_msg = 'POMO: {0:.0f} minute passed.\tFrom {1}'.format(
        duration, start_str
    )

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
