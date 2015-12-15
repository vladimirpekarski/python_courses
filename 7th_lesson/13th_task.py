# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

tuple_number = (123, 32, 12, 11, 222, 44, 555, 666, 7, 234)

def remove_odd(numbers):
    even_number = [x for x in numbers if x % 2 == 0]
    return tuple(even_number)

print(remove_odd(tuple_number))
print(type(remove_odd(tuple_number)))