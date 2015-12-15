# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

def all_price(price_by_kg, kgs):
    price = int(price_by_kg * kgs)
    print('Price for {}kg: {}'.format(kgs, price))

all_price(23.123, 4)