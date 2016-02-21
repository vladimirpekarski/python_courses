# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'


# bubble sort

def bubble_sort(some_list):
    for i in range(len(some_list) - 1):
        for j in range(len(some_list) - 1 - i):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]

# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16

def is_power_of_two(number):
    if number < 0:
        return False

    if number == 0:
        return True

    while number % 2 == 0:
        number /= 2

    return number == 1

# count brackets
# () - correct
# )( - incorrect
# (())() - correct
# (()))( - incorrect

def is_correct_brackets(some_string):
    stack = ['']
    brackets = {'(': ')'}
    for character in some_string:
        if character in brackets:
            stack.append(brackets[character])
        else:
            if character in brackets.values() and character != stack.pop():
                return False

    return stack == ['']

# c = '(()))('
# print(is_correct_brackets(c))


# 2 max
def two_max(some_list):
    max_value = some_list[0]
    before_max = some_list[1]
    for i in range(2, len(some_list)):
        if some_list[i] > max_value:
            max_value = some_list[i]
        elif before_max < some_list[i] < max_value:
            before_max = some_list[i]

    return before_max, max_value


# some_list = [123123123, 123123123, 123123123, 123123123, 123123123, 123123123, 123123123, 123123123, 123123123, 123123123, 123123123]
# print(two_max(some_list))


# 0 1 1 2 3 5 8 13 21
def fib_up_to_n(n):
    a, b = 0, 1
    while a < n:
        print('INFO: {}'.format(a))
        a, b = b, a + b

def n_element_of_feb(n):
    s = 0
    a, b = 0, 1
    for i in range(n):
        s += a
        print('Number {}: {}'.format(i + 1, a))
        a, b = b, a + b

    return s


# fact
# 1 * 2 * 3 * 4 * 5 * 6
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

print(fact(10))
