#!usr/bin/python3
# encoding:utf-8

import retest
import urllib.request

def getlink(url):
    headers = ("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    file=urllib.request.urlopen(url)
    data=str(file.read())
    pat='(https?://[^\s)";]+\.(\w|/)*)'
    link=retest.compile(pat).findall(data)
    link=list(set(link))
    return link
url="http://blog.csdn.net"
linklist=getlink(url)
a=1
for link in linklist:
    a=a+1
    print(link[0])
    print(a)



