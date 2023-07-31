#!/usr/bin/python3

from calendar import mdays, month_name


print('Months with 31 days:')
for month in range(1, len(month_name)):
    if mdays[month] == 31:
        print(f'- {month_name[month]}')
