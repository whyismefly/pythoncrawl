#!/usr/bin/python3
# encoding:utf-8

import re

patten="yue"
string="http://yum.iqianyue.com"
result=re.search(patten,string)
print(result)

patten1="\n"
string1='''http://yum.iqianyue.com
http://baidu.com'''
result1=re.search(patten1,string1)
print(result1)

patten2="\w"
patten3="\W"
patten4="\d"
patten5="\D"
patten6="\s"
patten7="\S"
patten8="\w\dpython\w"

print("----------")
string2="abcdefphp345pythony_ny"
result2=re.search(patten2,string2)
print(result2)
result3=re.search(patten3,string2)
print(result3)
result4=re.search(patten4,string2)
print(result4)
result5=re.search(patten5,string2)
print(result5)
result6=re.search(patten6,string2)
print(result6)
result7=re.search(patten7,string2)
print(result7)
result8=re.search(patten8,string2)
print(result8)


