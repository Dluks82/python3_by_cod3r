#!/usr/bin/python3
from math import pi
import sys


def help():
    print('You must pass the radius of the circle.')
    # sys.argv[0] is the name of the script
    print(f'Syntax: {sys.argv[0]} <radius>')


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    # else:
    radius = sys.argv[1]
    area = circle(radius)
    print(f'The area of your circle is {area} m^2.')
