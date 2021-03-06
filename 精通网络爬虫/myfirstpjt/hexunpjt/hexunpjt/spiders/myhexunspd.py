# -*- coding: utf-8 -*-
import scrapy
import retest
import urllib.request
from hexunpjt.items import HexunpjtItem
from scrapy.http import Request

class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    # start_urls = ['http://hexun.com/']
    # uid = "19940007"
    uid = "shihanbingblog"

    def start_requests(self):
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",
                      headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,"
                                               " like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})

    def parse(self, response):
        # pass
        item = HexunpjtItem()
        item['name']=response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item["url"]=response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()

        pat1='<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        hcurl=retest.compile(pat1).findall(str(response.body))[0]
        headers2 = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers2]
        # 将opener安装为全局
        urllib.request.install_opener(opener)
        #data为对应博客列表页的所有博文的点击数与评论数数据
        data=urllib.request.urlopen(hcurl).read()
        #pat2为提取文章阅读数的正则表达式
        pat2="click\d*?','(\d*?)'"
        #pat3为提取文章评论数的正则表达式
        pat3="comment\d*?','(\d*?)'"
        #提取阅读数和评论数数据并分别赋值给item下的hits和comment
        item["hits"]=retest.compile(pat2).findall(str(data))
        item["comment"]=retest.compile(pat3).findall(str(data))
        yield item
        #提取博文列表页的总页数
        pat4="blog.hexun.com/p(.*?)/"
        #通过正则表达式获取到的数据为一个列表，倒数第二个元素为总页数
        data2=retest.compile(pat4).findall(str(response.body))
        if(len(data2)>=2):
            totalurl=data2[-2]
        else:
            totalurl=1
        #在实际运行中，下一行print的代码可以注释掉，在调试过程中，可以开启下一行print的代码
        #print("一共"+str(totalurl)+"页")
        #进入for循环，依次爬取各博文列表页的博文数据
        for i in range(2,int(totalurl)+1):
            #构造下一次要爬取的url，爬取一下页博文列表页中的数据
            nexturl="http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            #进行下一次爬取，下一次爬取仍然模拟成浏览器进行
            yield Request(nexturl,callback=self.parse,headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})
