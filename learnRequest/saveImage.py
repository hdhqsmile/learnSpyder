import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/0904/20170904023103897.jpg"
root = "/Users/Diane/Pictures/"
path =root+url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        print(path)
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
