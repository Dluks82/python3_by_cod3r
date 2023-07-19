#!/usr/bin/python3

# Concepts Grades
# Write a program that asks the user for their grade on the last test.

# A     From 10,0 to 9,1
# A-    From 9,0 to 8,1
# B     From 8,0 to 7,1
# B-    From 7,0 to 6,1
# C     From 6,0 to 5,1
# C-    From 5,0 to 4,1
# D     From 4,0 to 3,1
# D-    From 3,0 to 2,1
# E     From 2,0 to 1,1
# E-    From 1,0 to 0,0

# The program should print the grade and the corresponding letter grade.

import sys


def letter(grade):
    if grade > 10 or grade < 0:
        print('The grade must be between 0 and 10.')
    elif grade >= 9.1:
        print(f'Your grade is {grade} and your letter grade is A.')
    elif grade >= 8.1:
        print(f'your grade is {grade} and your letter grade is A-.')
    elif grade >= 7.1:
        print(f'Your grade is {grade} and your letter grade is B.')
    elif grade >= 6.1:
        print(f'Your grade is {grade} and your letter grade is B-.')
    elif grade >= 5.1:
        print(f'Your grade is {grade} and your letter grade is C.')
    elif grade >= 4.1:
        print(f'Your grade is {grade} and your letter grade is C-.')
    elif grade >= 3.1:
        print(f'Your grade is {grade} and your letter grade is D.')
    elif grade >= 2.1:
        print(f'Your grade is {grade} and your letter grade is D-.')
    elif grade >= 1.1:
        print(f'Your grade is {grade} and your letter grade is E.')
    else:
        print(f'Your grade is {grade} and your letter grade is E-.')


def grade(grade):
    letter(grade)


if __name__ == '__main__':
    print(sys.argv)
    print(type(float(sys.argv[1])))
    if len(sys.argv) < 2:
        print('You must pass the grade.')
        print(f'Syntax: {sys.argv[0]}, <grade>')
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        print('The grade must be a number(int).')
        sys.exit(1)
    else:
        grade(float(sys.argv[1]))
