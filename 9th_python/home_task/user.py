# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from session import Session
from currency import Currency
from progress import Progress

class User(object):
    """
    >>> user = User('test@test.test', 'pass', 'nick')
    >>> user.email
    'test@test.test'
    >>> user.password
    'pass'
    >>> user.nickname
    'nick'
    >>> user.session
    >>> user.achievements
    >>> user.currency
    >>> user.progresses
    """
    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.session = None
        self.currency = None
        self.progresses = None
        self.achievements = None

    def __str__(self):
        """
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> print(user)
        User: email: test@test.test; Nickname: nick;
        """
        return '{}: email: {}; Nickname: {};'.format(self.__class__.__name__,
                                                     self.email,
                                                     self.nickname)

    def register(self, confirm_pass, shelve_db=None):
        """
        >>> import shelve
        >>> import os
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user.register('passsss', shelve_db)
        Confirmed password isn't correct
        >>> user.register('pass', shelve_db)
        User successfully registered
        Save User to db
        >>> user.register('pass', shelve_db)
        User can't register. Username already exists
        >>> os.remove(r'db/users')
        """
        if self._check_unique_nickname(self.nickname, shelve_db):
            print('{} can\'t register. Username already exists'.
                  format(self.__class__.__name__))
        elif self.password != confirm_pass:
            print('Confirmed password isn\'t correct')
        else:
            print('{} successfully registered'.format(self.__class__.__name__))
            self.currency = {Currency.GOLD_ID: Currency(Currency.GOLD_ID, 'Gold', value=0),
                             Currency.SILVER_ID: Currency(Currency.SILVER_ID, 'Silver', value=50),
                             Currency.BRONZE_ID: Currency(Currency.BRONZE_ID, 'Bronze'), }
            self.progresses = {Progress.EXPERIENCE_ID: Progress(Progress.EXPERIENCE_ID, 'Experience'),
                               Progress.SOME_PROGRESS_ID: Progress(Progress.SOME_PROGRESS_ID, 'Some_Progress2'), }
            self.achievements = {}
            self._save(shelve_db)

    def login(self, nickname, password, shelve_db=None):
        """
        >>> import shelve
        >>> import os
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user.register('pass', shelve_db)
        User successfully registered
        Save User to db
        >>> user.login('nick', 'pass', shelve_db) # doctest: +ELLIPSIS
        User nick logged in
        <__main__.User object at ...>
        >>> user.login('nick_', 'pass', shelve_db)
        User doesn't exist in db
        >>> os.remove(r'db/users')
        """
        if nickname in shelve_db.keys() and shelve_db[nickname].password == password:
            print('{} {} logged in'.format(self.__class__.__name__,
                                           self.nickname))
            logged_user = shelve_db[nickname]
            logged_user.session = Session()

            return logged_user
        else:
            print('{} doesn\'t exist in db'.format(self.__class__.__name__))

    def logout(self, shelve_db=None):
        """
        >>> import shelve
        >>> import os
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user.register('pass', shelve_db)
        User successfully registered
        Save User to db
        >>> logged_user = user.login('nick', 'pass', shelve_db) # doctest: +ELLIPSIS
        User nick logged in
        >>> logged_user.logout(shelve_db)
        User nick logged out
        Save User to db
        >>> logged_user.logout(shelve_db)
        User nick isn't logged in
        >>> os.remove(r'db/users')
        """
        if self.session:
            print('{} {} logged out'.format(self.__class__.__name__,
                                            self.nickname))
            self.session.stop_session()
            self._save(shelve_db)
            self.session = None
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    def _save(self, shelve_db=None):
        """
        >>> import shelve
        >>> import os
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user._save(shelve_db)
        Save User to db
        >>> os.remove(r'db/users')
        """
        print('Save {} to db'.format(self.__class__.__name__,))
        shelve_db[self.nickname] = self

    def do_something(self, progress_type, bonus):
        """
        >>> import shelve
        >>> import os
        >>> from progress import Progress
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user.register('pass', shelve_db)
        User successfully registered
        Save User to db
        >>> logged_user = user.login('nick', 'pass', shelve_db) # doctest: +ELLIPSIS
        User nick logged in
        >>> logged_user.do_something(Progress.EXPERIENCE_ID, 30)
        >>> logged_user.progresses[Progress.EXPERIENCE_ID].current_value
        30
        >>> logged_user.logout(shelve_db)
        User nick logged out
        Save User to db
        >>> logged_user.do_something(Progress.EXPERIENCE_ID, 30)
        User nick isn't logged in
        >>> os.remove(r'db/users')
        """
        if self.session:
            achievement = self.progresses[progress_type].change_progress(bonus)
            if achievement and achievement.ach_type not in self.achievements.keys():
                self.achievements[achievement.ach_type] = achievement
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    @staticmethod
    def _check_unique_nickname(nickname, shelve_db=None):
        """
        >>> import shelve
        >>> import os
        >>> shelve_db = shelve.open(r'db/users')
        >>> user = User('test@test.test', 'pass', 'nick')
        >>> user._check_unique_nickname('nick', shelve_db)
        False
        >>> user.register('pass', shelve_db)
        User successfully registered
        Save User to db
        >>> user._check_unique_nickname('nick', shelve_db)
        True
        >>> os.remove(r'db/users')
        """
        return nickname in shelve_db.keys()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
