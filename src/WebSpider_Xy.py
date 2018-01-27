import urllib.request, gzip, re

class WebSpider_Xy:
    "this is a web spider class"
    __headers = {}
    __url = ""

    def __init__(self):
        self.headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8"
        }

    # def __init__(self, headers):
    #     self.headers = headers
    #
    # def __init__(self, headers, url):
    #     self.headers = headers
    #     self.url = url

    def getHeaders(self):
        return self.headers

    def setHeaders(self, headers):
        self.headers = headers

    def getUrl(self):
        return self.headers

    def setUrl(self, url):
        self.url = url

    def getHTML(self, url):
        "return utf-8 data string"
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        return response.read().decode("utf-8")

    def getGzipHTML(self, url):
        "return utf-8 data string"
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        return gzip.decompress(response.read()).decode("utf-8")

    def filterHTML(self, htmlStr, pattern, flag):
        "return an list of result"
        # '<div class=\"content\">.*?<span.*?/span>'
        # re.S
        parrten = re.compile(pattern, flag)
        return re.findall(parrten, htmlStr)

    def saveFile(self, fileName, content, mode, encode):
        "save files to a txt"
        file = open(fileName, mode)
        file.write(bytes(str.encode(content, encode)))
        file.close()

    def saveFiles(self, fileName, list, mode, encode):
        "save files to a txt"
        file = open(fileName, mode)
        for content in list:
            file.write(bytes(str.encode(content, encode)))
        file.close()

    def printList(self, list):
        "print all elements in list"
        for content in list:
            print(content)

    def __str__(self):
        "return an string of web spider args"
        return "headers:" + str(self.headers) + "\n" + "url:" + self.url

    def easyWork_gzip_P(self, url, pattern, flag):
        "easy work and print"
        self.url = url
        data = self.getGzipHTML(self.url)
        list_result = self.filterHTML(data, pattern, flag)
        self.printList(list_result)

    def easyWork_P(self, url, pattern, flag):
        "easy work and print"
        self.url = url
        data = self.getHTML(self.url)
        list_result = self.filterHTML(data, pattern, flag)
        self.printList(list_result)

    def easyWork_S(self, url, pattern, flag, fileName, mode, encode):
        "easy work and save"
        self.url = url
        data = self.getHTML(self.url)
        list_result = self.filterHTML(data, pattern, flag)
        self.saveFiles(fileName, list_result, mode, encode)
