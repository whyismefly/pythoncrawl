#!/usr/bin/python3
# encoding:utf-8

import http.cookiejar,urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name+"="+item.value)


# filename = "cookies.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://weibo.com/")
# cookie.save(ignore_discard = True, ignore_expires = True)


import requests
import re

# r=requests.get("https://github.com/favicon.ico")
# with open("favicon.ico","wb") as f:
#     f.write(r.content)
# print(r.text)
# print(r.content)

# r = requests.get("https://www.zhihu.com/explore")
# print(r.text)
#
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
# }
# r = requests.get("https://www.zhihu.com/explore",headers = header)
# print(r.text)

# data = {'name':'germey','age':'22'}
# r = requests.post("http://httpbin.org/post",data=data)
# print(r.text)

# r = requests.get("http://www.jianshu.com")
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)

# files = {'file':open('favicon.ico','rb')}
# r = requests.post("http://httpbin.org/post",files=files)
# print(r.text)

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+"="+value)

# headers ={
#     'cookie':'zap=5d675a7c-a5c9-425c-8b24-8616ce6615de; d_c0="ACDW0mRX1xCPTo0qOTta_Ahl-WRf86-csJ8=|1582109222"; _ga=GA1.2.1573769491.1582677706; z_c0="2|1:0|10:1584694854|4:z_c0|92:Mi4xWExWekFBQUFBQUFBSU5iU1pGZlhFQ1lBQUFCZ0FsVk5SdFJoWHdCNVNvUWdsLTA4TTZBbDM1WTlvV240eE1UYTV3|a094296c8624912d71c7757620e1840d4b244921cad5235031a399bb078f1f20"; q_c1=4c740c0c79744595adbe15e2dea7987f|1584695951000|1584695951000; __utma=51854390.1573769491.1582677706.1585121232.1585121232.1; __utmz=51854390.1585121232.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/68263104; __utmv=51854390.100-1|2=registration_date=20140817=1^3=entry_date=20140817=1; _xsrf=537e766f-875b-40ae-90d7-0925568412e9; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1586332771,1586737268,1586919222,1588842381; tst=r; _gid=GA1.2.1758815139.1588842384; SESSIONID=KGzSoglMW71YG2JrLss6UDk6G2XB3wgjxwa1jNoSdfo; JOID=VV0cCklonsgRddDIEGbJVG9rW_MPIdWySR-1qF06q_VIOeeAbh0_d0Fy3sQbPRQxtE06_rlS_Z5Dpra09_-mPrE=; osd=Ul0VB0hvnsEcdNfIGWvIU29iVvIIIdy_SBi1oVA7rPVBNOaHbhQydkZy18kaOhQ4uUw9_rBf_JlDr7u18P-vM7A=; KLBRSID=3d7feb8a094c905a519e532f6843365f|1588899309|1588899147; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588899312',
#     'host':'www.zhihu.com',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

# cookies='zap=5d675a7c-a5c9-425c-8b24-8616ce6615de; d_c0="ACDW0mRX1xCPTo0qOTta_Ahl-WRf86-csJ8=|1582109222"; _ga=GA1.2.1573769491.1582677706; z_c0="2|1:0|10:1584694854|4:z_c0|92:Mi4xWExWekFBQUFBQUFBSU5iU1pGZlhFQ1lBQUFCZ0FsVk5SdFJoWHdCNVNvUWdsLTA4TTZBbDM1WTlvV240eE1UYTV3|a094296c8624912d71c7757620e1840d4b244921cad5235031a399bb078f1f20"; q_c1=4c740c0c79744595adbe15e2dea7987f|1584695951000|1584695951000; __utma=51854390.1573769491.1582677706.1585121232.1585121232.1; __utmz=51854390.1585121232.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/68263104; __utmv=51854390.100-1|2=registration_date=20140817=1^3=entry_date=20140817=1; _xsrf=537e766f-875b-40ae-90d7-0925568412e9; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1586332771,1586737268,1586919222,1588842381; tst=r; _gid=GA1.2.1758815139.1588842384; SESSIONID=KGzSoglMW71YG2JrLss6UDk6G2XB3wgjxwa1jNoSdfo; JOID=VV0cCklonsgRddDIEGbJVG9rW_MPIdWySR-1qF06q_VIOeeAbh0_d0Fy3sQbPRQxtE06_rlS_Z5Dpra09_-mPrE=; osd=Ul0VB0hvnsEcdNfIGWvIU29iVvIIIdy_SBi1oVA7rPVBNOaHbhQydkZy18kaOhQ4uUw9_rBf_JlDr7u18P-vM7A=; KLBRSID=3d7feb8a094c905a519e532f6843365f|1588899309|1588899147; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588899312',
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'host':'www.zhihu.com',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
# }
# for cookie in str(cookies).split(';'):
## cookies转换成str，否则报错'tuple' object has no attribute 'split'
#     key,value = cookie.split('=',1)
#     jar.set(key,value)
# r = requests.get("http://www.zhihu.com",cookies=jar,headers=headers)
# print(r.text)




