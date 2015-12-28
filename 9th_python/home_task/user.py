# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from session import Session
from currency import Currency
from progress import Progress


class User(object):
    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.session = None
        self.currency = None
        self.progresses = None
        self.achievements = None

    def __str__(self):
        return '{}: email: {}; Nickname: {}; '.format(self.__class__.__name__,
                                                      self.email,
                                                      self.nickname)

    def register(self, confirm_pass, shelve_db=None):
        if self._check_unique_nickname(self.nickname, shelve_db):
            print('{} can\'t register. Username already exists'.
                  format(self.__class__.__name__))
        elif self.password != confirm_pass:
            print('Confirmed password isn\'t correct')
        else:
            print('{} successfully registered'.format(self.__class__.__name__))
            self.currency = {1: Currency(1, 'Gold', value=0),
                             2: Currency(2, 'Silver', value=50),
                             3: Currency(3, 'Bronze'), }
            self.progresses = {1: Progress(1, 'Experience'),
                               2: Progress(2, 'Some_Progress2'), }
            self.achievements = {}
            self._save(shelve_db)

    def login(self, nickname, password, shelve_db=None):
        if nickname in shelve_db.keys() and shelve_db[nickname].password == password:
            print('{} {} logged in'.format(self.__class__.__name__,
                                           self.nickname))
            logged_user = shelve_db[nickname]
            logged_user.session = Session()

            return logged_user
        else:
            print('{} doesn\'t exist in db'.format(self.__class__.__name__))

    def logout(self, shelve_db=None):
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
        print('Save {} to db'.format(self.__class__.__name__,))
        shelve_db[self.nickname] = self

    def do_something(self, progress_type, bonus):
        if self.session:
            achievement = self.progresses[progress_type].change_progress(bonus)
            if achievement and achievement.ach_type not in self.achievements.keys():
                self.achievements[achievement.ach_type] = achievement
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    @staticmethod
    def _check_unique_nickname(nickname, shelve_db=None):
        return nickname in shelve_db.keys()
