# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class StandardGamer(User):
    def __init__(self, email, password, nickname, desc='Standard User',
                 banned=False, connect=None, user_id=None):
        super(StandardGamer, self).__init__(email, password, nickname,
                                            connect)
        self.banned = banned
        self.desc = desc
        self.role = User.STANDARD_GAMER
        self.user_id = user_id

    def __str__(self):
        return super(StandardGamer, self).__str__() + 'description: {}'.format(self.desc)

    def login(self, nickname, password):
        sql_data = {
            'nickname': nickname,
        }
        sql_query = """SELECT banned FROM user
                       WHERE nickname=%(nickname)s"""
        with self.connect:
            cur = self.connect.cursor()
            cur.execute(sql_query, sql_data)
        banned = cur.fetchone()

        if not banned[0]:
            return super(StandardGamer, self).login(nickname, password)
        else:
            print('{} is banned'.format(self.nickname))
