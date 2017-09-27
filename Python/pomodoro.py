#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import subprocess as spr
import time


def main():
    start = datetime.datetime.now()
    start_str = start.strftime("%H:%M:%S")
    spr.call(['notify-send',
              '--app-name', 'POMODORO',
              '--icon', 'dialog-information',
              'New pomodoro', 'From: {}'.format(start_str)])
    time.sleep(30 * 60)
    end = datetime.datetime.now()
    duration = (end - start).total_seconds() // 60

    for i in range(5):
        time.sleep(3)
        spr.call(
            ['notify-send',
             'POMO: {0:.0f} minute passed.\tFrom {1}'.format(
                 duration,
                 start_str
             )
             ]
        )


if __name__ == "__main__":
    main()
