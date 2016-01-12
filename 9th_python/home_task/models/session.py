# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from datetime import datetime

class Session(object):
    """
    >>> session = Session()
    >>> not session.start_time
    False
    >>> session.end_time

    >>> session.session_time

    """
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.session_time = None

    def __str__(self):
        """
        >>> session = Session()
        >>> session.stop_session()
        >>> print(session)
        Last session time: 0:00:00
        """
        return 'Last session time: {}'.format(self.session_time)

    def stop_session(self):
        self.end_time = datetime.now()
        self._calculate_session_time()
        self.start_time = None
        self.end_time = None

    def _calculate_session_time(self):
        self.session_time = self.end_time - self.start_time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
