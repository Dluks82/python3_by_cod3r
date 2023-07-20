#!/usr/bin/python3

def print_recursively(max, current):
    if current >= max:
        return
    print(current)
    print_recursively(max, current + 1)


if __name__ == '__main__':
    print_recursively(10, 0)
