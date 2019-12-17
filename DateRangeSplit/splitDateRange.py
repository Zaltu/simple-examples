#pylint: skip-file
import datetime

#[
#    0 = MONDAY
#    1 = TUESDAY
#    2 = WEDNESDAY
#    3 = THURSDAY
#    4 = FRIDAY
#    5 = SATURDAY
#    6 = SUNDAY
#]

SG_DATE_FORMAT = "%Y-%m-%d"

START = "2020-04-23"
END = "2020-05-19"

WEEKS = []

dt_start = datetime.datetime.strptime(START, SG_DATE_FORMAT)
dt_end = datetime.datetime.strptime(END, SG_DATE_FORMAT)

w1e = dt_start + datetime.timedelta(days=4-dt_start.weekday())  # See weekday commentary
wns = dt_end - datetime.timedelta(days=dt_end.weekday())  # See weekday commentary

WEEKS.append((wns.date(), dt_end.date()))

it = wns - datetime.timedelta(days=7)

while it > dt_start:
    wie = it + datetime.timedelta(days=4)
    WEEKS.append((it.date(), wie.date()))
    it = it - datetime.timedelta(days=7)

WEEKS.append((dt_start.date(), w1e.date()))

from pprint import pprint as pp
pp(WEEKS)
