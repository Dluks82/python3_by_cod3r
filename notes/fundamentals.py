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

# Unary operators
