#!/usr/bin/python3
# encoding:utf-8

import retest

patten="yue"
string="http://yum.iqianyue.com"
result=retest.search(patten, string)
print(result)

patten1="\n"
string1='''http://yum.iqianyue.com
http://baidu.com'''
result1=retest.search(patten1, string1)
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
result2=retest.search(patten2, string2)
print(result2)
result3=retest.search(patten3, string2)
print(result3)
result4=retest.search(patten4, string2)
print(result4)
result5=retest.search(patten5, string2)
print(result5)
result6=retest.search(patten6, string2)
print(result6)
result7=retest.search(patten7, string2)
print(result7)
result8=retest.search(patten8, string2)
print(result8)

print("----------")
pattern9="\w\dpython[xyz]\w"
pattern10="\w\dpython[^xyz]\w"
pattern11="\w\dpython[xyz]\W"
result9=retest.search(pattern9, string2)
result10=retest.search(pattern10, string2)
result11=retest.search(pattern11, string2)
print(result9)
print(result10)
print(result11)

print("----------")
pattern12=".python..."
result12=retest.search(pattern12, string2)
print(result12)

print("----------")
patternl="^abd"
pattern2="^abc"
pattern3="py$"
pattern4="ay$"
string="abcdfphp345pythony_py"
resultl=retest.search(patternl, string)
result2=retest.search(pattern2, string)
result3=retest.search(pattern3, string)
result4=retest.search(pattern4, string)
print(resultl)
print(result2)
print(result3)
print(result4)

print("----------")
patternl="py.*n"
pattern2="cd{2}"
pattern3="cd{3}"
pattern4="cd{2,}"
string="abcdddfphp345pythony_py"
resultl=retest.search(patternl, string)
result2=retest.search(pattern2, string)
result3=retest.search(pattern3, string)
result4=retest.search(pattern4, string)
print(resultl)
print(result2)
print(result3)
print(result4)

print("----------")
pattern="python|php"
string="abcdfphp345pythony_py"
resultl=retest.search(pattern, string)
print(resultl)

print("----------")
pattern21="(cd){1,}"
pattern22="cd{1,}"
string21="abcdcdcdcdfphp345pythony_py"
result2l=retest.search(pattern21, string21)
result22=retest.search(pattern22, string21)
print(result2l)
print(result22)

print("----------")
patternl="python"
pattern2="python"
string="abcdfphp345Pythony_py"
resultl=retest.search(patternl, string)
result2=retest.search(pattern2, string, retest.I)
print(resultl)
print(result2)

print("----------")
patternl="p.*y"#贪婪模式
pattern2="p.*?y"#懒惰模式
string="abcdfphp345pythony_py"
resultl=retest.search(patternl, string)
result2=retest.search(pattern2, string)
print(resultl)
print(result2)


print("----------")
string="apythonhellomypythonhispythonourpythonend"
pattern=".python."
result=retest.match(pattern, string)
result2=retest.match(pattern, string).span()
print(result)
print(result2)

print("----------")
string="hellomypythonhispythonourpythonend"
pattern=".python."
result=retest.match(pattern, string)
result2=retest.search(pattern, string)
print(result)
print(result2)

print("----------")
string="hellomypythonhispythonourpythonend"
pattern=retest.compile(".python.")#预编译
result=pattern.findall(string)#找出符合模式的所有结果
print(result)
result=retest.compile(".python.").findall(string)
print(result)

print("----------")
pattern="python."
resultl=retest.sub(pattern, "php", string)#全部替换
result2=retest.sub(pattern, "php", string, 2)#最多替换两次


