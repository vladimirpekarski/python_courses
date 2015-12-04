# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

file_object = open('C:\cat.bmp', 'rb')
data = file_object.read()
import struct
print(struct.unpack("<ccihhi", data[:14]))
print(len(data))
print(struct.unpack("<iiihhiiiiii", data[14:54]))
print(len(data) - 54)
print(608160 / 3)
d2 = data[:54] + (len(data) - 54) * '\xff'
open('gg.bmp', 'wb').write(d2)
d2 = data[:54] + (len(data) - 54) * '\x00'
open('gg1.bmp', 'wb').write(d2)