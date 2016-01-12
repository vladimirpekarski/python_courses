# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class AdminUser(User):
    def bann_user(self, standard_user):
        """
        >>> import shelve
        >>> import os
        >>> from standard_gamer import StandardGamer
        >>> shelve_db = shelve.open(r'db/users')
        >>> gamer2 = StandardGamer('email2@test.tst', 'password', 'nick')
        >>> gamer2.register('password', shelve_db)
        StandardGamer successfully registered
        Save StandardGamer to db
        >>> admin = AdminUser('admin@test.tst', 'password', 'admin')
        >>> admin.register('password', shelve_db)
        AdminUser successfully registered
        Save AdminUser to db
        >>> registered_admin = admin.login('admin', 'password', shelve_db)
        AdminUser admin logged in
        >>> registered_admin.bann_user(gamer2)
        >>> gamer2.banned
        True
        >>> os.remove(r'db/users')
        """
        if self.session:
            standard_user.banned = True
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
