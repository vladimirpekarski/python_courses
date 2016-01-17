# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'


class UserFactory(object):
    @staticmethod
    def create_user(user_data):
        import moderator_user
        import standard_gamer
        import admin_user
        if user_data[1] == standard_gamer.StandardGamer.STANDARD_GAMER:
            return standard_gamer.StandardGamer(
                user_data[3], user_data[4], user_data[2], user_data[6],
                user_data[5], user_id=user_data[0])
        elif user_data[1] == moderator_user.ModeratorUser.MODERATOR:
            return moderator_user.ModeratorUser(
                user_data[3], user_data[4], user_data[2],
                user_id=user_data[0])
        elif user_data[1] == admin_user.AdminUser.ADMIN:
            return admin_user.AdminUser(
                user_data[3], user_data[4], user_data[2],
                user_id=user_data[0])
