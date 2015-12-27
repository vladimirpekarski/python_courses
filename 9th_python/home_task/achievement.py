# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Achievement(object):
    def __init__(self, ach_type, name):
        self.ach_type = ach_type
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name