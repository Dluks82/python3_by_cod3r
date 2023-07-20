#! /usr/bin/python3

with open('people.csv') as file:
    with open('people.txt', 'w') as output:

        for record in file:
            person = record.strip().split(',')

            print('Name: {}, Age: {}'.format(*person), file=output)

if file.closed:
    print('File is closed')

if output.closed:
    print('Output is closed')
