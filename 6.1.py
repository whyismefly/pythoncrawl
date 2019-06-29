#!/usr/bin/python3
# encoding utf-8

import re
import urllib.request

"""https://list.jd.com/list.html?cat=9987,653,655&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"""

def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    print(html1)
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    print("=============")
    print(result1)
    result1=result1[0]
    print("=============")
    print(result1)
    pat2='<img width="220" height="220" data-img="1" src="//(.+?jpg)" '
    imagelist=re.compile(pat2).findall(result1)
    print("=============????????")
    print(imagelist)
    x=1
    for imageurl in imagelist:
        imagename="E:/learn/GitHub/pythoncrawl/img1/"+str(page)+str(x)+'.jpg'
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,2):
    url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

