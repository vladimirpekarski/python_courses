# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from datetime import datetime

class Session(object):
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.session_time = None

    def __str__(self):
        return 'Last session time: {}'.format(self.session_time)

    def stop_session(self):
        self.end_time = datetime.now()
        self._calculate_session_time()
        self.start_time = None
        self.end_time = None

    def _calculate_session_time(self):
        self.session_time = self.end_time - self.start_time
