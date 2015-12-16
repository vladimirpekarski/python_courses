# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

def check_positive_integer(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError('Proveded number isn\'t positive integer')

check_positive_integer(777)
check_positive_integer(-777)
check_positive_integer(777.132)