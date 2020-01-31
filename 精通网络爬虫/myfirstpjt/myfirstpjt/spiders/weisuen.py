# -*- coding: utf-8 -*-
import scrapy
# import sys
# sys.path.append()
#在jetbrain中用scrapy经常出路找不到包的情况要么通过sys添加路径要么用下面的方法解决
# https://blog.csdn.net/weixin_41931602/article/details/80181045
# 估计很多人和我遇到过这样的坑，就是scrapy做爬虫时，导入Module的时候总显示no module named ×××.items？可是检查很多遍都没发现什么大问题啊？
# 我明明是按照教程来打的案例！！！
# 原来这是因为编译器的问题，pycharm不会将当前文件目录自动加入自己的sourse_path。
# 那么具体的解决方法如下：
# 1,找到你的scrapy项目上右键
# 2.然后点击make_directory as
# 3.最后点击sources root
# 4.看到文件夹编程蓝色就成功了


from myfirstpjt.items import MyfirstpjtItem

# class WeisuenSpider(scrapy.Spider):
#     name = 'weisuen'
#     allowed_domains = ['iqianyue.com']
#     start_urls = ['http://iqianyue.com/']
#
#     def parse(self, response):
#         pass

class WeisuenSpider(scrapy.Spider):
    name="weisuen"
    allowed_domains=["sina.com.cn"]
    start_urls=(
    'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
    'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
    'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',
)
    # urls2=("http://www.jd.com",
    #        "http://sina.com.cn",
    #        "http://yum.iqianyue.com",
    # )

# def __init__(self,myurl=None,*args,**kwargs):
#     super(WeisuenSpider,self).__init__(*args,**kwargs)
#     print("要爬取的网址为:%s"%myurl)
#     self.start_urls=["%s"%myurl]

def __init__(self,myurl=None,*args,**kwargs):
    super(WeisuenSpider,self).__init__(*args,**kwargs)
    myurllist=myurl.split("|")
    for i in myurllist:
        print("要爬取的网址为:%s"%myurl)
    self.start_urls=myurllist

# def start_requests(self):
#     for url in self.urls2:
#         yield self.make_requests_from_url(url)

def parse(self,response):
    item=MyfirstpjtItem()
    item["urlname"]=response.xpath("/html/head/title/text()")
    print("标题：")
    print(item["urlname"])

#12.8见myxml