#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive function

def fibonacci(qtd, result=(0, 1)):

    # Stop condition
    if len(result) == qtd:
        return result

    # sum the last two numbers of the tuple
    return fibonacci(qtd, result + (sum(result[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
