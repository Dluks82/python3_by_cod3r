#!/usr/bin/python3

from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):  # __iter__
        return self.tasks.__iter__()

    # operator overload +=
    # project += task
    # home += ...
    def __iadd__(self, task):
        task.owner = self
        self._add_task(task)
        return self

    # Private Methods
    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, description, **kwargs):
        self.tasks.append(Todo(description, kwargs.get('due_date', None)))

    def add(self, task, due_date=None, **kwargs):
        chosen_func = self._add_task if isinstance(task, Todo) \
            else self._add_new_task
        kwargs['due_date'] = due_date
        chosen_func(task, **kwargs)
        pass

    def pending(self):
        return [task for task in self.tasks if not task.status]

    def search(self, description):
        # Possible IndexError
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self) -> str:
        return f'{self.name} ({len(self.pending())}) pending tasks!'


class Todo:
    def __init__(self, description, due_date=None):
        self.description = description
        self.createdAt = datetime.now()
        self.due_date = due_date
        self.status = False

    def done(self):
        self.status = True

    def __str__(self):
        status = []
        if self.status:
            status.append('(done)')
        elif self.due_date:
            if datetime.now() > self.due_date:
                status.append('(overdue)')
            else:
                days = (self.due_date - datetime.now()).days
                status.append(f'(expires in {days} days)')

        return f'{self.description} ' + ' '.join(status)


class RecurringTodo(Todo):
    def __init__(self, description, due_date=None, days=7):
        super().__init__(description, due_date)
        self.days = days
        self.owner = None

    def done(self):
        super().done()
        new_due_date = datetime.now() + timedelta(days=self.days)
        new_task = RecurringTodo(self.description, new_due_date, self.days)
        if self.owner:
            self.owner += new_task
        return new_task


def main():
    home = Project('Home tasks')
    home.add('Washing clothes', datetime.now())
    home.add('Clean the window', datetime.now())

    home += RecurringTodo('Clean the bathroom', datetime.now(), 7)
    home.search('Clean the bathroom').done()

    home.add('Clean the house', datetime.now() + timedelta(days=3, minutes=15))

    print(home)

    home.search('Washing clothes').done()

    for task in home:  # __iter__
        print(f'Task: {task}')

    print(home)


if __name__ == '__main__':
    main()
