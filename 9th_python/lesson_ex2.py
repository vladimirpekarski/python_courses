# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

if __name__ == "__main__":
    object_list = (A(), B(), C())
    class_list = (A, B, C)
    for o in object_list:
        for c in class_list:
            print("Class: {}, Object: {}, isinstance: {}".format(c, o, isinstance(o, c)))