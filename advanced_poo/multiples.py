#!/usr/bin/python3

class Animal:
    @property
    def capacities(self):
        return ('sleep', 'eat', 'drink')


class Man(Animal):
    @property
    def capacities(self):
        return super().capacities + ('love', 'talk', 'study')


class Spider(Animal):
    @property
    def capacities(self):
        return super().capacities + ('make webs', 'walk the walls')


class SpiderMan(Man, Spider):
    @property
    def capacities(self):
        return super().capacities + ('beat up bad guys', 'shoot webs between buildings')


if __name__ == '__main__':
    john = Man()
    print(f'John: {john.capacities}')

    spider = Spider()
    print(f'Spider: {spider.capacities}')

    spiderman = SpiderMan()
    print(f'SpiderMan: {spiderman.capacities}')
