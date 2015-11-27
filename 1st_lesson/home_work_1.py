__author__ = 'vladimir.pekarsky'

import random

def generate_random_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, 500))

    return random_list

def count_odd_index_sum(list_length=20):
    s = 0
    random_list = generate_random_list(list_length)
    if not random_list:
        return s

    for index, value in enumerate(random_list):
        if index % 2 != 0:
            s += value

    return s * random_list[-1]

print(count_odd_index_sum())
