#!/usr/bin/python3

class Human:
    # class attribute
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def from_the_caves(self):
        self.species = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def species():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neanderthal(Human):
    specie = Human.species()[-2]


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    lucas = Neanderthal('Lucas')

    print(f'Evolution (from the class): {", ".join(HomoSapiens.species())}')
    print(f'Evolution (from the instance): {", ".join(jose.species())}')

    print(f'Homo Sapiens evolved? {HomoSapiens.is_evolved()}')

    print(f'Neanderthal evolved? {Neanderthal.is_evolved()}')
