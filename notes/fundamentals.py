# First examples

from string import Template
from decimal import Decimal, getcontext

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

# Membership operators

print(2 in [1, 2, 3])
print(2 not in [1, 2, 3])
print('py' in 'Python')
print('py' not in 'Python')

# Identity operators

x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(x is not z)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b)
print(list_b is list_c)
print(list_a is not list_c)
print(list_a == list_c)

# Built-in functions

print(type(1))
print(__builtins__.type('Hey guys!'))
print(1+2)
print(__builtins__.dir())

# Type conversion

print(2 + 3)
print('2' + '3')
# print(2 + '3') TypeError: unsupported operand type(s) for +: 'int' and 'str'

a = 10
b = '5'

print(type(a))
print(type(b))

print(a + int(b))

print(str(a) + b)

print(type(str(a)))

print(2 + float('3.4'))

# print(2 + int('3.4')) ValueError: invalid literal for int() with base 10: '3.4'

print(2 + int(float('3.4')))
print(2 + int('3'))

# print(2 + int('3.4')) ValueError: invalid literal for int() with base 10: '3.4'

print(2 + float('3'))

# print(2 + float('3.4')) ValueError: could not convert string to float: '3.4'

print(2 + float('3.4'))

print(2 + int(True))
print(2 + int(False))
print(2 + float(True))
print(2 + float(False))
print(str(True))
print(str(False))
print(bool(''))
print(bool(0))
print(bool(-2))
print(bool(None))
print(bool(' '))
print(bool('abc'))

# Automatic type conversion

print(10/2)
print(type(10/2))
print(10/3)
print(type(10/3))
print(10//3)
print(type(10//3))
print(10//3.3)
print(type(10//3.3))
print(10/2.5)
print(type(10/2.5))
print(2+True)
print(type(2+True))
print(2+False)
print(type(2+False))
print(2+0.5)
print(type(2+0.5))
print(2+0)
print(type(2+0))
# print(2+'3') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(type(2+'3')) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(2*'3')
print(type(2*'3'))

# Numeric types

print(dir(int))
print(dir(float))

a = 7
b = 3.2

print(type(a))
print(type(b))
print(type(a+b))

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(2, 3))
print((-2).__abs__())

print((-3.6).__abs__())

# Decimal

print(1.1 + 2.2)


getcontext().prec = 10

print(Decimal(1.1) + Decimal(2.2))
print(Decimal(1) / Decimal(7))

print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))

print(dir(Decimal))

# String
print("String")
print(dir(str))

name = 'Diogo'
print(name)
print(name[0])
print(name[4])
# print(name[5]) IndexError: string index out of range
print(name[-1])
print(name[-5])
# print(name[-6]) IndexError: string index out of range

print(name[0:2])
print(name[2:4])
print(name[:4])
print(name[2:])
print(name[-2:])
print(name[:-2])
print(name[:])
print(name[::2])
print(name[::-1])
print(name[::-2])

# whater mark
print("Luks \"Nunes\"" == 'Luks "Nunes"')
print('Text with \n line break')
print(r'Text with \n line break')

print("""\
Text with
line break""")

print("""\
Text with
    line break""")

print('Text with' + '\n' + 'line break')

print('Text with\nline break')

print('Text with\n\tline break')

# List

print(dir(list))

empty_list = []

list_a = [1, 2, 3]

print(list_a)
print(type(list_a))
print(len(list_a))
print(list_a[0])
print(list_a[1])
print(list_a[2])

# print(list_a[3]) IndexError: list index out of range

print(list_a[-1])
print(list_a[-2])
print(list_a[-3])

# print(list_a[-4]) IndexError: list index out of range

list_a[0] = 'Now I am a string'
print(list_a)

list_a[0] = 1
print(list_a)

list_a.append(4)
print(list_a)

list_a.append([5, 6])
print(list_a)

list_a.remove(2)
print(list_a)

list_a.extend([7, 8, 9])
print(list_a)

list_a.insert(0, 0)
print(list_a)

list_a.pop()
print(list_a)

list_a.pop(0)
print(list_a)

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_a)

del (list_a[1:3])
print(list_a)

del (list_a[0])
print(list_a)

list_a.reverse()
print(list_a)

print(list_a[::-1])

print(list_a.index(5))

print(list_a.index(9))

# print(list_a.index(10)) ValueError: 10 is not in list

print(list_a[2:5])

print(list_a[2:])
print(list_a[:5])
print(list_a[:])

print(list_a[::2])
print(list_a[::-1])

print(list_a)
print(list_a * 2)

print(2 in list_a)
print(10 in list_a)
print(10 not in list_a)

list_a = ['Diogo', 'Luks', 'Nunes']
print(list_a)

print(list_a[0])
print(list_a[1])
print(list_a[2])

print(list_a[-1])

print(list_a[0][0])

list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_a)

print(list_a[0])

print(list_a[0][0])

print(list_a[1][2])

print(list_a[2][1])

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_a)

