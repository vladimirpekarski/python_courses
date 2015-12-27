# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class SmallStupidList(object):
    MAX_LEN = 3
    def __init__(self, *args):
        if len(args) > self.MAX_LEN:
            raise Exception("Too long list")
        self._internal_list = []
        self._internal_list.extend(args)

    def __str__(self):
        return str(self._internal_list)

    def append(self, x):
        if len(self._internal_list) + 1 > self.MAX_LEN:
            raise Exception("Too long list")
        self._internal_list.append(x)


if __name__ == "__main__":
    l1 = SmallStupidList(1, 2, 3)
    print(l1)
    l1.append(4)