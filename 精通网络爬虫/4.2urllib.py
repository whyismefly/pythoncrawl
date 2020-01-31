#!/usr/bin/python3
# encoding:utf-8

import urllib.request

file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readline()
datalines=file.readlines()

print(data)
print('---------')
print(dataline)
print('---------')
for line in datalines:
    print(datalines)

fhandle=open("1.html","wb")
fhandle.write(data)
fhandle.close()
print(file.info())
print(file.getcode())
print(file.geturl())

filename=urllib.request.urlretrieve("http://edu.51cto.com","2.html")
urllib.request.urlcleanup()

quoteurl=urllib.request.quote("http://www.sina.com.cn")
print(quoteurl)
unquote=urllib.request.unquote(quoteurl)
print(unquote)