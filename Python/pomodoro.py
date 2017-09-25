#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import subprocess as spr
import time


def main():
    start = datetime.datetime.now()
    spr.call(['notify-send', 'Started new pomodoro'])
    time.sleep(30 * 60)
    end = datetime.datetime.now()
    duration = (end - start).total_seconds() // 60

    for i in range(5):
        time.sleep(3)
        spr.call(
            ['notify-send',
             'POMO: {0:.0f} minute passed.\tFrom {1}'.format(
                 duration,
                 start.strftime("%H:%M:%S"))
             ]
        )


if __name__ == "__main__":
    main()
