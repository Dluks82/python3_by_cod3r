#!/usr/bin/python3

from datetime import datetime


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):  # __iter__
        return self.tasks.__iter__()

    def add(self, description):
        self.tasks.append(Todo(description))

    def pending(self):
        return [task for task in self.tasks if not task.status]

    def search(self, description):
        # Possible IndexError
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self) -> str:
        return f'{self.name} ({len(self.pending())}) pending tasks!'


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
    home = Project('Home tasks')
    home.add('Washing clothes')
    home.add('Clean the house')

    print(home)

    home.search('Washing clothes').done()

    for task in home:  # __iter__
        print(f'Task: {task}')

    print(home)


if __name__ == '__main__':
    main()
