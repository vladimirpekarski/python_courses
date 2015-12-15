# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

_number = 23
number_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

def print_number(number):
    word_list = []
    sting_number = str(number)
    for letter in sting_number:
        word_list.append(number_dict[int(letter)])

    word_string = ' '.join(word_list)
    print(word_string)

print_number(766443498767678687687680999)