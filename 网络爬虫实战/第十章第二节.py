# ！usr/bin/python3
# encoding:utf-8

# import random
# import redis
#
#
# class RedisClient(object):
#     def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT, password=RADIS_PASSWORD):
#         self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
#         self.type = type
#         self.website = website
#
#     def name(self):
#         return '{type}:{website}'.format(type=self.type, website=self.website)
#
#     def set(self, username, value):
#         return self.db.hset(self.name(), username, value)
#
#     def get(self, username):
#         return self.db.hget(self.name(), username)
#
#     def delete(self, username):
#         return self.db.hdel(self.name(), username)
#
#     def count(self):
#         return self.db.hlen(self.name())
#
#     def random(self):
#         return random.choice(self.db.hvals(self.name()))
#
#     def username(self):
#         return self.db.hkeys(self.name())
#
#     def all(self):
#         return self.db.hgetall(self.name())

# import json
# import requests
# from requests.exceptions import ConnectionError
#
#
# class WeiboValidTester(ValidTester):
#     def __init__(self, weibo='weibo'):
#         ValidTester.__init__(self, website)
#
#     def test(self, username, cookies):
#         print('testing cookies', 'name', username)
#         try:
#             cookies = json.loads(cookies)
#         except TypeError:
#             print('cookies inligil', username)
#             self.cookies_db.delete(username)
#             print('delete cookies', username)
#             return
#         try:
#             test_url = TEST_URL_MAP[self.website]
#             response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
#             if response.status_code == 200:
#                 print('cookies ok', username)
#                 print('part ok', response.text[0:50])
#             else:
#                 print(response.status_code, response.headers)
#                 print('cookies not ok', username)
#                 self.cookies_db.delete(username)
#         except ConnectionError as e:
#             print('exception', e.args)


import json
from flask import Flask, g

app = Flask(__name__)
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}


@app.route('/')
def index():
    return '<h2>cookie pool</h2>'


def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('redisclient' + '("cookies","' + website + '")'))
            return g


@app.route('/')
def random(website):
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies
