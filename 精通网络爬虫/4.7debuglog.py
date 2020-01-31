#!/usr/bin/python3
# encoding:utf-8

import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httphds=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httphds)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://edu.51cto.com")



