# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User
from standard_gamer import StandardGamer

class AdminUser(User):
    def bann_user(self, standard_user):
        if self.session:
            standard_user.banned = True
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

if __name__ == '__main__':
    import shelve
    shelve_db = shelve.open(r'db/users')
    gamer2 = StandardGamer('email2@test.tst', 'password', 'nick')
    gamer2.register('password', shelve_db)

    admin = AdminUser('admin@test.tst', 'password', 'admin')
    admin.register('password', shelve_db)
    registered_admin = admin.login('admin', 'password', shelve_db)
    registered_admin.bann_user(gamer2)
    registered_admin.logout(shelve_db)
    logged_user = gamer2.login('nick', 'password', shelve_db)
    shelve_db.close()
