# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'
string_test = 'bla bla bla bla bla bla bla olo olo'

def split_string(text):
    return text.split()

for word in split_string(string_test):
    print(word)