'''
爬取电玩巴士xbox360所有游戏
'''
import requests
from bs4 import BeautifulSoup

"""下载图片"""
# pic_url = "http://cp1.douguo.net/upload/caiku/5/6/b/600x400_561ed01b40507e04adbc3b180a7b6b4b.jpg"
# try:
#     pic = requests.get(pic_url, timeout=10)
# except requests.exceptions.ConnectionError:
#     print("【错误】当前图片无法下载")
# file = open(r"C:\Users\Administrator\Desktop\caipu\donwload.jpg", "wb")
# file.write(pic.content)
# file.close()

# class Game:
#     gName = ""
#     gDetail = ""
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "gName:%s gDetail:%s" % (self.gName, self.gDetail)
#
#     def show(self):
#         print(self.__str__())
#
#
# def saveFile(listGame):
#     file = open("game.txt", "ab")
#     for game in listGame:
#         file.write(bytes(game.__str__() + "\r\n", "utf-8"))
#
#     file.close()
#
#
# if __name__ == "__main__":
#
#     for pageNum in range(73):
#         destUrl = 'http://games.tgbus.com/default.aspx?page=%d&elite=0&keyword=&type=0&tag=0&nid=33' % pageNum
#         res = requests.get(destUrl)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         listDiv = soup.findAll("div", {"class": "ml left"})
#         listGame = []
#
#         for content in listDiv:
#             gName = ""
#             aHtml = content.find("a", {"target": "_blank"})
#             if aHtml != None:
#                 gName = aHtml.string
#             # gName = content.find("a",{"target":"_blank"}).string
#             game = Game()
#             game.gName = gName
#             gDl = content.find("dl")
#             listStr = []
#             for dd in gDl.findAll("dd"):
#                 listStr.append(dd.get_text())
#
#             game.gDetail = "".join(listStr)
#             game.show()
#             listGame.append(game)
#
#         saveFile(listGame)
