# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class StandardGamer(User):
    """
    >>> gamer = StandardGamer('some@email.com', 'pass', 'nick')
    >>> gamer.banned
    False
    >>> gamer.desc
    'Standard User'
    """
    def __init__(self, email, password, nickname, desc='Standard User',
                 banned=False):
        super(StandardGamer, self).__init__(email, password, nickname)
        self.banned = banned
        self.desc = desc

    def __str__(self):
        """
        >>> gamer = StandardGamer('some@email.com', 'pass', 'nick')
        >>> print(gamer)
        StandardGamer: email: some@email.com; Nickname: nick;description: Standard User
        """
        return super(StandardGamer, self).__str__() + 'description: {}'.format(self.desc)

    def login(self, nickname, password, _shelve_db=None):
        """
        >>> gamer = StandardGamer('some@email.com', 'pass', 'nick')
        >>> gamer.banned = True
        >>> gamer.login('nick', 'pass')
        nick is banned
        """
        if not self.banned:
            return super(StandardGamer, self).login(nickname, password,
                                                    _shelve_db)
        else:
            print('{} is banned'.format(self.nickname))


if __name__ == '__main__':
    import doctest
    doctest.testmod()