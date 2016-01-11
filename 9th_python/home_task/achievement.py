# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Achievement(object):
    """
    >>> ach = Achievement(1, 'Test')
    >>> ach.ach_type
    1
    >>> ach.name
    'Test'
    """
    def __init__(self, ach_type, name):
        self.ach_type = ach_type
        self.name = name

    def __str__(self):
        """
        >>> ach = Achievement(1, 'Test')
        >>> ach.__str__()
        'Test'
        """
        return self.name

    def __repr__(self):
        """
        >>> ach = Achievement(1, 'Test')
        >>> ach.__repr__()
        'Test'
        """
        return self.name

if __name__ == '__main__':
    import doctest
    doctest.testmod()
