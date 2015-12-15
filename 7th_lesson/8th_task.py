# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

def custom_sum(*args):
    return sum(args)

print(custom_sum(21, 4124, 2, 44444, 11111111, 4))
print(custom_sum(11111111, 4))
print(custom_sum(21))
print(custom_sum())