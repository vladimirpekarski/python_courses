# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Convert number')
    parser.add_argument('-num')

    return parser.parse_args()

def convert_number(number):
    try:
        print(hex(number))
        print(oct(number))
        print(bin(number))
    except TypeError:
        print('Error: invalid number {}'.format(number))

if __name__ == '__main__':
    args = parse_args()
    number = args.num
    convert_number(number)