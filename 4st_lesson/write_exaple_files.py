# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

file_object = open('test.txt', 'w')
file_object.write('Hello out there!\n')
file_object.close()

file_object = open('test.txt', 'a')
file_object.write('Hello again!')