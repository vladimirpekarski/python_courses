# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User
from standard_gamer import StandardGamer

class ModeratorUser(User):
    def update_user_desc(self, nickname, value, _shelve_db):
        if self.session:
            user = _shelve_db[nickname]
            user.desc = value
            _shelve_db[nickname] = user
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

if __name__ == '__main__':
    import shelve
    shelve_db = shelve.open(r'db/users')

    moderator = ModeratorUser('mod@test.tst', 'pass', 'moderator')
    moderator.register('pass', shelve_db)
    logged_mod = moderator.login('moderator', 'pass', shelve_db)
    logged_mod.update_user_desc('nickname', 'UPDATED DESC', shelve_db)
    print(shelve_db['nickname'])
    print(shelve_db['nickname'].session.end_time)
    print(shelve_db['nickname'].session.session_time)

    shelve_db.close()
