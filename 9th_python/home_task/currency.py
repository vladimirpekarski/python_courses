# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Currency(object):
    GOLD_ID = 1
    SILVER_ID = 2
    BRONZE_ID = 3

    def __init__(self, type, name, value=100):
        self.type = type
        self.name = name
        self.value = value
