# First examples

print('First Program...')
print(1 + 2)
print(1 /
      + 2)

# Basic types

print(True)
print(False)
print(1.2+1)
print('String')
print("String")
print('You are ' + 3 * 'very ' + 'cool')
# print(3 + '3') TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([1, 2, 3])
print({'name': 'Diogo', 'age': 41})
print(None)

# Variables

a = 20
b = 4.5

print(a+b)

a = 'Now I am a string'
print(a)

# print(a + b) # TypeError: can only concatenate str (not "float") to str

# Comments

# This is a comment
print('After comment')

'''
This is a
multi-line
comment
'''

print('After multi-line comment')

salary = 5000.50
expenses = 2850.20
print(salary - expenses)

print('end')

# Arithmetic operators

print(5+3)
print(5-2)
print(2*3.15)
print(8/4)
print(8//3)
print(8 % 3)
print(2**8)


# Challenge - Calculate percentual of expenses
salary = 5000.0
expenses = 3000.0

percentual = (expenses / salary) * 100

print(percentual, '%')

# Relational operators

print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)
print(1 == 2)
print(1 != 2)
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 != 2)
print(1 == 1 or 2 != 2)
print(not 1 == 1)

# Assignment operators

a = 5
a = a + 8
print(a)
a += 9
print(a)
a -= 4
print(a)
a *= 2
print(a)
a /= 4
print(a)
a %= 4
print(a)
a **= 8
print(a)
a //= 256
print(a)

# Logical operators

print(True or False)
print(False or False)
print(True and True)
print(not True)
print(not False)
print(not 0)
print(not 1)
print(1 > 2 and 2 < 3)
print(1 > 2 or 2 < 3)
print(1 > 2 or 2 == 3 and 3 > 2)
print(1 > 2 and 2 == 3 or 3 > 2)
print(1 > 2 and (2 == 3 or 3 > 2))
print(1 > 2 or 2 == 3 and 3 > 2)
print(1 != 2 and 10 > 2 and 2 == 2)

# Caution - Logical operators and bitwise operators
True & True
False | True
True ^ False

# 3 = 11
# 2 = 10
# 1 = 01
# 0 = 00

# 3 & 2 = 10
# 2 | 1 = 11
# 3 ^ 2 = 01

# Example
balance = 100
salary = 5000
expenses = 3000

balance_positive = balance > 0
expenses_controlled = salary - expenses >= 0.2 * salary

print('Expenses controlled::', balance_positive and expenses_controlled)

# Challenge -
# 1. Work on the morning and afternoon
# 2. The TV is on
# 3. Buy an ice cream
work_morning = False
work_afternoon = False

tv_50 = work_morning and work_afternoon
tv_32 = work_morning != work_afternoon

ice_cream = work_morning or work_afternoon
healthy = not ice_cream

print('TV 50: {} TV 32: {} Ice Cream: {} Healthy: {}'.format(
    tv_50, tv_32, ice_cream, healthy))


# Unary operators

a = 5
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 1
print(a)
a %= 3
print(a)
a **= 5
print(a)
a //= 3
print(a)
a = -a
print(a)
a = +a
print(a)

# Ternary operator

logged_user = True

msg = 'User logged.' if logged_user else 'User needs to log in.'
msg2 = 'User logged: ' + ('No!', 'Yes!')[logged_user]
print(msg)
print(msg2)
