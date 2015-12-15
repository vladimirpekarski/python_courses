# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Write file by block')
    parser.add_argument('-read', type=str)
    parser.add_argument('-write', type=str)

    return parser.parse_args()

def write_to_file(file_read, file_write, block_size=1024):
    try:
        _file_read = open(file_read)
        _file_write = open(file_write, 'w')
        while True:
            block = _file_read.read(block_size)
            if not block:
                break
            _file_write.write(block)
    except IOError:
        print('Something happens')


if __name__ == '__main__':
    args = parse_args()
    file_read = args.read
    file_write = args.write
    write_to_file(file_read, file_write)