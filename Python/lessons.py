#!/usr/bin/env python3
# By HVN at http://pymi.vn/

import datetime

print('PyFML 1609 HCM Schedule')
lesson = 1
MONDAY = 0
WEDNESDAY = 2
day = datetime.date(2016, 9, 12)
while lesson <= 12:
    if day.weekday() == MONDAY or day.weekday() == WEDNESDAY:
        print(lesson, day.strftime('%Y-%m-%d'))
        lesson += 1
    day += datetime.timedelta(1)
print('Then 🍻  😍 ')
