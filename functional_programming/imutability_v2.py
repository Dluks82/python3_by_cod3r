#!/usr/bin/python3

from calendar import mdays, month_name
from functools import reduce


def month_31(month): return mdays[month] == 31


def get_month_name(month): return month_name[month]


def together(all, month_name): return f'{all}\n- {month_name}'


print(reduce(together, map(get_month_name, filter(
    month_31, range(1, len(month_name)))), 'Months with 31 days:'))
