#! /usr/bin/python3

file = open('people.csv')
for record in file:
    # * unpacks the list into two arguments
    print('Name: {}, Age: {}'.format(*record.split(',')))

file.close()
