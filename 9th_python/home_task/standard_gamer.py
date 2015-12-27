# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from user import User

class StandardGamer(User):
    def __init__(self, email, password, nickname, desc='Standard User',
                 banned=False):
        super(StandardGamer, self).__init__(email, password, nickname)
        self.banned = banned
        self.desc = desc

    def __str__(self):
        return super(StandardGamer, self).__str__() + 'description: {}'.format(self.desc)

    def login(self, nickname, password, _shelve_db=None):
        if not self.banned:
            return super(StandardGamer, self).login(nickname, password,
                                                    _shelve_db)
        else:
            print('{} is banned'.format(self.nickname))


if __name__ == '__main__':
    import shelve
    import time

    def print_entities(db):
        for user in db:
            print(user)

    shelve_db = shelve.open(r'db/users')

    valid_user = StandardGamer('some@email.com', 'password1', 'nickname')
    valid_user.register('password1', shelve_db)
    logged_user = valid_user.login('nickname', 'password1', shelve_db)
    logged_user.do_something(1, 30)
    logged_user.do_something(1, 30)
    logged_user.do_something(1, 30)
    logged_user.do_something(1, 30)
    logged_user.do_something(1, 30)
    logged_user.do_something(1, 30)
    time.sleep(10)
    print(logged_user.session.start_time)
    print(logged_user.session.end_time)
    print(logged_user.session.session_time)
    print(logged_user.progresses[1].name)
    print(logged_user.progresses[1].current_value)
    print(logged_user.progresses[1].target_value)
    print(logged_user.achievements)
    logged_user.logout(shelve_db)
    shelve_db.close()