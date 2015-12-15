# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'


list_of_numbers = [123, 12333, 3123, 22, 42, 0, -123123, 34, 444, 234]

for number in list_of_numbers:
    if number % 13 != 0:
        continue
    else:
        print(number)