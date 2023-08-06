import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_long = []

for i in range(1, 13):
    month_long.append(calendar.month_name[i]) # month_name is an array
for i in month_long:
    print(f'{year}{i[0:3].upper()}')