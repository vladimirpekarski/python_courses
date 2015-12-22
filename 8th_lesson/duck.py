# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

class Duck:
    def __init__(self, name):
        self.name = name

    def say(self, msg):
        print("{} said: {}".format(self.name, msg))


class SpeechlessDuck(Duck):
    def say(self, msg):
        # do not say anything
        pass


if __name__ == "__main__":
    duck1 = Duck("McDuck")
    duck2 = SpeechlessDuck("SpeechlessDuck")
    duck1.say("Hello")
    duck2.say("Hello")