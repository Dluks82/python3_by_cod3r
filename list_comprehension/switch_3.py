def get_day_type(day):
    days = {
        (1, 7): 'Weekend day',
        tuple(range(2, 7)): 'Week day'
    }
    chosen = (day_type for numbers,
              day_type in days.items() if day in numbers)
    return next(chosen, '** Invalid day **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_day_type(day)}')
