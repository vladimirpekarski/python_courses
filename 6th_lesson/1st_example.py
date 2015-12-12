# -*- coding: utf-8 -*-

import datetime

l = range(10**6)
s = set(range(10**6))
number = 1000

start = datetime.datetime.now()
for _ in xrange(number):
    10**7 in s
finish = datetime.datetime.now()
print("Set time: {}".format(finish-start))

start = datetime.datetime.now()
for _ in xrange(number):
    10**7 in l
finish = datetime.datetime.now()
print("List time: {}".format(finish-start))
