# -*- coding: utf-8 -*-
import scrapy
import retest
from qtpjt.items import QtpjtItem
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.comtb/']

    def parse(self, response):
        # pass
        item = QtpjtItem()
        paturl="(http://pic.qiantucdn.com/58pic/.*?).jpg"
        item["picurl"] = retest.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item["picid"] = retest.compile(patlocal).findall(str(response.body))
        yield item
        for i in range(1,201):
            nexturl="http://www.58pic.com/tb/id-"+str(i)+".html"
            yield Request(nexturl,callback=self.parse)