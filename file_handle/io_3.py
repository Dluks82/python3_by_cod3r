#! /usr/bin/python3

file = open('people.csv')
for record in file:
    print('Name: {}, Age: {}'.format(
        *record.strip().split(',')))  # strip() remove \n

file.close()
