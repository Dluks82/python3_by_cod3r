from .person import Person


def get_date(order):
    return order.date


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_last_order_date(self):
        return None if not self.orders else \
            sorted(self.orders, key=get_date)[-1].date

    def total_orders(self):
        total = 0
        for order in self.orders:
            total += order.value
        return total
