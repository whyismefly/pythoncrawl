#!/usr/bin/python3
# encoding:utf-8

import threading
import queue
import re
import urllib.request
import time
import urllib.error

# class A (threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             print("aaaaaaaaa"+str(i))
# class B (threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             print("bbbbbbbbbb"+str(i))
#
# # t1=A()
# # t1.start()
# # t2=B()
# # t2.start()
#
# a=queue.Queue()
# a.put("hello")
# a.task_done()
# print(a.get())
# a.put("python")
# a.task_done()
# a.put("php")
# a.task_done()
# a.put("java")
# a.task_done()
# print(a.get())
# print(a.get())
# print(a.get())

urlqueue=queue.Queue()
headers=(
"user-agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
)
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
listurl=[]
def use_proxy(proxy_addr,url):
    try:
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("excption:"+str(e))
        time.sleep(1)

class geturl(threading.Thread):
    def __init__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.pagestart=pagestart
        self.pageend=pageend
        self.proxy=proxy
        self.urlqueue=urlqueue
        self.key=key
    def run(self):
        page=self.pagestart
        keycode=urllib.request.quote("key")
        pagecode=urllib.request.quote("&queue")
        for page in range(self.pagestart,self.pageend+1):
            url="http://weixin.sougou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            data1=use_proxy(self.proxy,url)
            listurlpat='<div class="txt_box">.*?(http://.*)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("get page "+str(len(listurl)))
        for i in range(0,len(listurl)):
            time.sleep(7)
            for j in range(0,len((listurl[i]))):
                try:
                    url=listurl[i][j]
                    url=url.replace("amp;","")
                    print("第"+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("excption:" + str(e))
                    time.sleep(1)

class getcontent(threading.Thread):
    def __init__(self,urlqueue,proxy):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue
        self.proxy=proxy
    def run(self):
        html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>微信文章页面</title>
            </head>
            <body>'''
        fh = open("../2.html", "wb")
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh=open("../2.html", "ab")
        i=1
        while(True):
            try:
                url=self.urlqueue.get()
                data=use_proxy(self.proxy,url)
                titlepat="<title>(.*?)</title>"
                contentpat='id="js_content">(.*?)id="js_sq_bar"'
                title=re.compile(titlepat).findall(data)
                content=re.compile(contentpat,re.S).findall(data)
                thistitle="not this time"
                thiscontent = "not this time"
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                dataall="<p>title:"+thistitle+"</p><p>content:"+thiscontent+"</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("page"+str(i)+"...")
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                time.sleep(10)
            except  Exception as e:
                print("exception:"+str(e))
                time.sleep(1)
        fh.close()
        html2='''</body>
        </html>
        '''
        fh=open("../2/html","ab")
        fh.write(html2.encode("utf-8"))
        fh.close()

class conrl(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue=urlqueue
    def run(self):
        while(True):
            print("excuting")
            time.sleep(60)
            if(self.urlqueue.empty()):
                print("excuted")
                exit()
key="人工智能"
proxy="119.6.136.122:80"
proxy2=""
pagestart=1
pageend=2
t1=geturl(key,pagestart,pageend,proxy,urlqueue)
t1.start()
t2=getcontent(urlqueue,proxy)
t2.start()
t3=conrl(urlqueue)
t3.start()
