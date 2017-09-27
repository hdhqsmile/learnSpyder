import requests


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)

    except:
        return "产生异常"


if __name__ == "__main__":
    print("main 函数")
    url = "http://www.baidu.com"
    getHTMLText(url)

