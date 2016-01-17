# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from datetime import datetime

class Session(object):
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.session_time = None

    def __str__(self):
        return 'Last session time: {}'.format(self.session_time)

    def __repr__(self):
        return 'Last session time: {}'.format(self.session_time)

    def stop_session(self):
        self.end_time = datetime.now()
        self._calculate_session_time()

    def _calculate_session_time(self):
        self.session_time = (self.end_time - self.start_time).total_seconds()

    def save_to_db(self, connect, user_id):
        sql_data = self._as_dict(user_id)

        sql_query = """INSERT INTO session (user_id, start_time,
                       end_time, duration, created, updated)
                       VALUES (%(user_id)s, %(start_time)s, %(end_time)s,
                       %(duration)s, now(), now())"""

        with connect:
            cur = connect.cursor()
            cur.execute(sql_query, sql_data)

    def _as_dict(self, user_id):
        return {
            'user_id': user_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'duration': self.session_time
        }