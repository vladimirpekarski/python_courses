# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Find substring')
    parser.add_argument('-path', type=str)
    parser.add_argument('-pattern', type=str)

    return parser.parse_args()

def print_string_with_pattern(file_path, pattern):
    for line in open(file_path):
        if pattern in line:
            print(line.strip())


if __name__ == '__main__':
    args = parse_args()
    path = parse_args().path
    pattern = parse_args().pattern
    print_string_with_pattern(path, pattern)
