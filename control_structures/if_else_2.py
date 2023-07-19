#!/usr/bin/python3

def age_range(age):
    if 0 <= age < 18:
        return 'You are a minor.'
    elif 18 <= age < 65:
        return 'You are an adult.'
    elif age >= 65:
        return 'You are a senior.'
    else:
        return 'Invalid age.'


if __name__ == '__main__':
    for age in (16, 33, 88, -1):
        print(f'Age: {age} - {age_range(age)}')
