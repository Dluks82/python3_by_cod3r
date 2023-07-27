#!/usr/bin/python3

from abc import ABCMeta, abstractproperty

# experimental feature abstract class


class Human(metaclass=ABCMeta):
    # class attribute
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def intelligent(self):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age must be a positive value.')
        self._age = age

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

    @property
    def intelligent(self):
        return False


class HomoSapiens(Human):
    specie = Human.species()[-1]

    @property
    def intelligent(self):
        return True


if __name__ == '__main__':

    # try:
    #     anonymous = Human('John Doe')
    #     print(anonymous.intelligent)
    # except TypeError:
    #     print('abstract class.')

    jose = HomoSapiens('José')
    print('{} of class {}, intelligent: {}'.format(
        jose.name, jose.__class__.__name__, jose.intelligent))

    lucas = Neanderthal('Lucas')
    print('{} of class {}, intelligent: {}'.format(
        lucas.name, lucas.__class__.__name__, lucas.intelligent))
