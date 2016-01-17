# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from achievement import Achievement

class Progress(object):
    EXPERIENCE_ID = 1
    SOME_PROGRESS_ID = 2

    def __init__(self, progress_type, name, current_value=0,
                 target_value=100):
        self.progress_type = progress_type
        self.name = name
        self.current_value = current_value
        self.target_value = target_value

    def __str__(self):
        return 'Progress name: {}; current progress: {}'.format(
            self.name, self.current_value)

    def change_progress(self, received_value):
        self.current_value += received_value
        if self.current_value >= self.target_value:
            return self._give_achievement()

    def _give_achievement(self):
        achievement_name = 'ACHIEVEMENT_' + self.name
        print('Give achievement: {}'.format(achievement_name))
        achievement = Achievement(self.progress_type, achievement_name)

        return achievement

    def save_to_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)

        sql_query = """INSERT INTO progress (user_id, type, name,
                       current_value, target_value, created, updated)
                       VALUES (%(user_id)s, %(type)s ,%(name)s,
                       %(current_value)s, %(target_value)s, now(), now())"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def update_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)
        sql_query = """UPDATE progress SET current_value=%(current_value)s,
                       target_value=%(target_value)s, updated=now()
                       WHERE user_id=%(user_id)s AND type=%(type)s"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def _as_dict(self, user_id):
        return {
            'user_id': user_id,
            'type': self.progress_type,
            'name': self.name,
            'current_value': self.current_value,
            'target_value': self.target_value
        }

    @staticmethod
    def load_from_db(user_id, connect):
        sql_data = {
            'user_id': user_id
        }

        sql_query = """SELECT type, name, current_value, target_value
                       FROM progress WHERE user_id=%(user_id)s"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

        return cur.fetchall()

