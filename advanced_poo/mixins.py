#!/usr/bin/python3

class HtmlToStringMixin(object):
    def __str__(self):
        """Html conversion"""
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal(object):
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self) -> str:
        return self.name + (' (pet)' if self.pet else '')


class PersonHtml(HtmlToStringMixin, Person):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    diogo = Person('Diogo')
    print(diogo)

    lucas = PersonHtml('Lucas')
    print(lucas)

    bob = AnimalHtml('Bob')
    print(bob)

    tuce = AnimalHtml('Tuce', False)
    print(tuce)
