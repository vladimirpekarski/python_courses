# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(
        description='Date diff')
    parser.add_argument('-d1', type=str)
    parser.add_argument('-d2', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    first_date = parse_args().d1
    second_date = parse_args().d2
    date_1 = datetime.strptime(first_date, '%Y-%m-%d')
    date_2 = datetime.strptime(second_date, '%Y-%m-%d')

    print (date_2 - date_1)
