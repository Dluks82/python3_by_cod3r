#!/usr/bin/python3

def all_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    all_params('a', 'b', 'c')
    all_params('a', 'b', 'c', cool=True, value=12.99)
    all_params('Ana', False, [1, 2, 3], size='G', fragile=False)
