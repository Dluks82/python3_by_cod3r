#!/usr/bin/python3

class SimpleClass:
    counter = 0

    def __init__(self):
        self.count()

    # or
    # def __init__(self):
    #     self.__class__.counter += 1

    @classmethod
    def count(cls):
        cls.counter += 1


if __name__ == '__main__':
    list = [SimpleClass(), SimpleClass()]
    print(SimpleClass.counter)  # Expected 2
