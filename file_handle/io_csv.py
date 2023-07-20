#! /usr/bin/python3
import csv

with open('people.csv') as input:
    for person in csv.reader(input):
        print('Name: {}, Age: {}'.format(*person))

if input.closed:
    print('Input is closed')
