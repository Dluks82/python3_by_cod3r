#!/usr/bin/python3

class Date:

    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


d1 = Date(5, 12, 2021)
# d1.day = 5
# d1.month = 12
# d1.year = 2021
print(d1)

d2 = Date(year=2023, month=12)
d2.day = 15
# d2.month = 10
# d2.year = 2023
print(d2)
