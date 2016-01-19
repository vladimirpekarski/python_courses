# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import time
import MySQLdb as mdb
import models.standard_gamer as st_gamer
import models.admin_user as admin
import models.moderator_user as moderator
import models.progress as progress
import models.currency as curr

con = mdb.connect('localhost', 'root', 'root', 'my_game_3')
cur = con.cursor()

gamer = st_gamer.StandardGamer('email1@test.tst', 'password', 'nick',
                               connect=con)
gamer2 = st_gamer.StandardGamer('email2@test.tst', 'password', 'nick2',
                                connect=con)
gamer3 = st_gamer.StandardGamer('email3@test.tst', 'password', 'nick3',
                                connect=con)
moderator = moderator.ModeratorUser('moderator@test.tst', 'password',
                                    'moderator', connect=con)

admin = admin.AdminUser('admin@test.tst', 'passw', 'admin', connect=con)


gamer.register('password')
admin.register('passw')
gamer2.register('password')
gamer = gamer.login('nick', 'password')
gamer3.register('password')
time.sleep(10)
gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
gamer.do_something(progress.Progress.EXPERIENCE_ID, 50)
gamer.give_money(curr.Currency.BRONZE_ID, 900)
gamer.give_money(curr.Currency.SILVER_ID, 900)
gamer.give_money(curr.Currency.GOLD_ID, 900)
gamer.logout()
moderator.register('password')
moderator = moderator.login('moderator', 'password')
moderator.update_user_desc(gamer, "UPDATED DESCRIPTION!!!!")
moderator.logout()
gamer2 = gamer2.login('nick2', 'password')
gamer2.do_something(progress.Progress.EXPERIENCE_ID, 85)
gamer2.do_something(progress.Progress.EXPERIENCE_ID, 1222)
gamer2.do_something(progress.Progress.EXPERIENCE_ID, 85)
gamer2.logout()
admin = admin.login('admin', 'passw')
admin.bann_user(gamer3)
gamer3 = gamer3.login('nick3', 'password')
admin.logout()
gamer = gamer.login('nick', 'password')
gamer.do_something(progress.Progress.SOME_PROGRESS_ID, 50)
gamer.do_something(progress.Progress.SOME_PROGRESS_ID, 50)
gamer.do_something(progress.Progress.SOME_PROGRESS_ID, 50)
gamer.do_something(progress.Progress.SOME_PROGRESS_ID, 50)
gamer.logout()
gamer2 = gamer2.login('nick2', 'password')
gamer2.do_something(progress.Progress.SOME_PROGRESS_ID, 500)
gamer2.do_something(progress.Progress.SOME_PROGRESS_ID, 500)
gamer2.do_something(progress.Progress.SOME_PROGRESS_ID, 500)
gamer2.take_money(curr.Currency.GOLD_ID, 100)
gamer2.take_money(curr.Currency.SILVER_ID, 100)
gamer2.take_money(curr.Currency.BRONZE_ID, 500)
gamer2.logout()
