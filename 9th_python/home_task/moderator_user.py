# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class ModeratorUser(User):
    def update_user_desc(self, nickname, value, _shelve_db):
        """
        >>> import shelve
        >>> import os
        >>> from standard_gamer import StandardGamer
        >>> shelve_db = shelve.open(r'db/users')
        >>> gamer2 = StandardGamer('email2@test.tst', 'password', 'nick')
        >>> gamer2.register('password', shelve_db)
        StandardGamer successfully registered
        Save StandardGamer to db
        >>> moderator = ModeratorUser('mod@test.tst', 'pass', 'moderator')
        >>> moderator.register('pass', shelve_db)
        ModeratorUser successfully registered
        Save ModeratorUser to db
        >>> logged_mod = moderator.login('moderator', 'pass', shelve_db)
        ModeratorUser moderator logged in
        >>> logged_mod.update_user_desc('nick', 'UPDATED DESC', shelve_db)
        >>> logged_gamer = gamer2.login('nick', 'password', shelve_db)
        StandardGamer nick logged in
        >>> logged_gamer.desc
        'UPDATED DESC'
        >>> os.remove(r'db/users')
        """
        if nickname not in _shelve_db.keys():
            print('User with nickname {} doesn\'t exist'.format(nickname))
        elif self.session:
            user = _shelve_db[nickname]
            user.desc = value
            _shelve_db[nickname] = user
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
