# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'


class Duck:
    def __init__(self, name):
        self.name = name
        print("Hello, {}".format(self.name))

    def __del__(self):
        print("Bye-bye, {}".format(self.name))

    def say(self, message):
        print('{} says {}'.format(self.name, message))

if __name__ == "__main__":
    d = Duck(name="Donald Duck")
    d.say('Something')
    del d
    print("after all...")