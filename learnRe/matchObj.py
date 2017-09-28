import re
pat = re.compile(r'[1-9]\d{5}')
match = pat.search('BIT 100081,BTU 100084')

#match 对象介绍 match 返回第一次匹配结果
if match:
    print(match.group(0)) #匹配到的结果
    print(match.pos)
    print(match.endpos)
    print(match.start()) #匹配到的开始字符位置
    print(match.end()) #匹配到的结束字符位置
    print(match.string) #待匹配的字符串
