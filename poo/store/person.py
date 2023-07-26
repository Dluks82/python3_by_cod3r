OVER_AGE = 18


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        if not self.age:
            return self.name

        return f'Name: {self.name} ({self.age}) years old.'

    def is_adult(self):
        return (self.age or 0) > OVER_AGE
