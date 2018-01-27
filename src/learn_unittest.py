# coding=utf-8
import HTMLTestRunner
from learn_selenium import Widget
import unittest

# 执行测试的类


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget = None

    def testABC(self):
        self.assertEqual(self.widget.abc(1, 2, 3), 6)


# 测试
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testABC"))

    # 定义个报告存放路径，支持相对路径
    filename = 'E:\\logs\\selenium_report\\result.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：')

    # 执行测试
    runner.run(suite)

'''PyUnit 模块中定义了一个名为 main 的全局方法，使用它可以很方便地将一个单元测试模块变成可
以直接运行的测试脚本，main()方法使用 TestLoader 类来搜索所有包含在该模块中的测试方法，并自
动执行它们。如果 Python 程序员能够按照约定（以 test 开头）来命名所有的测试方法，那就只需要在
测试模块的最后加入如下几行代码即可：'''
# # 测试
# if __name__ == "__main__":
# unittest.main()

'''批量执行测试用例'''
#-*-coding=utf-8 -*-
# import os
# #列出某个文件夹下的所有 case,这里用的是 python，
# #所在 py 文件运行一次后会生成一个 pyc 的副本
# caselist=os.listdir('D:\\selenium_use_case\\test_case')
# for a in caselist:
# s=a.split('.')[1] #选取后缀名为 py 的文件
# if s=='py':
# #此处执行 dos 命令并将结果保存到 log.txt
# os.system('D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)

'''测试套件没执行多个py'''
# #coding=utf-8
# import unittest
# #这里需要导入测试文件
# # baidu,youdao使用if __name__ == "__main__":unittest.main()执行

# import baidu,youdao
# testunit=unittest.TestSuite()
# #将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))
# #执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

'''为每一个test方法添加注释,以方便生成的htmltestrunner报告提升可读性'''
#百度搜索用例
# def test_baidu_search(self):
#     u"""百度搜索"""
#     driver = self.driver
#     driver.get(self.base_url + "/")


''' 报告文件名取当前时间'''
# time.time() 获取当前时间戳
# time.localtime() 当前时间的 struct_time 形式
# time.ctime() 当前时间的字符串形式
# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


#取前面时间
# now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
# #把当前时间加到报告中
# filename = "D:\\selenium_python\\report\\"+now+'result.html'
# fp = file(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(
# stream=fp,
# title=u'百度搜索测试报告',
# description=u'用例执行情况：')


'''目录结构
/selenium/testcase/a.py
                  /b.py
                  /c.py
                  /login.py
                  /quit.py
                  /__init__.py
         /data/user.csv
         /test_all_case.py
我们把 D:\selenium_python\test_cast 目录添加到
系统 path 下，就可以正常的调用了。为了标识一下目录是可引用的包，那么就需要在目录下创建一个
__init__.py 文件。
'''

# #coding=utf-8
# import unittest
# #把 test_case 目录添加到 path 下，这里用的相对路径
# import sys
# sys.path.append("\test_case")
# from test_case import youdao
# from test_case import baidu
# #这里需要导入测试文件
# import baidu,youdao

'''找到所有的用例，并执行'''
listaa='D:\\selenium_python\\test_case'
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(listaa,
    pattern ='start_*.py',
    top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)

    return testunit
alltestnames = creatsuitel()
now = time.strftime(' %Y-%m-%M-%H_%M_%S ',time.localtime(time.time()))
filename = 'D:\\selenium_python\\report\\'+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'百度搜索测试报告',
description=u'用例执行情况：')
#执行测试用例
runner.run(alltestnames)

