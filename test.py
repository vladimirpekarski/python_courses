# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]


def is_power_two(number):
    if number < 0:
        return False
    elif number == 0:
        return True

    while number % 2 == 0:
        number /= 2
    else:
        if number == 1:
            return True
        else:
            return False

# for valuer in [2 ** x for x in range(10)]:
#     print(is_power_two(valuer))


def brackets(data):
    stack = ['']
    bracker = {'(': ')', '[': ']', '{': '}'}
    for c in data:
        if c in bracker:
            stack.append(bracker[c])
        elif c in bracker.values() and c != stack.pop():
            return False

    return stack == ['']

