# [expression for item in list if conditional]

# List comprehension
double_of_odd = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(double_of_odd)

# Normal version
double_of_odd = []
for i in range(1, 11):
    if i % 2 == 0:
        double_of_odd.append(i * 2)

print(double_of_odd)
