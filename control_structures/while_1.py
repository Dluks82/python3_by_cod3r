#!/usr/bin/python3

# while True:
#     print("Infinite loop")

from random import randint

tip_number = -1
secret_number = randint(0, 9)

while tip_number != secret_number:
    tip_number = int(input("Guess the secret number (between 0 and 9): "))

# print("You got it! The secret number was: {}".format(secret_number))
print(f'You got it! The secret number was: {secret_number}')
