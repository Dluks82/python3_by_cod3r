#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci():
    current, next = 0, 1
    while True:
        current, next = next, current + next
        yield current


if __name__ == '__main__':
    for n in fibonacci():
        print(n, end=', ')
        if n > 2000:
            break
    print()
