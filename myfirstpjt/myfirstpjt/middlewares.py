# -*- coding: utf-8 -*-

import random
from  myfirstpjt.settings import IPPOOL
# from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class IPPOOLS(HttpProxyMiddleware):

    def __init__(self,ip=''):
        self.ip=ip

    def process_request(self,request,spider):
        thisip=random.choice(IPPOOL)
        print("IP:"+thisip["ipaddr"])
        request.mate["proxy"]="http://"+thisip["ipaddr"]