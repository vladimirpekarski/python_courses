# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'
import random
import time


def generate_random_list(length):
    print('INFO: Start generate list')
    random_list = []
    for _ in xrange(length):
        random_list.append(random.randrange(0, length))

    print('INFO: Finish generate list')
    # print('INFO: random list', random_list)
    return random_list


def sort_bubble(list_to_sort):
    print('INFO: Start bubble sort')
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp
    print('INFO: Finish bubble sort')
    # print('INFO: sorted list by bubble', list_to_sort)

def standard_search(list_to_sort):
    print('INFO: Start standard sort')
    list_to_sort.sort()
    print('INFO: Finish standard sort')
    # print('INFO: sorted list by standard', list_to_sort)


def get_execution_time(function, quantity_of_elements):
    print('INFO: Start test')
    test_list = generate_random_list(quantity_of_elements)
    start_time = time.time()
    function(test_list)
    finish_time = time.time()
    delta = finish_time - start_time
    print('INFO: Finish test')
    print('=' * 50)

    return delta


def get_average_time(temp_results):
    print('INFO: Start finding average')
    temp_results.remove(max(temp_results))
    temp_results.remove(min(temp_results))
    average = sum(temp_results) / len(temp_results)
    print('INFO: Finish finding average')

    return average


def run_test(function, quantity_of_elements):
    results = []

    for _ in xrange(5):
        results.append(get_execution_time(function,
                                          quantity_of_elements))

    average = get_average_time(results)

    return average


# print(run_test(sort_bubble, 50000))
print(get_execution_time(sort_bubble, 50000))
# print('Standard search {} ms'.format(get_execution_time(standard_search,
#                                                         100)))



