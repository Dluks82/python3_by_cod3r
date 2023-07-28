#!/usr/bin/python3

def multiplier(times):
    def calc(x):
        return x * times
    return calc


if __name__ == '__main__':
    double = multiplier(2)
    triple = multiplier(3)

    print(double)
    print(triple)

    print(f'The double of 4 is {double(4)}')
    print(f'The triple of 4 is {triple(4)}')
