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
    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
      <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <title>微信文章页面</title>
      </head>
      <body>'''
    fh=open("../1.html","wb")
    fh.close()
    fh=open("../1.html","ab")
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                url=url.replace("amp;","")
                data=use_proxy(proxy,url)
                titlepat="<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat, re.S).findall(data)
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                dataall="<p>标题为:"+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页第"+str(j)+"次处理") #便于调试
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
            except  Exception as e:
                print("exception:"+str(e))
                time.sleep(1)
    fh.close()
    html2 = '''</body>
        </html>
        '''
    fh=open("../1.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()

key="物联网"
proxy="119.6.136.122:80"
proxy2=""
pagestart=1
pageend=2
listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)

