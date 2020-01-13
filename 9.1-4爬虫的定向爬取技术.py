#!/usr/bin/python3
# encoding:utf-8

import urllib.request
import http.cookiejar
import re

vid= "1472528692"
comid="6173403130078248384"
url="http://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
         "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
         "Connection": "keep-alive",
         "referer": "http://www.163.com/"
}

cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8")

idpat='"id":"(.*?)"'
userpat='"nick":"(.*?)",'
conpat='"content":"(.*?)",'

idlist=re.compile(idpat,re.S).findall(data)
userlist=re.compile(userpat,re.S).findall(data)