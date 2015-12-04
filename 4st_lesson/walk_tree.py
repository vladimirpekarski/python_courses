# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import os
for root_dir, dirs, files in os.walk(".."):
    print("root_dir is {}, dirs are {}, files are {}".format(root_dir, dirs, files))