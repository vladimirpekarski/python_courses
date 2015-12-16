# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

def generate_exception(number):
    value = int(number)
    str_value = 'str' + number


try:
    generate_exception('asd')
finally:
    print('FINALLY')

try:
    generate_exception(2222)
finally:
    print('FINALLY')

try:
    generate_exception(88/0)
finally:
    print('FINALLY')