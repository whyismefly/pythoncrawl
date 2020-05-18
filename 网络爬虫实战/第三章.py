#!/usr/bin/python3
# encoding:utf-8

import http.cookiejar, urllib.request

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

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)


# from requests.packages import urllib3
#
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


# proxies = {
#     'http': "http://10.10.1.10:3128",
#     'https': "http://10.10.1.10:1080",
# }
# requests.get("https://www.taobao.com", proxies=proxies)

# from requests.auth import HTTPBasicAuth
#
# r=requests.get('http://localhost:5000',auth=HTTPBasicAuth('whyismefly','1q2w3e4r5t6y'))
# print(r.status_code)#yichang

from requests import Request, Session

# url = 'http://httpbin.org/post'
# data = {
#     'name': 'germey'
# }
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
# }
# s = Session()
# req = Request('post', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)

import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.search('<Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())  # 'NoneType' object has no attribute 'group'
# print(result.span())

# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))

# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())

# content = 'http://weibo.com/comment/kEraCN'
# resultl = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('resultl', resultl.group(1))
# print('result2', result2.group(1))

# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*?Demo$', content,re.S)
# print(result.group(1))
# print(result.span())

# content="(百度)www.baidu.com"
# result = re.match('\(百度\)www\.baidu\.com',content)
# print(result)

# html ='''＜ div id="songs-list" >
# <h2 class ＝Title ”〉经典老歌＜／ h2>
# <p class=” introduction ”>
# 经典老歌y1J 农
# <Ip>
# <ul id=” list” class=” list-group”>
# <li data-view="2 ”〉一路上有你＜／ li>
# <li data-view="7 ”>
# <a href ＝”／ 2.mp3 ” singer="任贤齐">沧海一卢笑</a>
# </li>
# <li data-view=” 4 ” class=” active">
# 。href ＝”／ 3 .mp3 ” singer="齐泰">往事随风</a>
# </li>
# <li data-view ＝飞”＞＜ a href="/4.mp3 " singer="beyo nd ">尤辉岁月</a><lli>
# <li data-view=” 5”>< a href="/S.mp3 ” singer~ ”除A也琳”〉记事本＜／ a><lli>
# <li data-view=” 5’'>
# 。href ＝”／ 6.mp3 ” singer ＝”邓丽君、但愿人长久＜ l a>
# <lli>
# </ul>
# </div>'''
# result=re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(0),result.group(1),result.group(2))
#     print(result.group())

# results= re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0],result[1],result[2])

# content1='2016-12-15 12:00'
# content2='2016-12-17 12:55'
# content3='2016-12-22 13:21'
# pattern=re.compile('\d{2}:\d{2}')
# result1=re.sub(pattern,'',content1)
# result2=re.sub(pattern,'',content2)
# result3=re.sub(pattern,'',content3)
# print(result1,result2,result3)

#3.4
import time
from requests.exceptions import RequestException
import json
def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None
def main():
    url='http://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<a.*?src="(.*?)">.*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items=re.findall(pattern,html)
    print(items)
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:]if len(item[3])>3 else '',
            'time': item[4].strip()[5:]if len(item[4])>5 else '',
            'score': item[5].strip()+item[6].strip()
        }
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
























