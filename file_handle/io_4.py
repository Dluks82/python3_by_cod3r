#! /usr/bin/python3

try:
    file = open('people.csv')
    for record in file:
        # IndexError: Replacement index 1 out of range for positional args tuple
        print('Name: {}, Age: {}'.format(
            record.strip().split(',')))

finally:
    print('Closing file')
    file.close()

if file.closed:
    print('File is closed')
