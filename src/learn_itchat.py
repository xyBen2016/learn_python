import itchat
import re
import time
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS])
def text_reply(msg):
    if msg["Type"] == "Text":
        reply_content = msg["Text"]
    print(msg["Text"])
    friend = itchat.search_friends(userName=msg["FromUserName"])
    itchat.send(r"Friend:%s -- %s"
                r"Time:%s   "
                r"Message:%s" % (friend["NickName"], friend["RemarkName"], time.ctime(), reply_content),
                toUserName="filehelper")
    itchat.send(r"I'v got the message you send at [%s],[%s]please wait for a second.wxhelper code by python" % (
        time.ctime(), reply_content), toUserName=msg["FromUserName"])


itchat.auto_login()
itchat.run()
