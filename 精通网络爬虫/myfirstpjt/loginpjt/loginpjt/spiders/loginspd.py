# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest


class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}

    def start_requests(self):
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        # pass
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()
        if len(captcha)>0:
            print("yanzhengma")
            localpath="./captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print("qingshuru")
            captcha_value=input()
            data={
                #设置登录账号，格式为账号字段名:具体账号
                "form_email":"weisuen007@163.com",
                #设置登录密码，格式为密码字段名:具体密码，读者需要将账号密码换成自己的
                #因为笔者完成该项目后已经修改密码
                "form_password":"weijc7789",
                #设置验证码，格式为验证码字段名:具体验证码
                "captcha-solution":captcha_value,
                #设置需要转向的网址，由于我们需要爬取个人中心页，所以转向个人中心页
                "redir":"https://www.douban.com/people/151968962/",
            }
        else:
            print("meiyouyanzhengma")
            data = {
                "form_email": "weisuen007@163.com",
                "form_password": "weijc7789",
                "redir": "https://www.douban.com/people/151968962/",
            }
            print("dengluzhong")
            return [FormRequest.from_response(response,
                                              # 设置cookie信息
                                              meta={"cookiejar": response.meta["cookiejar"]},
                                              # 设置headers信息模拟成浏览器
                                              headers=self.header,
                                              # 设置post表单中的数据
                                              formdata=data,
                                              # 设置回调函数，此时回调函数为next()
                                              callback=self.next,
                                              )]
    def next(self,response):
        print("yiwanchengpaqu")
        xtitle="/html/head/title/text()"
        #日记标题Xpath表达式
        xnotetitle="//div[@class='note-header pl2']/a/@title"
        #日记发表时间Xpath表达式
        xnotetime="//div[@class='note-header pl2']//span[@class='pl']/text()"
        #日记内容Xpath表达式
        xnotecontent="//div[@class='mbtr2']/div[@class='note']/text()"
        #日记链接Xpath表达式
        xnoteurl="//div[@class='note-header pl2']/a/@href"

        title=response.xpath(xnotetitle).extract()
        notetitle = response.xpath(xnotetitle).extract()
        notetime = response.xpath(xnotetime).extract()
        notecontent = response.xpath(xnotecontent).extract()
        noteurl = response.xpath(xnoteurl).extract()
        print("网页标题是："+title[0])
        for i in range(0,len(notetitle)):
            print("第" + str(i + 1) + "篇文章的信息如下:")
            print("文章标题为：" + notetitle[i])
            print("文章发表时间为：" + notetime[i])
            print("文章内容为：" + notecontent[i])
            print("文章链接为：" + noteurl[i])
            print("------------")