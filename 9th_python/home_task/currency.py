# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Currency(object):
    """
    >>> curr = Currency(Currency.GOLD_ID, 'Gold')
    >>> curr.cur_type
    1
    >>> curr.name
    'Gold'
    >>> curr.value
    100
    """
    GOLD_ID = 1
    SILVER_ID = 2
    BRONZE_ID = 3

    def __init__(self, cur_type, name, value=100):
        self.cur_type = cur_type
        self.name = name
        self.value = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
