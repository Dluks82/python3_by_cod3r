#!/usr/bin/python3

class Car:
    def __init__(self, max_speed=200):
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, delta=5):
        self.current_speed = self.current_speed + \
            delta if self.current_speed + delta <= self.max_speed else self.max_speed
        return self.current_speed

    def brake(self, delta=5):
        self.current_speed = self.current_speed - \
            delta if self.current_speed - delta >= 0 else 0
        return self.current_speed


if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        print(c1.accelerate(8))

    for _ in range(10):
        print(c1.brake(delta=20))
