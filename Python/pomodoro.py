#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as spr
import time


def main():
    spr.call(['notify-send', 'Started new pomodoro'])
    time.sleep(30 * 60)
    for i in range(5):
        time.sleep(3)
        spr.call(['notify-send', 'POMODORO END'])


if __name__ == "__main__":
    main()
