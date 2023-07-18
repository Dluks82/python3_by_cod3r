#!/usr/bin/python3
from math import pi


def circle(radius):
    print('Circ area:', pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Enter the radius of your circle (m): ')
    circle(radius)
