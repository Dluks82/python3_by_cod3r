#!/usr/bin/python3

def run(function):
    if callable(function):
        function()


def gm():
    print('Good Morning!')


def ga():
    print('Good Afternoon!')


def gn():
    print('Good Night!')


if __name__ == '__main__':
    run(gm)
    run(ga)
    run(gn)
    run(1)
