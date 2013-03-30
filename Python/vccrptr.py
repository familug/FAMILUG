#!/usr/bin/env python
#-*-encoding: utf-8 -*-

from datetime import date as dtdate
from datetime import timedelta

""" A simple script auto generate data for 
    reporting weekly at BBTeam - VCCloud"""

# TODO: get data from git and wiki, teamspace
# put them all in template then send

def get_week_boundary(day_in_week=dtdate.today()):
    """ Return a tuple contains Monday and Saturday day of a week """
    dow = day_in_week.weekday()

    mon_of_week = day_in_week - timedelta(dow)
    sat_of_week = mon_of_week + timedelta(5)
    date_format = "%Y/%m/%d"

    return (mon_of_week.strftime(date_format), 
            sat_of_week.strftime(date_format))

def get_subject(wbdr=get_week_boundary()):
    return "Báo cáo tuần (%s -> %s)" % wbdr

if __name__ == "__main__":
    print get_subject()
