# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import shelve
import models.standard_gamer as st_gamer
import models.admin_user as admin
import models.moderator_user as moderator
import models.progress as progress

shelve_db = shelve.open(r'models/db/users')

first_gamer = st_gamer.StandardGamer('test@test.tst', 'pass', 'nick')
first_gamer.register('pass', shelve_db)
logged_first_gamer = first_gamer.login('nick', 'pass', shelve_db)
logged_first_gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
logged_first_gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
logged_first_gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
print(logged_first_gamer.achievements)
first_moderator = moderator.ModeratorUser('moderator@test.tst', 'pass', 'mod')
first_moderator.register('pass', shelve_db)
logged_first_moderator = first_moderator.login('mod', 'pass', shelve_db)
logged_first_moderator.update_user_desc('nick', 'UPDATED DESC', shelve_db)
print(logged_first_gamer.desc)
logged_first_gamer.logout(shelve_db)
first_admin = admin.AdminUser('admin@test.tst', 'pass', 'admin')
first_admin.register('pass', shelve_db)
logged_first_admin = first_admin.login('admin', 'pass', shelve_db)
logged_first_admin.bann_user(logged_first_gamer)
logged_first_gamer = logged_first_gamer.login('nick', 'pass', shelve_db)
