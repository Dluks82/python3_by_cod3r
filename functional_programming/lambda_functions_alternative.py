#!/usr/bin/python3

def cal_total_price(purchase):
    return purchase['quantity'] * purchase['price']


purchases = (
    {'quantity': 2, 'price': 10},
    {'quantity': 3, 'price': 20},
    {'quantity': 4, 'price': 30}
)

totals = tuple(
    map(
        cal_total_price, purchases
    )
)

print('Total prices:', list(totals))
print('Total', sum(totals))
