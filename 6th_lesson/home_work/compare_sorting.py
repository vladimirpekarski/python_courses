# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse
import random
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='Comparing standard python sort method versus bubble sort')
    parser.add_argument('integers', metavar='N', type=int, nargs=5,
                        help='Provide 5 integers value for quantities.')

    return parser.parse_args()

def generate_random_list(length):
    random_list = []
    for _ in xrange(length):
        random_list.append(random.randrange(0, length))

    return random_list


def sort_bubble(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp


def standard_search(list_to_sort):
    list_to_sort.sort()


def get_execution_time(function, quantity_of_elements):
    test_list = generate_random_list(quantity_of_elements)
    start_time = time.time()
    function(test_list)
    finish_time = time.time()
    delta = finish_time - start_time

    return delta


def get_average_time(temp_results):
    temp_results.remove(max(temp_results))
    temp_results.remove(min(temp_results))
    average = sum(temp_results) / len(temp_results)

    return average


def run_test(function, quantity_of_elements):
    results = []
    for _ in xrange(5):
        results.append(get_execution_time(function,
                                          quantity_of_elements))
    average = get_average_time(results)
    print('...Test for {}({}) has finished in {} sec'.
          format(function.__name__, quantity_of_elements, average))

    return average


def run_package_test(function, _list_of_elements):
    results = []
    for _quantity in _list_of_elements:
        results.append([_quantity, run_test(function, _quantity)])

    return results


def print_results(results):
    for result in results:
        print('[{}]: {} sec'.format(result[0], result[1]))


if __name__ == '__main__':
    list_of_elements = parse_args().integers
    print('Bubbles sort test:')
    bubble_results = run_package_test(sort_bubble, list_of_elements)

    print('Standard sort test:')
    standard_results = run_package_test(standard_search,
                                        list_of_elements)

    print('Bubble sort results:')
    print_results(bubble_results)

    print('Standard sort results:')
    print_results(standard_results)

