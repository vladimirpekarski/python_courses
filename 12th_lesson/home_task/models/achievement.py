# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Achievement(object):
    def __init__(self, ach_type, name):
        self.ach_type = ach_type
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save_to_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)

        sql_query = """INSERT INTO achievement (user_id, name,
                       type, created, updated) VALUES (%(user_id)s,
                       %(name)s, %(type)s, now(), now())"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def _as_dict(self, user_id):
        return {
            'user_id': user_id,
            'name': self.name,
            'type': self.ach_type,
        }

    @staticmethod
    def load_from_db(user_id, connect):
        sql_data = {
            'user_id': user_id
        }

        sql_query = """SELECT name, type FROM achievement
        WHERE user_id=%(user_id)s"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

        return cur.fetchall()

