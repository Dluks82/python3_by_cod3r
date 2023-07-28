#!/usr/bin/python3

from first_class_function import double, square


def process(title, list, function):
    print(f'Processing {title}')
    for i in list:
        print(i, '->', function(i))


if __name__ == '__main__':
    process('Double from 1 to 10', range(1, 11), double)
    process('Square from 1 to 10', range(1, 11), square)
