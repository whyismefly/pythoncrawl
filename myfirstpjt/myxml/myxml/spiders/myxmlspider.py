# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from scrapy.spiders import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        # item = {}

        item=MyxmlItem()
        item['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        item['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        item['author'] = node.xpath("/rss/channel/item/author/text()").extract()

        for j in range(len(item['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是：")
            print(item['title'][j])
            print("对应链接是：")
            print(item['link'][j])
            print("对应作者是：")
            print(item['author'][j])
            print("___________________________")

        return item



