# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

list_of_numbers = [123, 12333, 3123, 22, 42, 0, -123123, 34, 444, 234]

for number in list_of_numbers:
    if number == 42:
        print('The Answer to the Ultimate Question of Life, the Universe, and Everything')
        break
    if len(str(number)) < 3:
        print number