#!/usr/bin/python3
# encoding:utf-8

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
import requests
from selenium import webdriver
import redis
from random import choice
import json
from .utils import get_page
from pyquery import PyQuery as pq


# proxy = 'username:password@127.0.0.1:9743'
# proxy_handler = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# proxy = 'username:password@127.0.0.1:9743'
# proxies = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# })
# try:
#     response = requests.get('http://httpbin.org/get',proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error',e.args)

# proxy='127.0.0.1:9743'
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://'+proxy)
# browser=webdriver.Chrome(chrome_options=chrome_options)
# browser.get('http://httpbin.org/get')

# MAX_SCORE = 100
# MIN_SCORE = 0
# INITIAL_SCORE = 10
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# REDIS_PASSWORD = None
# REDIS_KEY = 'proxies'
#
#
# class RedisClient(object):
#     def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
#
#         self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
#
#     def add(self, proxy, score=INITIAL_SCORE):
#
#         if not self.db.zscore(REDIS_KEY, proxy):
#             return self.db.zadd(REDIS_KEY, score, proxy)
#
#     def random(self):
#
#         result = self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
#         if len(result):
#             return choice(result)
#         else:
#             result = self.db.zrevrange(REDIS_KEY, 0, 100)
#             if len(result):
#                 return choice(result)
#             else:
#                 raise PoolEmptyError
#
#     def decrease(self, proxy):
#
#         score = self.db.zscore(REDIS_KEY, proxy)
#         if score and score > MIN_SCORE:
#             print('代理', proxy, '当前分数', score, '减1')
#             return score.db.zincrby(REDIS_KEY, proxy, -1)
#         else:
#             print('代理', proxy, '当前分数', score, '移除')
#             return self.db.zrem(REDIS_KEY, proxy)
#
#     def exists(self, proxy):
#
#         return not self.db.zscore(REDIS_KEY, proxy) == None
#
#     def max(self, proxy):
#         print('代理', proxy, '可用，设置为', MAX_SCORE)
#         return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)
#
#     def count(self):
#
#         return self.db.zcard(REDIS_KEY)
#
#     def all(self):
#
#         return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)


