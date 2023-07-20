#!/usr/bin/python3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive function

def fibonacci(qtd, result=(0, 1)):
    return result if len(result) == qtd else \
        fibonacci(qtd, result + (sum(result[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
