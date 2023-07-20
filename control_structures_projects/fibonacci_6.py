#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(qtd):
    result = [0, 1]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == qtd:
            break
    return result


if __name__ == '__main__':
    for n in fibonacci(20):
        print(n)
