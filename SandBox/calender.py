import calendar

cal= calendar.Calendar(firstweekday=0)

for x in cal.iterweekdays():
    print(x)

#set firstweekday=1
cal= calendar.Calendar(firstweekday=1)
for x in cal.iterweekdays():
    print(x)

cal= calendar.Calendar()
for x in cal.itermonthdates(2022, 1):
	print(x)

# cal= calendar.Calendar()
for x in cal.itermonthdays2(2022, 1):
	print(x)

# cal= calendar.Calendar()
for x in cal.itermonthdays(2022, 1):
	print(x)

# cal= calendar.Calendar()
for date in cal.monthdatescalendar(2022, 1):
    print(date)

# cal= calendar.Calendar()
print(cal.monthdays2calendar(2022, 1))

print(cal.monthdayscalendar(2022, 1))

print(cal.yeardatescalendar(2022, 1))

print(cal.yeardays2calendar(2022, 1))

print(cal.yeardayscalendar(2022, 1))

"""TEXT CALENDER"""

import calendar
from datetime import date, datetime

tc= calendar.TextCalendar(firstweekday=0)
now = datetime.now()
year = int(now.strftime('%Y'))
month_int = int(now.strftime('%m'))

print( tc.formatmonth(year, month_int))



"""**Get Number of Days In the Month**"""

from calendar import monthrange

num_days = monthrange(2022, 1)[1]
print(f'Number of days: {num_days}.')

def num_days(year, month):
    return monthrange(year, month)[1]

print(f'Number of days: {num_days(2022, 2)}.')

from calendar import monthrange
from datetime import date, datetime

date = date.today()
now = datetime.now()
year = now.strftime('%Y')
month_int = now.strftime('%m')
daysInMonth= monthrange(date.year, date.month)[1]

for i in range((daysInMonth)):
    print(f'{year}{month_int}{str(i+1).zfill(2)}')

import calendar
import datetime

currentDate = datetime.date.today()
daysInMonth= calendar.monthrange(currentDate.year, currentDate.month)[1]
lastDayOfMonth = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[1])

print(currentDate)
print(daysInMonth)
print(lastDayOfMonth)