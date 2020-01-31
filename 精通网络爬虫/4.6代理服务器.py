#!/usr/bin/python3
# encoding:utf-8

"""这节用的IP是动态的得自己去网页抓"""
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr="123.163.96.25:9999"
data=use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))