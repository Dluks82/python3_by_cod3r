def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a+b+c


def sum_n(*numbers):
    # print(type(numbers))
    sum = 0
    for n in numbers:
        sum += n

    return sum


if __name__ == '__main__':
    print(sum_2(23, 7))
    print(sum_3(3, 6, 9))
    print(sum_n(2))
    print(sum_n(2, 6, 5))
    print(sum_n(2, 6, 5, 7, 4, 10))
