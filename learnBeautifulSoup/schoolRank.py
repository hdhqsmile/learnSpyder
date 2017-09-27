import requests
from bs4 import BeautifulSoup
url="http://zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

for tbody in soup.find_all('tbody'):
    for child in tbody.contents:
        if not child.name == None:
            for td in child.find_all('td'):


