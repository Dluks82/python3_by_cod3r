#!/usr/bin/python3

for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

# The continue statement causes the loop to skip the remainder of its body and
# immediately retest its condition prior to reiterating.
# In this case, the loop will skip the print() function call when x is even.
# The continue statement is useful when you want to skip over a loop iteration

for x in range(1, 11):
    if x == 5:
        break
    print(x)

# The break statement causes the loop to terminate immediately.
# In this case, the loop will terminate when x is equal to 5.
# The break statement is useful when you want to terminate a loop prematurely
# when a condition is met.
