import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_short = calendar.month_abbr[1:]

for i in month_short:
    print(f'{year}{i.upper()}')