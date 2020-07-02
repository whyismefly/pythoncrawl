#!/usr/bin/python3
# encoding:utf-8

from pickle import dumps,loads
from request import WeixinRequest

class RedisQuere():
    def __init__(self):
        self.db = StrictRedis(host=REDIS_HOST)