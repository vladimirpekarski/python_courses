# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import smtplib

smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
print(smpt_obj.ehlo())
print(smpt_obj.starttls())
print(smpt_obj.login('some@email.com', 'somepassword'))
print(smpt_obj.sendmail('fromsomeemail', 'tosomeemail', 'somemessage'))
print(smpt_obj.quit())
