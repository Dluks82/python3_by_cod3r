#!/usr/bin/python3

from datetime import datetime
from store import Client, Order, Seller


def main():
    client = Client('Diogo Oliveira', 41)
    seller = Seller('Ana Oliveira', 25, 5000)
    order1 = Order(seller, datetime.now(), 512)
    order2 = Order(seller, datetime(2023, 2, 10), 256)
    client.add_order(order1)
    client.add_order(order2)

    print(f'Client: {client}', '(adult)' if client.is_adult() else '')
    print(f'Seller: {seller}')

    total_order = client.total_orders()
    qty_orders = len(client.orders)

    print(f'Total: {total_order} in {qty_orders} orders')
    print(f'Last order: {client.get_last_order_date()}')


if __name__ == '__main__':
    main()
