#!/usr/bin/python3
# encoding:utf-8

import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1)
        data=file.read()
        print(len(data),"  ",i)
    except Exception as e:
        print("error"+str(e))