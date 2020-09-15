#!/usr/bin/python3
# encoding:utf-8

import retest

pattern="'[a-zA-Z]+://[^\s]*[.com|.cn]"
string="<a href=http://www.baidu.com'>百度首页</a>"
result=retest.search(pattern, string)
print(result)

pattern="\d{4}-\d{7}|\d{3}-\d{8}"
string="010-465134161651131315421"
result=retest.search(pattern, string)
print(result)

pattern="\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
# pattern="([.+-]\w+)"
string="<a href ＝'http://www.baidu.com'>百度首页<／a><br><a href='mailto:c-e+o@iqianyue.com.cn'>电子邮件地址<／a>"
result=retest.search(pattern, string)
print(result)