print(list_a[1:4])


# Tuple

tuple_a = tuple()
tuple_a = ()
print(tuple_a)
print(type(tuple_a))

print(dir(tuple))

tuple_a = ('One element')
print(tuple_a)
print(type(tuple_a))

tuple_a = ('One element',)

print(tuple_a)
print(type(tuple_a))

tuple_a = ('One', 'Two', 'Three')
print(tuple_a)
print(type(tuple_a))

print(tuple_a[0])
print(tuple_a[1])
print(tuple_a[2])

# tuple_a[0] = 1 TypeError: 'tuple' object does not support item assignment

print(tuple_a[1:])
print(tuple_a[:-1])
print(tuple_a[:])

print(tuple_a + tuple_a)
print(tuple_a * 2)

print(3 in tuple_a)
print('Three' in tuple_a)
print('Four' not in tuple_a)

tuple_b = tuple_a
print(tuple_a is tuple_b)
print(tuple_a == tuple_b)

tuple_b = tuple_a + tuple_a
print(tuple_a is tuple_b)
print(tuple_a == tuple_b)

tuple_a, tuple_b = (1, 2, 3), (4, 5, 6)
print(tuple_a)
print(tuple_b)

tuple_a, tuple_b = tuple_b, tuple_a
print(tuple_a)
print(tuple_b)

# Dictionary

print(dir(dict))

dict_a = {}
print(dict_a)
print(type(dict_a))

dict_a = dict()
print(dict_a)
print(type(dict_a))

dict_a = {'key1': 'value1', 'key2': 'value2'}
print(dict_a)
print(type(dict_a))

print(dict_a['key1'])
print(dict_a['key2'])

# print(dict_a['key3']) KeyError: 'key3'

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)
print(type(dict_a))

dict_a['key4'] = 'value4'
print(dict_a)

dict_a['key4'] = 'value5'
print(dict_a)

del dict_a['key4']
print(dict_a)

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)

print('key1' in dict_a)
print('key4' in dict_a)
print('key4' not in dict_a)

print('value1' in dict_a)
print('value4' in dict_a)
print('value4' not in dict_a)

print(len(dict_a))

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print(dict_a.get('key1'))
print(dict_a.get('key4'))
print(dict_a.get('key4', 'Not found!'))

print(dict_a)

print(dict_a.pop('key1'))
print(dict_a)

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)

print(dict_a.popitem())
print(dict_a)

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)

dict_a.update({'key4': 'value4'})
print(dict_a)

dict_a.update({'key1': 'value5'})
print(dict_a)

dict_a.update({'key1': 'value5', 'key5': 'value5'})
print(dict_a)

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)

dict_a.clear()
print(dict_a)

dict_a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dict_a)

dict_b = dict_a
print(dict_a)
print(dict_b)

dict_b['key1'] = 'value5'
print(dict_a)
print(dict_b)

dict_b = dict_a.copy()
print(dict_a)
print(dict_b)

dict_b['key1'] = 'value6'
print(dict_a)
print(dict_b)

del dict_b['key1']
print(dict_a)
print(dict_b)


# Set

print(dir(set))

set_a = set()
print(set_a)
print(type(set_a))

set_a = {1, 2, 3}
print(set_a)

set_a = {1, 2, 3, 3, 3, 3, 3, 3, 3}
print(set_a)

set_a.add(4)
print(set_a)

set_a.remove(4)
print(set_a)

set_a.discard(3)
print(set_a)

# set_a.remove(3) KeyError: 3

set_a = {1, 2, 3}
print(set_a)

set_a.update({4, 5, 6})
print(set_a)

set_a.pop()
print(set_a)

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
print(c1)

c1.update(c2)
print(c1)

c1 -= {2}
print(c1)

c1 = {1, 2}
c2 = {2, 3}
print(c1)
print(c2)

print(c1 - c2)
print(c2 - c1)

c1 -= {2}
print(c1)


# Interpolation

name, age = 'Diogo', 41
# s = string, d = decimal, f = float, r = raw, a = ascii, e = exponential, g = general, o = octal, x = hexadecimal
print('Name: %s Age: %d' % (name, age))  # Old way
print('Name: {0} Age: {1}'.format(name, age))  # Python 3
print(f'Name: {name} Age: {age}')  # Python 3.6

print(f'2 + 2 = {2 + 2}')

print(f'Name: {name} Age: {age + 2}')

print(f'Name: {name.lower()} Age: {age + 2}')


# Template

s = Template('Name: $name Age: $age')
print(s.substitute(name=name, age=age))
