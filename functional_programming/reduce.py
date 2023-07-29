#!/usr/bin/python3
from functools import reduce

people = [
    {'name': 'Diogo', 'age': 41},
    {'name': 'Ana', 'age': 14},
    {'name': 'Diana', 'age': 12},
    {'name': 'Maurício', 'age': 28},
    {'name': 'Joaquim', 'age': 35},
    {'name': 'Eli', 'age': 67},
]

only_ages = map(lambda p: p['age'], people)
minors = filter(lambda age: age < 18, only_ages)

sum_age = reduce(lambda ages, age: ages + age, minors, 0)

print(sum_age)
