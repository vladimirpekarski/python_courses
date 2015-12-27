# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Currency(object):
    def __init__(self, type, name, value=100):
        self.type = type
        self.name = name
        self.value = value
