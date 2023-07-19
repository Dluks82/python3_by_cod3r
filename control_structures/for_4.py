#!/usr/bin/python3

# for i in range(1, 10):
#     if i == 7:
#         break
#     print(i)
# else:
#     print('The loop is over')

# Challenge
# Random a number from 1 to 6
# For loop with range 1 to 6
# If number is odd, continue
# If number is even and equal to random number, print('You win!') and call break
# Else print('Try again')

from random import randint


def roll_dice():
    return randint(1, 6)


for i in range(1, 7):
    if not i % 2 == 0:
        continue
    if i == roll_dice():
        print(f'You win! The number is {i}')
        break
else:
    print('You lose! Try again.')
