# [expression for item in list]

# List comprehension
double = [i * 2 for i in range(1, 11)]
print(double)

# Normal version
double = []
for i in range(1, 11):
    double.append(i * 2)

print(double)
