# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

s = 'превед, медвед!'
su = s.decode('utf-8') # decode from utf-8 to unicode
print(isinstance(su, unicode), type(su))
text = su.encode('utf-8') # code from unicode to utf-8
print(isinstance(text, unicode), type(text))