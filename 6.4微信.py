#!/usr/bin/python3
# encoding:utf-8

import re
import urllib.request
import time
import urllib.error

headers = (
"user-agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]

urllib.request.install_opener(opener)
listurl=[]

def use_proxy(proxy_addr,url):
    try:
        import urllib.request
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(0)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        keycode=urllib,re.quote(key)
        pagecode=urllib.request.quote("&page")
        for page in range(pagestart,pageend+1):
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            data1=use_proxy(proxy,url)
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("total"+str(len(listurl)))
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(0)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)


def getcontent(listurl,proxy):
    i=0
