import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.126.com"
mail_user = "xingyi_90@126.com"
mail_pwd = "xingyi251"

sender = "webspiderman"
receivers = ["xingyi_90@126.com"]

message = MIMEText('hello world', 'plain', 'utf-8')
message['From'] = Header('webspiderman', 'utf-8')
message['To'] = Header('webspiderman', 'utf-8')

subject = 'this is an subject'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("send email successed")
    smtpObj.quit()
except smtplib.SMTPException:
    print("send email fail")


# import os
# import datetime
# import time
#
# result_dir = 'E:\\xy\\test\\pycharm\\pycharmWorkspace\\selenium_testcase\\report'
# lists = os.listdir(result_dir)
# lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
# print('最新的文件为： ' + lists[-1])
# file = os.path.join(result_dir, lists[-1])
# print(file)
