#!/usr/bin/python3

# Python does not have a switch statement
# We can use a dictionary to simulate a switch statement


def get_week_day(day):
    days = {
        1: {'name': 'Sunday', 'is_weekend': True},
        2: {'name': 'Monday', 'is_weekend': False},
        3: {'name': 'Tuesday', 'is_weekend': False},
        4: {'name': 'Wednesday', 'is_weekend': False},
        5: {'name': 'Thursday', 'is_weekend': False},
        6: {'name': 'Friday', 'is_weekend': False},
        7: {'name': 'Saturday', 'is_weekend': True}
    }
    f = f'{day} is '
    if days.get(day, 'Invalid day') != 'Invalid day':
        f += days[day]['name']
        if days[day]['is_weekend']:
            f += ' and is weekend'
        else:
            f += ' and is not weekend'
    else:
        f += 'Invalid day'
    return f


if __name__ == '__main__':
    for day in range(0, 9):
        print(get_week_day(day))

# From Python 3.10, we can use match statement
# match statement is similar to switch statement
# match statement is more powerful than switch statement
# match statement can be used to compare any data type
# match statement can be used to compare multiple values
# match statement can be used to compare multiple conditions
# match statement can be used to compare multiple conditions with multiple values

# match day:
#     case 2 | 3 | 4 | 5 | 6:
#         print('Weekday')
#     case 1 | 7:
#         print('Weekend')
#     case _:
#         print('Invalid day')
