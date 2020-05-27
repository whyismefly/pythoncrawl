#!/usr/bin/python3
# encoding:utf-8

from urllib.parse import urlencode
import requests
base_url='https://m.weibo.cn/api/container/getIndex'

headers={
    'host':'m.weibo.cn',
    'referer':'https://m.weibo.cn/u/2830678474',
    'user-agent':'_T_WM=26155091068; ALF=1593130388; XSRF-TOKEN=b507bb; WEIBOCN_FROM=1110006030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh3B.-AosTJLXS9Em.Lx7o25JpX5K-hUgL.FozceKzX1hMX1KM2dJLoIEBLxKnL12qLBozLxKML1h2LB-zLxKqLBo-L1h2LxKBLB.2L1K2t; MLOGIN=1; SCF=Aq6zpBgormkFlKSi_kdUwNudIvo14Qbm7SC8zAI4xflEAhn5Shm-IbnWGB3dUjwj65aoPlGy2GN1flnLCpqYUWU.; SUB=_2A25zylgPDeRhGeRI6lAV-CnIwjuIHXVRNXhHrDV6PUJbktANLXjFkW1NUt43xGH04CEkIyjbyMacse0UBLDePgFI; SUHB=0tKrKw4ERt2orM; SSOLoginState=1590569056; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032830678474%26fid%3D1076032830678474%26uicode%3D10000011',
    'x-requested-with':'xmlhttprequest',
}

def get_page(page):
    params={
        'type':'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('errior',e.args)




