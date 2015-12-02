# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import urllib2
import urllib

api_key = ''
phone = ''

url_template = 'http://sms.ru/sms/send?api_id=%(api_key)s&to=%(phone)s'
url = url_template % {"api_key": api_key, "phone": phone}
text = u'Hello, медвед!'
encoded_text = urllib.urlencode({"text": text.encode('utf-8')})
headers = {"Content-type": "application/x-www-form-urlencoded", }
r = urllib2.Request(url, data=encoded_text, headers=headers)
u = urllib2.urlopen(r)
print(u.read())

