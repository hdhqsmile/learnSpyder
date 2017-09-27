import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.find_all(['a','b']))
for tag in soup.find_all(True):
    print(tag.name)
for link in soup.find_all('a'):
    print(link.get('href'))

soup.find_all('p','course')

