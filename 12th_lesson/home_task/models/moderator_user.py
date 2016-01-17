# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class ModeratorUser(User):
    def __init__(self, email, password, nickname, connect=None, user_id=None):
        super(ModeratorUser, self).__init__(email, password, nickname,
                                            connect)
        self.role = User.MODERATOR
        self.user_id = user_id

    def update_user_desc(self, user, value):
        if not self.is_value_exists(user.nickname, 'nickname'):
            print('User with nickname {} doesn\'t exist'.format(user.nickname))
        elif self.session:

            sql_data = {
                'id': user.user_id,
                'description': value
            }

            sql_query = """UPDATE user SET description=%(description)s,
                           updated=now() WHERE id=%(id)s"""

            with self.connect:
                cur = self.connect.cursor()
                cur.execute(sql_query, sql_data)

