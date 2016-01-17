# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class AdminUser(User):
    def __init__(self, email, password, nickname, connect=None,
                 user_id=None):
        super(AdminUser, self).__init__(email, password, nickname,
                                        connect)
        self.role = User.ADMIN
        self.user_id = user_id

    def bann_user(self, standard_user):
        if not self.is_value_exists(standard_user.nickname, 'nickname'):
            print('User with nickname {} doesn\'t exist'.format(
                standard_user.nickname))
        else:
            sql_data = {
                'id': standard_user.user_id,
                'banned': 1,
            }
            sql_query = """UPDATE user SET banned=%(banned)s,
                           updated=now() WHERE id=%(id)s"""
            with self.connect:
                cur = self.connect.cursor()
                cur.execute(sql_query, sql_data)
