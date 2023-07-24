# **kwargs

def result_f1(first, second, third):
    print(f'1) -> {first}')
    print(f'2) -> {second}')
    print(f'3) -> {third}')


if __name__ == '__main__':
    podium = {'first': 'L. Hamilton',
              'second': 'M. Verstappen',
              'third': 'S. Vettel'}
    result_f1(**podium)
