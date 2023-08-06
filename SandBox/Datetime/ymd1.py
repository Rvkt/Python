import calendar
from datetime import datetime

now = datetime.now()

year = now.strftime('%Y')
month_int = (now.strftime('%m').zfill(2))
numDays = calendar.monthrange(now.year, now.month)[1]
# print(numDays)
print(
    f'Year is: {year}, Month is: {month_int} and number of days in the current month ({month_int}) is {numDays} days.')

def numDaysDirs():
    for d in range(1, numDays + 1):
        print(f'{year}_{month_int}_{str(d).zfill(2)}')

