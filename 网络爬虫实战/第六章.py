#!/usr/bin/python3
# encoding:utf-8

# import requests
# from pyquery import PyQuery as pq
# from urllib.parse import urlencode
# from pymongo import MongoClient
#
# base_url='https://m.weibo.cn/api/container/getIndex?'
#
# headers={
#     'host':'m.weibo.cn',
#     'referer':'https://m.weibo.cn/u/2830678474',
#     'user-agent':'_T_WM=26155091068; ALF=1593130388; XSRF-TOKEN=b507bb; WEIBOCN_FROM=1110006030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh3B.-AosTJLXS9Em.Lx7o25JpX5K-hUgL.FozceKzX1hMX1KM2dJLoIEBLxKnL12qLBozLxKML1h2LB-zLxKqLBo-L1h2LxKBLB.2L1K2t; MLOGIN=1; SCF=Aq6zpBgormkFlKSi_kdUwNudIvo14Qbm7SC8zAI4xflEAhn5Shm-IbnWGB3dUjwj65aoPlGy2GN1flnLCpqYUWU.; SUB=_2A25zylgPDeRhGeRI6lAV-CnIwjuIHXVRNXhHrDV6PUJbktANLXjFkW1NUt43xGH04CEkIyjbyMacse0UBLDePgFI; SUHB=0tKrKw4ERt2orM; SSOLoginState=1590569056; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032830678474%26fid%3D1076032830678474%26uicode%3D10000011',
#     'x-requested-with':'xmlhttprequest',
# }
#
# client = MongoClient()
# db = client['weibo']
# collection = db['weibo']
# max_page = 10
#
# def get_page(page):
#     params={
#         'type':'uid',
#         'value': '2830678474',
#         'containerid': '1076032830678474',
#         'page': page
#     }
#     url=base_url+urlencode(params)
#     try:
#         response=requests.get(url,headers=headers)
#         if response.status_code==200:
#             return response.json()
#     except requests.ConnectionError as e:
#         print('error',e.args)
#
# def parse_page(json):
#     if json:
#         items = json.get('data').get('cards')
#         for item in items:
#             item=item.get('mblog')
#             weibo={}
#             weibo['id']=item.get('id')
#             weibo['text']=pq(item.get('text')).text()
#             weibo['attitudes']=item.get('attitudes_count')
#             weibo['comments']=item.get('comments_count')
#             weibo['reposts']=item.get('reposts_cpunt')
#             yield weibo
#
# def save_to_mongo(result):
#     if collection.insert(result):
#         print('Saved to Mongo')
#
# if __name__=='__main__':
#     for page in range(1,11):
#         json = get_page(page)
#         results = parse_page(json)
#         for result in results:
#             print(result)
#             save_to_mongo(result)

import requests
from urllib.parse import urlencode
from hashlib import md5
import os

def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
    }
    url='http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        title = item.get('data')
        images = item.get('title')
        for image in images:
            yield {
                'image':image.get('url'),
                'title':title
            }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path=''





