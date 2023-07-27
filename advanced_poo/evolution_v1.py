#!/usr/bin/python3

class Human:
    # class attribute
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def from_the_caves(self):
        self.species = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Human('José')
    cavernoso = Human('Cavernoso').from_the_caves()
    # cavernoso.from_the_caves()

    print(f'Human species: {Human.species}')
    print(f'jose.species: {jose.species}')
    print(f'cavernoso.species: {cavernoso.species}')
