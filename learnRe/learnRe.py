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
