#!/usr/bin/python3
# encoding:utf-8

import urllib.request
import urllib.parse

#1.get
# keywd="hello"
# url="http://www.baidu.com/s?wd="+keywd
# req=urllib.request.Request(url)
# data=urllib.request.urlopen(req).read()
# fhandle=open("4.html","wb")
# fhandle.write(data)
# fhandle.close()
# print(len(data))

# url="http://www.baidu.com/s?wd="
# key="微微老师"
# key_code=urllib.request.quote(key)
# url_all=url+key_code
# req=urllib.request.Request(url_all)
# data=urllib.request.urlopen(req).read()
# fhandle=open("5.html","wb")
# fhandle.write(data)
# fhandle.close()
# print(len(data))

#2.post

url="http://www.iqianyue.com/mypost"
postdata=urllib.parse.urlencode({
    "name":"ceo@iqianyue.com",
    "pass":"aA123456"
}).encode('utf-8')
req=urllib.request.Request(url,postdata)

headers=("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
req.add_header("user-agent",headers)

data=urllib.request.urlopen(req).read()
fhandle=open("6.html","wb")
fhandle.write(data)
fhandle.close()
#这里没有测试成功


