import subprocess
import sys
"""
Generate sound wav file and play it.
tested player on OSX, Ubuntu16.04
"""


RATE = 44100


def get_note(note, length=None):
    import struct
    from math import sin, pi

    if length is None:
        length = round(RATE/4)

    wv_data = b""
    for i in range(0, length):
        max_vol = 2 ** 15 - 1.0
        raw = round(max_vol * sin(i * 2 * pi * note / RATE))
        wv_data += struct.pack('h', raw)
        wv_data += struct.pack('h', raw)
    return wv_data


def generate_sound_file(filename='noise.wav'):
    import wave

    noise_output = wave.open(filename, 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    A6 = 1760
    B6 = 1975.53
    C7 = 2093.00
    wv_data = b"".join([get_note(n) for n in [A6, B6, C7]])

    noise_output.writeframes(wv_data)

    noise_output.close()


filename = 'noise.wav'
generate_sound_file(filename)
if sys.platform == 'darwin':
    subprocess.call(['afplay', filename])
elif 'win' in sys.platform:
    subprocess.call(['start', 'wmplayer', filename])
else:
    try:
        subprocess.call(['xdg-open', filename])
    except Exception:
        try:
            # TODO when this work, switch with xdg-open
            subprocess.call(['mpg321', filename])
        except Exception:
            print("Cannot play sound file")
