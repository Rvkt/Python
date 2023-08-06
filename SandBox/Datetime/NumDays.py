import calendar
from datetime import datetime
now = datetime.now()

numDay = calendar.monthrange(now.year, now.month)[1]
# print(numDay)

monthNum = now.strftime('%B')
yearMonthNum = now.strftime('%Y_%m')


# print('Number of days in the ' + monthNum + ' is ' + str(numDay))
# print(yearMonthNum)

def numDates():
    for d in range(1, calendar.monthrange(now.year, now.month)[1] + 1):
        print(f'{yearMonthNum}_{str(d).zfill(2)}')

numDates()