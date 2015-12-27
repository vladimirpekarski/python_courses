# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

from achievement import Achievement

class Progress(object):
    def __init__(self, progress_type, name, current_value=0,
                 target_value=100):
        self.progress_type = progress_type
        self.name = name
        self.current_value = current_value
        self.target_value = target_value

    def change_progress(self, received_value):
        self.current_value += received_value
        if self.current_value >= self.target_value:
            return self._give_achievement()

    def _give_achievement(self):
        achievement_name = 'ACHIEVEMENT_' + self.name
        print('Give achievement: {}'.format(achievement_name))
        achievement = Achievement(self.progress_type, achievement_name)

        return achievement
