#!/usr/bin/python3

from datetime import datetime


class Todo:
    def __init__(self, description):
        self.description = description
        self.createdAt = datetime.now()
        self.status = False

    def done(self):
        self.status = True

    def __str__(self):
        return f'{self.description} is{"" if self.status else " not"} done'


def main():
    home = []
    home.append(Todo('Clean the house'))
    home.append(Todo('Washing clothes'))
    home.append(Todo('Throw the trash'))

    # Challenge -> conclude 'Washing clothes'

    # for task in home:
    #     if task.description == 'Washing clothes':
    #         task.done()

    # List comprehension
    [task.done() for task in home if task.description ==
     'Washing clothes']  # other solution

    for task in home:
        print(f'Task: {task}')


if __name__ == '__main__':
    main()
