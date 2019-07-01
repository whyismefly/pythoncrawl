#!/usr/bin/python3
# encoding:utf-8

import re
import urllib.request

def getcontent(url,page):
    headers = ("user-agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    userpat='target="_blank" title="(.*?)">'
    contentpat='<div class="content">(.*?)</div>'
    userlist=re.compile(userpat,re.S).findall(data)
    print(userlist)
    contentlist=re.compile(contentpat,re.S).findall(data)
    print(contentlist)
    x=1
    for content in contentlist:
        content=content.replace("\n","")
        name="content"+str(x)
        exec(name+'=content')
        x+=1
    y=1
    for user in userlist:
        name="content"+str(y)
        print("user"+str(page)+str(y)+"is:"+user)
        print("content:")
        exec("print("+name+")")
        print("\n")
        y+=1
for i in range(1,30):
    url="https://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url,i)