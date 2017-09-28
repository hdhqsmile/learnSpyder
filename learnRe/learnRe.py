import re
match = re.search(r'[1-9]\d{5}', 'BTN 100081')
if match:
    print(match.group(0))
# 匹配结果要用if检测是否为空
# re函数 search match (从头位置开始) find_all(返回列表类型)
# re.split 将字符串按照正则表达式匹配结果进行分割
# re.finditer 迭代获得匹配的结果

for m in re.finditer(r'[1-9]\d{5}', 'BIU 100081,TSU 100084'):
    if m:
        print(m.group(0))

ls = re.findall(r'[1-9]\d{5}', 'BIU 100081,TSU 100084')
print(ls)

splitStr = re.split(r'[1-9]\d{5}', 'BIU 100081,TSU 100084')
print(splitStr)

splitStr = re.split(r'[1-9]\d{5}', 'BIU 100081,TSU 100084', maxsplit=1)
print(splitStr)

# re.sub() 用一个新的子串替换字符串中正则表达式匹配到的字符

str = 'BIU 100081,TSU 100084'
newStr = re.sub(r'[1-9]\d{5}', ':zipcode', str)
print(newStr)

#面向对象用法
pat = re.compile(r'[1-9]\d{5}') #将字符串编译成正则表达式
match = pat.search('BIU 100081,TSU 100084')

#Re库 默认采用贪婪匹配 即输出匹配最长的子串
m = re.search(r'PY.*N', 'PYANBNCNDN')
if m:
    print(m.group(0))

#最小匹配 需要用到操作符
'''
    *? 前一个字符 0-n次匹配，最小匹配
    +? 前一个字符 1-n次匹配，最小匹配
    ?? 前一个字符 0/1次匹配，最小匹配
    {m,n}? 扩展前一个字符m-n次匹配，最小匹配
'''

m = re.search(r'PY.*?N','PYANBNCNDN')
if m:
    print(m.group(0))