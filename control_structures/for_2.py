#!/usr/bin/python3

word = 'Python'

for letter in word:
    # print(letter)  # default end='\n'
    print(letter, end=',')  # end=',' - print with comma
print('End')

approved = ['Diogo', 'Ana', 'Eli', 'Diana']

for name in approved:
    print(name)

for position, name in enumerate(approved):
    print(f'{position + 1})', name)

weekdays = ('Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday')

for day in weekdays:
    print(f'Today is {day}.')

for letter in set('Python is cool'):  # set() - remove duplicate letters and sort
    print(letter)
