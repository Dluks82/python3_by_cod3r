#!/usr/bin/python3

def log(function):
    def decorator(*args, **kwargs):
        print(f'Start of function call: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        result = function(*args, **kwargs)
        print(f'Call result: {result}')
        return result
    return decorator


@log
def sum(x, y):
    return x+y


@log
def sub(x, y):
    return x-y


if __name__ == '__main__':
    print(sum(2, 5))
    print(sub(7, y=2))
