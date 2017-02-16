# coding: utf-8
'''Script calculates sched for PyFML class http://pymi.vn
'''
import datetime

TUE = 1
THURS = 3


def main():
    cntr = 0
    # TODO get input
    date = datetime.datetime(2017, 2, 23)
    while cntr < 12:
        if date.weekday() == THURS or date.weekday() == TUE:
            cntr += 1
            print(date.strftime('%c'))

        date += datetime.timedelta(1)


if __name__ == "__main__":
    main()
