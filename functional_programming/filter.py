#!/usr/bin/python3

people = [
    {'name': 'Diogo', 'age': 41},
    {'name': 'Ana', 'age': 14},
    {'name': 'Diana', 'age': 12},
    {'name': 'Maurício', 'age': 28},
    {'name': 'Joaquim', 'age': 35},
    {'name': 'Eli', 'age': 67},
]

minors = filter(lambda p: p['age'] < 18, people)
print(list(minors))

greater_than_6 = filter(lambda p: len(p['name']) >= 7, people)
print(tuple(greater_than_6))
