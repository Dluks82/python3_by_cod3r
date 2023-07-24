from package1 import module1
from package2 import module1 as module1_sub


print('Sum', module1.sum(1, 2))
print('Sub', module1_sub.sub(2, 1))
