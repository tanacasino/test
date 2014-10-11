#!/usr/bin/env python

class B(object):
    def b(self):
        print("b")

    def bb(self, word):
        print("Hello, %s World!" % word)


B().b()
B().b()
B().b()
