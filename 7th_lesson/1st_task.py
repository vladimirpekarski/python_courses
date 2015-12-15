# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'


a = 90000000
b = -8888
c = 5000000

list_max = [a, b, c]

def find_max(_a, _b , _c):
    _min = _a
    if _min > _b:
        _min = _b
    elif _min > _c:
        _min = _c

    return _min

list_max.remove(find_max(a, b, c))

print(sum(list_max))


