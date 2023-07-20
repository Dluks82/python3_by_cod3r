#! /usr/bin/python3

with open('people.csv') as file:
    for record in file:
        # IndexError: Replacement index 1 out of range for positional args tuple
        print('Name: {}, Age: {}'.format(
            *record.strip().split(',')))

if file.closed:
    print('File is closed')
