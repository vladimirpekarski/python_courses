# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from achievement import Achievement

class Progress(object):
    """
    >>> progress = Progress(Progress.EXPERIENCE_ID, 'Experience')
    >>> progress.EXPERIENCE_ID
    1
    >>> progress.name
    'Experience'
    >>> progress.current_value
    0
    >>> progress.target_value
    100
    """
    EXPERIENCE_ID = 1
    SOME_PROGRESS_ID = 2

    def __init__(self, progress_type, name, current_value=0,
                 target_value=100):
        self.progress_type = progress_type
        self.name = name
        self.current_value = current_value
        self.target_value = target_value

    def __str__(self):
        """
        >>> progress = Progress(Progress.EXPERIENCE_ID, 'Experience')
        >>> print(progress)
        Progress name: Experience; current progress: 0
        """
        return 'Progress name: {}; current progress: {}'.format(
            self.name, self.current_value)

    def change_progress(self, received_value):
        """
        >>> progress = Progress(Progress.EXPERIENCE_ID, 'Experience')
        >>> progress.change_progress(50)
        >>> progress.current_value
        50
        """
        self.current_value += received_value
        if self.current_value >= self.target_value:
            return self._give_achievement()

    def _give_achievement(self):
        """
        >>> progress = Progress(Progress.EXPERIENCE_ID, 'Experience')
        >>> progress._give_achievement()
        Give achievement: ACHIEVEMENT_Experience
        ACHIEVEMENT_Experience
        """
        achievement_name = 'ACHIEVEMENT_' + self.name
        print('Give achievement: {}'.format(achievement_name))
        achievement = Achievement(self.progress_type, achievement_name)

        return achievement

if __name__ == '__main__':
    import doctest
    doctest.testmod()
