# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

host_path = r'C:\Windows\System32\drivers\etc\hosts'
host_file = open(host_path)
print(host_file)
data = host_file.readlines()
for line in data:
    print(line.strip())