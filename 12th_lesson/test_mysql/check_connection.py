# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import MySQLdb as mdb
import datetime


con = mdb.connect('localhost', 'root', 'root', 'game')

def as_dict(user_id):
    return {
        'user_id': user_id,
        'start_time': datetime.datetime.now(),
        'end_time': datetime.datetime.now(),
        'duration':  5
        }

sql_data = as_dict(1)

sql_query = """INSERT INTO session (user_id, start_time,
    end_time, duration, created, updated) VALUES (%(user_id)s,
    %(start_time)s, %(end_time)s, %(duration)s, now(), now())
    """

with con:
    cur = con.cursor()
    cur.execute(sql_query, sql_data)
