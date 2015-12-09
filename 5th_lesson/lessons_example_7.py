# -*- coding: utf-8 -*-

import Image
import datetime

def get_midnight_datetime(dt=datetime.datetime.now()):
    return datetime.datetime(dt.year, dt.month, dt.day)

if __name__ == "__main__":
    print(get_midnight_datetime())
