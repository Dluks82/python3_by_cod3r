#!/usr/bin/python3

def fibonacci(seq=[0, 1]):  # mutable object
    seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == '__main__':
    start = fibonacci()
    print(start, id(start))
    print(fibonacci(start))
    restart = fibonacci()  # trap
    print(restart, id(restart))
    assert restart == [0, 1, 1]  # AssertionError
