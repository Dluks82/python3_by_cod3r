#!/usr/bin/python3

product = {'name': 'MacBook Pro', 'price': 1350.00,
           'imported': True, 'stock': 10}

for key in product:  # iterates over the keys
    print(key)

for value in product.values():  # values() returns a list of values
    print(value)

for key, value in product.items():  # items() returns a list of tuples
    print(key, '=', value)

# Obs.: variables are available after the loop

print(key, value)
