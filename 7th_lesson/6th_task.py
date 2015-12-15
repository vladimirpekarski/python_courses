# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Find sum of integers')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='Prove N integers for sum')

    return parser.parse_args()


if __name__ == '__main__':
    list_of_elements = parse_args().integers
    print('Sum of elements: {}'.format(sum(list_of_elements)))