# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Find substring')
    parser.add_argument('-f1', type=str)
    parser.add_argument('-f2', type=str)
    parser.add_argument('--set_mode', type=str)

    return parser.parse_args()

def read_file(_file):
    contant = open(_file).read()
    list_of_number = contant.split(' ')
    for index, value in enumerate(list_of_number):
        list_of_number[index] = int(value)

    return list_of_number


def print_intersection(first_list, second_list):
    s1 = set(first_list)
    s2 = set(second_list)
    print(s1.intersection(s2))


def print_union(first_list, second_list):
    s1 = set(first_list)
    s2 = set(second_list)
    print(s1.union(s2))


def print_substraction(first_list, second_list):
    s1 = set(first_list)
    s2 = set(second_list)
    print(s1.difference(s2))

if __name__ == '__main__':
    args = parse_args()
    first_file = args.f1
    second_file = args.f2
    mode = args.set_mode

    first_list = read_file(first_file)
    second_list = read_file(second_file)

    if mode == 'intersection':
        print_intersection(first_list, second_list)
    elif mode == 'union':
        print_union(first_list, second_list)
    elif mode == 'substraction':
        print_substraction(first_list, second_list)
