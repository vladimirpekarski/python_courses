# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

list_test = [321, 44, 55, 5, 1, 0, 44, 12]

def print_numbers(list_of_number):
    for number in list_of_number:
        if number % 2 == 0:
            print('An even number: {}'.format(number))
        else:
            print('An odd number: {}'.format(number))


print_numbers(list_test)