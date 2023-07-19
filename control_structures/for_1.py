#!/usr/bin/python3

for i in range(1, 11):  # the last number is not included
    print(f'i = {i}')

for j in range(10):
    print(f'j = {j}')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x*y}')
