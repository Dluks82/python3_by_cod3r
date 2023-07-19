#!/usr/bin/python3
from math import pi
import sys
import errno


class TerminalColor:
    """Terminal colors"""
    ERR = '\033[91m'  # red
    NORMAL = '\033[0m'  # normal


def help():
    print('You must pass the radius of the circle.')
    # sys.argv[0] is the name of the script
    print(f'Syntax: {sys.argv[0]} <radius>')


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERR + 'The radius must be a number(integer).' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print(f'The area of your circle is {area} m^2.')
        print(dir())
