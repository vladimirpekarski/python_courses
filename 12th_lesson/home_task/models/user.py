# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from session import Session
from currency import Currency
from progress import Progress
from achievement import Achievement
from user_fabric import UserFactory

class User(object):
    STANDARD_GAMER = 0
    MODERATOR = 1
    ADMIN = 2

    def __init__(self, email, password, nickname, connect):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.connect = connect
        self.session = None
        self.currency = None
        self.progresses = None
        self.achievements = None
        self.banned = None
        self.desc = None
        self.role = None
        self.user_id = None

    def __str__(self):
        return '{}: email: {}; Nickname: {};'.format(self.__class__.__name__,
                                                     self.email,
                                                     self.nickname)

    def register(self, confirm_pass):
        if self.is_value_exists(self.nickname, 'nickname'):
            print('{} can\'t register. Username already exists'.
                  format(self.__class__.__name__))
        elif self.is_value_exists(self.email, 'email'):
            print('{} can\'t register. Email already exists'.
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
            self.save_to_db()

    def login(self, nickname, password):
        user = self.load_from_db(nickname)
        if user:
            if user.password == password:
                user.session = Session()
                user.connect = self.connect
                return user
            else:
                print('Provided password doesn\'t match'.format(self.__class__.__name__))
        else:
            print('{} doesn\'t exist in db'.format(self.__class__.__name__))

    def logout(self):
        if self.session:
            print('{} {} logged out'.format(self.__class__.__name__,
                                            self.nickname))
            self.session.stop_session()
            achievements_db = self._is_achievement()
            if not achievements_db:
                for achievement in self.achievements.values():
                    achievement.save_to_db(self.connect, self.user_id)
            else:
                ach_types_db = [achievement_db[1] for achievement_db in achievements_db]
                for achievement in self.achievements.values():
                    if achievement.ach_type not in ach_types_db:
                        achievement.save_to_db(self.connect, self.user_id)

            self.session.save_to_db(self.connect, self.user_id)
            self.session = None
            self.update_db()
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    def do_something(self, progress_type, bonus):
        if self.session:
            achievement = self.progresses[progress_type].change_progress(bonus)
            if achievement and achievement.ach_type not in self.achievements.keys():
                self.achievements[achievement.ach_type] = achievement
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    def give_money(self, money_type, value):
        if self.session:
            self.currency[money_type].change_money(value)
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    def take_money(self, money_type, value):
        if self.session:
            self.currency[money_type].change_money(-value)
        else:
            print('{} {} isn\'t logged in'.format(self.__class__.__name__,
                                                  self.nickname))

    def is_value_exists(self, value, column):
        sql_query = """SELECT """ + column + """ FROM user"""
        with self.connect:
            cur = self.connect.cursor()
            cur.execute(sql_query)
        results = cur.fetchall()

        for result in results:
            if result[0] == value:
                return True

        return False

    def _is_achievement(self):
        achievements = Achievement.load_from_db(self.user_id, self.connect)
        return achievements

    def save_to_db(self):
        sql_data = self._as_dict()

        sql_query = """INSERT INTO user (role, nickname, email,
                       password, banned, description, created, updated)
                       VALUES (%(role)s, %(nickname)s, %(email)s,
                       %(password)s, %(banned)s, %(description)s, now(),
                       now())"""

        with self.connect:
            cur = self.connect.cursor()
            cur.execute(sql_query, sql_data)

        self.user_id = cur.lastrowid

        for currency in self.currency.values():
            currency.save_to_db(self.connect, cur.lastrowid)

        for progress in self.progresses.values():
            progress.save_to_db(self.connect, cur.lastrowid)

        if self.session:
            self.session.save_to_db(self.connect, cur.lastrowid)

    def load_from_db(self, nickname):
        sql_data = {
            'nickname': nickname
        }
        sql_query = """SELECT id, role, nickname, email, password, banned,
                       description FROM user WHERE nickname=%(nickname)s"""

        with self.connect:
            cur = self.connect.cursor()
            cur.execute(sql_query, sql_data)

        result = cur.fetchone()
        if not result:
            return False

        user = UserFactory.create_user(result)
        achievements = Achievement.load_from_db(user.user_id, self.connect)
        user.achievements = {}
        for achievement in achievements:
            user.achievements[achievement[1]] = Achievement(achievement[1],
                                                            achievement[0])

        currencies = Currency.load_from_db(user.user_id, self.connect)
        user.currency = {}
        for currency in currencies:
            user.currency[currency[2]] = Currency(currency[2], currency[0],
                                                  currency[1])

        progresses = Progress.load_from_db(user.user_id, self.connect)
        user.progresses = {}
        for progress in progresses:
            user.progresses[progress[0]] = Progress(progress[0], progress[1],
                                                    progress[2], progress[3])

        return user

    def update_db(self):
        sql_data = self._as_dict()

        sql_query = """UPDATE user SET role=%(role)s, nickname=%(nickname)s,
                       email=%(email)s, password=%(password)s, banned=%(banned)s,
                       description=%(description)s, updated=now() WHERE id=%(id)s"""

        with self.connect:
            cur = self.connect.cursor()
            cur.execute(sql_query, sql_data)

        for currency in self.currency.values():
            currency.update_db(self.connect, self.user_id)

        for progress in self.progresses.values():
            progress.update_db(self.connect, self.user_id)

    def _as_dict(self):
        return {
            'id': self.user_id,
            'role': self.role,
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password,
            'banned': self.banned,
            'description': self.desc
        }
