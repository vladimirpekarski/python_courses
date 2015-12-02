# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import smtplib

from email.message import Message
from email.header import Header

msg = Message()
msg.set_charset('utf-8')
h = Header(u'Привет, Медвед!'.encode('utf-8'), 'utf-8')
msg['Subject'] = h
text = u'Юникод!'
msg.set_payload(text.encode('utf-8'))
smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)


print(smpt_obj.ehlo())
print(smpt_obj.starttls())
print(smpt_obj.login('some@email.com', 'somepassword'))
print(smpt_obj.sendmail('fromsomeemail', 'tosomeemail', 'somemessage'))
print(smpt_obj.quit())