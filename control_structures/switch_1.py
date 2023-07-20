#!/usr/bin/python3

# Python does not have a switch statement
# We can use a dictionary to simulate a switch statement


def get_week_day(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day, 'Invalid day')


if __name__ == '__main__':
    for day in range(0, 9):
        print(get_week_day(day))

# From Python 3.10, we can use match statement

# match day:
#     case 1:
#         print('Sunday')
#     case 2:
#         print('Monday')
#     case 3:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')
#     case 6:
#         print('Friday')
#     case 7:
#         print('Saturday')
#     case _:
#         print('Invalid day')

# match day:
#     case 1 | 7:
#         print('Sunday')
#     case 2:
#         print('Monday')
#     case 3:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')
#     case 6:
#         print('Friday')
#     case _:
#         print('Invalid day')
