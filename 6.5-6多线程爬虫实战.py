#!/usr/bin/python3
# encoding:utf-8

import threading
class A (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("aaaaaaaaa"+str(i))
class B (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("bbbbbbbbbb"+str(i))

t1=A()
t1.start()
t2=B()
t2.start()
