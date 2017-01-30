# coding: utf-8
import datetime

import pandas as pd
import lunardate

import canchi

f = open('presidents.txt')
years = []
for line in f:
    dob = line.strip().split('|')[1].strip()
    dob = datetime.datetime.strptime(dob, '%B %d, %Y')
    if dob.year < 1900:
        # temporarily workaround, calendar libs does not work with years < 1900
        # might lose the precision of result
        # TODO FIXME

        # most of January is still old Lunar year
        if dob.month == 1:
            years.append(dob.year - 1)
        else:
            years.append(dob.year)
    else:
        ld = lunardate.LunarDate.fromSolarDate(dob.year, dob.month, dob.day)
        years.append(ld.year)


branches = [canchi.get_branch(year) for year in years]
s = pd.Series(branches)
print s.value_counts()
