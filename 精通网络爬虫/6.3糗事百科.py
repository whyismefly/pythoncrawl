#!/usr/bin/python3
# encoding:utf-8

import re
import urllib.request

def getcontent(url,page):
    headers = ("user-agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8",  errors='ignore')#这里转码有错误，先忽略吧
    data=str(data)
    # print(data)
    # userpat='target="_blank" title="(.*?)">'
    # < a class ="recmd-content" href="/article/121217166" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])" > 咏哥走了，金大侠也走了，朋友圈又是一波接一波的轰炸。跑保险的借此说大病；做净水器的说喝水的重要性；做保健品的说产品疗效……我说，咏哥买不起保险还是安装不起净水器 < / a >
    userpat="'web-list-user','chick'])\" >(.*?)</a>\""
    # contentpat='<div class="content">(.*?)</div>'
    # contentpat='<div class="content">(.*?)</div>'
    # userlist=re.compile(userpat,re.S).findall(data)
    userlist=re.compile(userpat,re.S).findall(data)
    print(userlist)

    # contentlist=re.compile(contentpat,re.S).findall(data)
    # print(contentlist)
    # x=1
    # for content in contentlist:
    #     content=content.replace("\n","")
    #     name="content"+str(x)
    #     exec(name+'=content')
    #     x+=1


    # y=1
    # for user in userlist:
    #     name="content"+str(y)
    #     print("user"+str(page)+str(y)+"is:"+user)
    #     print("content:")
    #     exec("print("+name+")")
    #     print("\n")
    #     y+=1

for i in range(1,7):
    url="https://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url, i)