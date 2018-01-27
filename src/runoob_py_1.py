# coding=utf-8
# print("hello world");
# print ("你好，世界");
# import time
#
# def lalala(inta,intb):
#     "print the str yeah"
#     inttemp = inta;
#     inta = intb;
#     intb = inttemp;
#
#     print("inner inta:",inta);
#     print("inner intb:", intb);

# list_a = [1,2,3,4,5];
# print(time.asctime(time.localtime()));
# print(list_a);

# hello = str.encode("hello","utf-8");
# file = open("a.txt","wb");
# file.write(bytes(hello));
# file.close();
#
# file = open("E:\\xy\\test\\pycharm\\pycharmWorkspace\\learnpython\\a.txt","r+");
# data = file.read();
# print(data);

# inta = 1;
# intb = 2;
# lalala(inta,intb);
#
# print("outter inta:", inta);
# print("outter intb:", intb);
# import json
#
# json.dump()

# from WebSpider_Xy import WebSpider_Xy
# import re
#
# webSpider = WebSpider_Xy()
# headers = {
#     "Host":"127.0.0.1",
#     "Connection":"keep-alive",
#     "Cache-Control":"max-age=0",
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding":"gzip, deflate, sdch, br",
#     "Accept-Language":"zh-CN,zh;q=0.8"
# }
# webSpider.headers = headers
# print(webSpider.getHTML("http://127.0.0.1/bugfree3.0.4/index.php/site/login"))
# # <img src=\"https://.*?.(jpg|png|gif)"
# # webSpider.easyWork_P("http://www.dytt8.net/",'<a href=\".*?\">.*?</a>',re.S)
# del webSpider
