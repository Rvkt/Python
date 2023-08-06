from calendar import monthrange
from datetime import date, datetime

now = datetime.now()
year = input('Enter Year: ')
month = input('Enter Month: ')
yymm = now.strftime(f'{year}{month}')
date = date.today()
daysInMonth = monthrange(int(year), int(month))[1]
dayNum = []

for i in range(daysInMonth):
    dayNum.append(f'{yymm}{str(i + 1).zfill(2)}')

for i in dayNum:
    print(i)

# date = date.today()
now = datetime.now()
year = now.strftime('%Y')
month = now.strftime('%m')

'''Version One'''


# daysInMonth= monthrange(2022, 9)[1]+1
# print(f'No. of Days: {monthrange(2022, 1)[1]}')
# print(daysInMonth)
# for i in range(1,daysInMonth+1):
#     print(str(i).zfill(2))


# daysINMonth= monthrange(int(year), int(month))[1]+1
# print(f'No. of Days: {monthrange(int(year), int(month))[1]+1}')
# print(daysINMonth)
# for m in range(1, int(daysINMonth)+1):
#     print(str(m).zfill(2))

def vOne():
    daysInMonth = monthrange(2022, 9)[1] + 1
    print(f'No. of Days: {monthrange(2022, 1)[1]}')
    print(daysInMonth)
    for i in range(1, daysInMonth + 1):
        print(str(i).zfill(2))


def vTwo():
    daysInMonth = monthrange(int(year), int(month))[1] + 1
    print(f'No. of Days: {monthrange(int(year), int(month))[1] + 1}')
    print(daysInMonth)
    for m in range(1, int(daysInMonth) + 1):
        print(str(m).zfill(2))


print('Version Two')

daysINMonth = monthrange(int(year), int(month))[1] + 1
print(f'No. of Days: {monthrange(int(year), int(month))[1] + 1}')
print(daysINMonth)

# for m in range(1, int(daysINMonth)+1):
#     print(str(m).zfill(2))

month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
year = now.strftime('%Y')

dirName = []
for m in iter(month):
    # print(f"No. of Days of {str(m).zfill(2)}: {monthrange(int(year), int(m))[1]}")
    daysRange = monthrange(int(year), int(m))[1]
    for d in range(1, daysRange + 1):
        # print(f'{year}{str(m).zfill(2)}{str(d).zfill(2)}')
        dirName.append(f'{year}{str(m).zfill(2)}{str(d).zfill(2)}')

print(dirName)

month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
year = now.strftime('%Y')

yymm = []
yymmdd = []
for m in iter(month):
    yymm.append(f'{year}{str(m).zfill(2)}')
    daysRange = monthrange(int(year), int(m))[1]
    for d in range(1, daysRange + 1):
        yymmdd.append(f'{year}{str(m).zfill(2)}{str(d).zfill(2)}')

# for i in yymm:
#     print(i)

# for i in yymmdd:
#     print(i)

txt = "Hello, welcome to my world."
search_str = input('Enter the string you want to search: ')
x = txt.find(search_str)
print(f'exits at index: {x}')
