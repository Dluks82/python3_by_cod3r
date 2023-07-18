#!/usr/bin/python3
from math import pi


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    radius = input('Enter the radius of your circle (m): ')
    area = circle(radius)
    print(f'The area of your circle is {area} m^2.')
