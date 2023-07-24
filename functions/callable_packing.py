#!/usr/bin/python3

def calc_final_price(init_price, cal_tax, *params):  # packing
    return init_price + init_price * cal_tax(*params)  # unpacking


def tax_x(imported):
    return 0.22 if imported else 0.13


def tax_y(explosive, mult_factor=1):
    return 0.11 * mult_factor if explosive else 0


if __name__ == '__main__':
    init_price = 134.98
    final_price = calc_final_price(init_price, tax_x, True)
    final_price = calc_final_price(final_price, tax_y, True, 1.5)
    print(f'Final price US$ {final_price}')
