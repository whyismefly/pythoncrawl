#!/usr/bin/python3
# encoding:utf-8

import urllib.request
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"

#1.build_opener()方法
# file=urllib.request.urlopen(url)
# print(file.readlines())
# print(file.getcode())
# #csdn没有屏蔽...
# #user-agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
# headers=("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# data=opener.open(url).read()
# print(data)
# fhanle1=open("3.1.html","wb")
# fhanle1.write(file.read())
# fhanle1.close()
# fhanle=open("3.html","wb")
# fhanle.write(data)
# fhanle.close()

#2.add_header()方法
req=urllib.request.Request(url)
req.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
data=urllib.request.urlopen(req).read()
print(data)