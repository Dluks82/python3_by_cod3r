#!/usr/bin/python3

class Date:

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


d1 = Date()
d1.day = 5
d1.month = 12
d1.year = 2021
print(d1)

d2 = Date()
d2.day = 15
d2.month = 10
d2.year = 2023
print(d2)
