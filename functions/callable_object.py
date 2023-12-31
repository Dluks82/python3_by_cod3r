#!/usr/bin/python3

class Power:

    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, base):
        return base ** self.exponent


if __name__ == '__main__':
    square = Power(2)
    cube = Power(3)

    if callable(square) and callable(cube):
        print(f'3^2 = {square(3)}')
        print(f'2^3 = {cube(2)}')
        print(Power(4)(2))
