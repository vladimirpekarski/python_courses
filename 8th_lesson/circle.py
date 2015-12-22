# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def circuit_len(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    c1 = Circle(2)
    c2 = Circle(1)
    assert int(c1.square()) == 12
    assert int(c2.square()) == 3
    assert int(c1.circuit_len()) == 12
    assert int(c2.circuit_len()) == 6