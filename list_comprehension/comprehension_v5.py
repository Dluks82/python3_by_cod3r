dictionary = {i: i * 3 for i in range(1, 11) if i % 2 == 0}

for number, triple in dictionary.items():
    print(f'{number} * 3 = {triple}')
