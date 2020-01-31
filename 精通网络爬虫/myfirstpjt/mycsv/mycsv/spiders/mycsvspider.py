# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    # delimiter = '\t'
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        # i = {}
        #i['url'] = row['url']
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        print("name:")
        print(i['name'])
        print("sex:")
        print(i['sex'])
        print("___________________________")
        #i['description'] = row['description']
        return i
