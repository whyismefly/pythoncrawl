#!/usr/bin/python3
# encoding:utf-8

import urllib.request
import urllib.parse
import http.cookiejar

"""http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F"""
"""
Request URL: https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20190506_00&sl=en&tl=zh-CN&sp=nmt&tc=1&sr=1&tk=93976.520559&mode=1
"""
# url="https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20190506_00&sl=en&tl=zh-CN&sp=nmt&tc=1&sr=1&tk=93976.520559&mode=1"
# """该网址不对"""
# url="http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F"
# """该网址不对"""
# url="http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F/static/js/login.js?id=bd2401b1e1243312fbb0"
# """该网址不对"""
# postdata=urllib.parse.urlencode({
# "username":"15305549775",
# "password":"1q2w3e"
# }).encode('utf-8')
# req=urllib.request.Request(url,postdata)
# req.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
# data=urllib.request.urlopen(req).read()
# print(data)
# fhandle=open("5.5-1.html",'wb')
# fhandle.write(data)
# fhandle.close()
# url2="http://bbs.chinaunix.net/"
# req2=urllib.request.Request(url2,postdata)
# req.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
# data2=urllib.request.urlopen(req2).read()
# fhandle=open("5.5-2.html",'wb')
# fhandle.write(data2)
# fhandle.close()

#https://blog.csdn.net/qq_35488769/article/details/72758034

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LB6kU"
postdata = urllib.parse.urlencode({
    "username":"15637142735",
    "password":"f43312626"
}).encode("UTF-8")
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(req).read()
text = data.decode("gbk","ignore")
file = open("login.html","w")
file.write(text)
url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
data = urllib.request.urlopen(req2).read()
file = open("log2.html","wb")
file.write(data)
file.close()












