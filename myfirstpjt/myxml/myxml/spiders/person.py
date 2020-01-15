# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/pat12/test.xml']
    #网站已废
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        # item = {}
        item = MyxmlItem()
        item['link'] = selector.xpath('/person/email/text()').extract()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        print(item['link'])
        return item
