import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    html = ""
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取信息失败")
        return ""


def fillUnivList(uList, html):
    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[1].string, tds[3].string])


def printUnivList(uList, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "大学名称", "总分"))
    for i in range(num):
        u = uList[i]
        # print(u)
        print("{:^10}\t{:^6}\t{:^10}".format(i + 1, u[0], u[1]))


if __name__ == "__main__":
    uinfo = []
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
