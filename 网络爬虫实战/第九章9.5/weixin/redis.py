#!/usr/bin/python3
# encoding:utf-8

from config import *
from pickle import dumps, loads
from request import WeixinRequest


class RedisQueue():
    def __init__(self):
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_HOST, password=REDIS_PASSWORD)

    def add(self, request):
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0
