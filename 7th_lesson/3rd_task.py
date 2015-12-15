# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

price_per_kg = 6.6
kilo = 1.2

while kilo < 2.0:
    print('Price for {}kg: {}'.format(kilo, price_per_kg * kilo))
    kilo += 0.2
