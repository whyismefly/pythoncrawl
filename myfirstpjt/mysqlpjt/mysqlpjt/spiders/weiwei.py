# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysqlpjt.mysqlpjt.items import MysqlpjtItem


class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MysqlpjtItem()
        item["name"]=response.xpath("/html/head/title/text()").extract()
        item["keywd"]=response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
