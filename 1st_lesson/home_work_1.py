__author__ = 'vladimir.pekarsky'

import random

def generate_random_list(length=20):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, 500))

    return random_list

def count_odd_index_sum(test_list):
    s = 0
    if not test_list:
        return s

    for index, value in enumerate(test_list):
        if index % 2 != 0:
            s += value

    return s * test_list[-1]

print(count_odd_index_sum([0, 1, 2, 3, 4, 5]))
print(count_odd_index_sum([]))
print(count_odd_index_sum(generate_random_list()))
