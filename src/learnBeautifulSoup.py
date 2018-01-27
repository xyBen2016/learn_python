'''
爬取豆瓣图片
from bs4 import BeautifulSoup
import urllib.request,os

targetPath = "E:/logs/webspider"
cntImg = 1

def saveFile(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    pos = path.rindex('/')
    t = os.path.join(targetPath, str(cntImg)+"_"+path[pos + 1:])
    return t

if __name__ == '__main__':
    destUrl = "https://www.douban.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36',
    }

    req = urllib.request.Request(url=destUrl, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read()
    # data = str(data,"utf-8")
    # if data is str:print("data is str")
    # print(data)

    soup = BeautifulSoup(data, "html.parser")

    for linkImg in soup.findAll("img"):
        urlImg = linkImg.get("src")
        print(urlImg)
        try:
            urllib.request.urlretrieve(urlImg, saveFile(urlImg))
            cntImg += 1
        except:
            print('失败')

    # print(soup.prettify())
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.title.parent.name)
    # print(soup.p)
    # print(soup.p['class'])
    # print(soup.a)
    # print(soup.findAll('a'))
    # print(soup.findAll(id="anony-nav"))

'''
# 爬取糗事百科
import urllib.request
from bs4 import BeautifulSoup

destUrl = "http://www.qiushibaike.com/8hr/page/1/?s=4925119"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36'
}
for pageNum in range(1, 3):
    destUrl = "http://www.qiushibaike.com/8hr/page/%d/?s=4925119" % pageNum

    req = urllib.request.Request(url=destUrl, headers=headers)
    res = urllib.request.urlopen(req)
    data = str(res.read(), "utf-8")
    soup = BeautifulSoup(data, "html.parser")
    list_res = soup.findAll("div", {"class": "content"})
    file = open("a.txt", "ab")

    for htmlTag in list_res:
        content = htmlTag.span.get_text() + "\r\n"
        print(content)
        file.write(bytes(content + "\r\n", encoding='utf-8'))

    file.close()
