# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Currency(object):
    GOLD_ID = 1
    SILVER_ID = 2
    BRONZE_ID = 3

    def __init__(self, cur_type, name, value=100):
        self.cur_type = cur_type
        self.name = name
        self.value = value

    def change_money(self, delta):
        self.value += delta

    def save_to_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)

        sql_query = """INSERT INTO currency (user_id, name,
                       value, type, created, updated)
                       VALUES (%(user_id)s,%(name)s, %(value)s, %(type)s,
                       now(), now())"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def update_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)
        sql_query = """UPDATE currency SET value=%(value)s, updated=now()
                       WHERE user_id=%(user_id)s AND type=%(type)s"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def _as_dict(self, user_id):
        return {
            'user_id': user_id,
            'name': self.name,
            'value': self.value,
            'type': self.cur_type,
        }

    @staticmethod
    def load_from_db(user_id, connect):
        sql_data = {
            'user_id': user_id
        }

        sql_query = """SELECT name, value, type FROM currency
                       WHERE user_id=%(user_id)s"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

        return cur.fetchall()