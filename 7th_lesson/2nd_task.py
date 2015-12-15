# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

price_per_kg = 6.6

for kg in range(1, 11):
    print('Price for {}kg: {}'.format(kg, price_per_kg * kg))