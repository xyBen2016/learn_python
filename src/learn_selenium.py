# # coding=utf-8
# from selenium import webdriver
# import selenium.webdriver.support.ui as ui
# import time
# #引入 Keys 类包
# from selenium.webdriver.common.keys import Keys
#
# # driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\Mozilla Firefox/geckodriver")
# # driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver")
# driver = webdriver.PhantomJS()
# html = driver.get("http://www.secomid.com/secomid-e/page/index.php")
# driver.maximize_window()
# print("driver.current_url: %s" % driver.current_url)
# # 最多等待10秒
# wait = ui.WebDriverWait(driver, 10)
# wait.until(lambda dr: driver.find_element_by_class_name("next").is_displayed())
# for i in range(1, 5):
#     driver.find_element_by_class_name("next").click()
#     time.sleep(1)
# driver.save_screenshot("a.png")
# # 得到登录按钮，触发点击事件
# driver.find_element_by_id("su").click()
# time.sleep(1)
# driver.save_screenshot("b.png")
# print("driver.current_url: %s" % driver.current_url)
# driver.quit()
#
# driver.maximize_window()  # 将浏览器最大化显示
# driver.set_window_size(480, 800)  # 参数数字为像素点
# driver.back()  # 返回（后退）到xx页
# driver.forward()  # 前进到xx页

'''当一个文字连接很长时，我们可以只取其中的一部分，只要取的部分可以唯一标识元素。一般一个页
面上不会出现相同的文件链接，通过文字链接来定位元素也是一种简单有效的定位方式。'''
# <a href="http://news.baidu.com" name="tj_news">新 闻</a>
# <a href="http://tieba.baidu.com" name="tj_tieba">贴 吧</a>
# <a href="http://zhidao.baidu.com" name="tj_zhidao">一个很长的文字连接</a>
# find_element_by_link_text("新 闻")
# find_element_by_partial_link_text("一个很长的")

# driver.find_element_by_id("user_name").clear()  # 清除元素的内容，如果可以的话
# driver.find_element_by_id("dl_an_submit").submit()  # 提交表单
# size = driver.find_element_by_id("kw").size  # 返回元素的尺寸。
# text = driver.find_element_by_id("cp").text  # 获取元素的文本
# attribute=driver.find_element_by_id("kw").get_attribute('type')  # 获得属性值
# result=driver.find_element_by_id("kw").is_displayed()  # 设置该元素是否用户可见

'''我们在实际的 web 产品测试中
发现，有关鼠标的操作，不单单只有单击，有时候还要和到右击，双击，拖动等操作，这些操作包含在
ActionChains 类中。这里需要注意的是，在使用 ActionChains 类下面的方法之前，要先将包引入'''
# from selenium.webdriver.common.action_chains import ActionChains
# ActionChains 类鼠标操作的常用方法：
#  context_click() 右击
#  double_click() 双击
#  drag_and_drop() 拖动
#  move_to_element() 鼠标悬停在一个元素上
#  click_and_hold() 按下鼠标左键在一个元素上
# #定位到要右击的元素
# right =driver.find_element_by_xpath("xx")
# #对定位到的元素执行鼠标右键操作
# ActionChains(driver).context_click(right).perform()
#
# #定位到要双击的元素
# double =driver.find_element_by_xpath("xxx")
# #对定位到的元素执行鼠标双击操作
# ActionChains(driver).double_click(double).perform()
#
# #定位元素的原位置
# element = driver.find_element_by_name("xxx")
# #定位元素要移动到的目标位置
# target = driver.find_element_by_name("xxx")
# #执行元素的移动操作
# ActionChains(driver).drag_and_drop(element, target).perform()
#
# #定位到鼠标移动到上面的元素
# above = driver.find_element_by_xpath("xxx")
# #对定位到的元素执行鼠标移动到上面的操作
# ActionChains(driver).move_to_element(above).perform()
#
# #定位到鼠标按下左键的元素
# left=driver.find_element_by_xpath("xxx")
# #对定位到的元素执行鼠标左键按下的操作
# ActionChains(driver).click_and_hold(left).perform()
#
#
# #输入空格键+“教程”
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# Keys.BACK_SPACE
#
# #ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# #ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# #输入框重新输入内容，搜索
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
# #通过回车键盘来代替点击操作
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

'''通常我们可以通过获得页面的 title 、URL 地址，页面上的标识性信息（如，登录成功的“欢迎，xxx”
信息）来判断用例执行成功。'''
# #获得前面 title，打印
# title = driver.title
# #获得前面 URL，打印
# now_url = driver.current_url
# #获得登录成功的用户，打印
# now_user=driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text
# print(now_user)


# sleep()：设置固定休眠时间。python 的 time 包提供了休眠方法 sleep() ，导入 time包后就可以使用 sleep()
# 进行脚本的执行过程进行休眠。
# implicitly_wait()：是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。
# 如果超出了设置时间的则抛出异常。
# WebDriverWait()：同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前
# 页面元素是否存在，如果超过设置时间检测不到则抛出异常。
#导入 WebDriverWait 包
# from selenium.webdriver.support.ui import WebDriverWait
# # #导入 time 包
# # import time
# element = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))
# element.send_keys("selenium")
# # 添加智能等待
# driver.implicitly_wait(30)
# driver.find_element_by_id("su").click()
# #添加固定休眠时间
# time.sleep(5)
# driver.quit()

'''switch_to_frame 的参数问题。官方说 name 是可以的，但是经过实验发现 id 也可以。所以只要 frame
中 id 和 name，那么处理起来是比较容易的。如果 frame 没有这两个属性的话，你可以直接手动添加。'''
# #先找到到 ifrome1（id = f1）
# driver.switch_to.frame("f1")
# #再找到其下面的 ifrome2(id =f2)
# driver.switch_to.frame("f2")
# 因为switch_to_frame()
# 只能使用name和id，如果没有name或id应该怎么处理呢？
# 此时可以使用xpath先对iframe进行定位：
# iframe = find_element_by_xpath（"//div/iframe"）
# 然后再使用switch_to_frame()函数：
# switch_to_frame(iframe)
# driver.switch_to_default_content()，返回到主content，也就是主界面中

'''窗口之间的切换'''
# #获得当前窗口
# nowhandle=driver.current_window_handle
# #打开注册新窗口
# driver.find_element_by_name("tj_reg").click()
# #获得所有窗口
# allhandles=driver.window_handles
# #循环判断窗口是否为当前窗口
# for handle in allhandles:
# if handle != nowhandle:
# driver.switch_to.window(handle)
# print 'now register window!'
# #切换到邮箱注册标签
# driver.find_element_by_id("mailRegTab").click()
# time.sleep(5)
# driver.close()
# #回到原先的窗口
# driver.switch_to.window(nowhandle)
# driver.find_element_by_id("kw").send_keys(u"注册成功！")
# time.sleep(3)
# driver.quit()


'''alert'''
# #接受警告信息
# alert = driver.switch_to.alert()
# alert.accept()
# #得到文本信息并打印
# alert = driver.switch_to.alert()
# print alert.text()
# #取消对话框（如果有的话）
# alert = driver.switch_to.alert()
# alert.dismiss()
# #输入值（如果有的话）
# alert = driver.switch_to.alert()
# alert.send_keys("xxx"")

'''上传文件'''
#定位上传按钮，添加本地文件
# driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload
# _file.txt')
# time.sleep(2)
# driver.quit()


'''执行JavaScript'''
# #######通过 JS 隐藏选中的元素##########第一种方法：
# execute_script(script, *args)
# 在当前窗口/框架 同步执行 javaScript
# script：JavaScript 的执行。
# *args：适用任何 JavaScript 脚本。
# #隐藏文字信息
# driver.execute_script('$("#tooltip").fadeOut();')
# time.sleep(5)
# #隐藏按钮：
# button = driver.find_element_by_class_name('btn')
# driver.execute_script('$(arguments[0]).fadeOut()',button)
# time.sleep(5)

'''滚动条'''
# #将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(3)
# #将滚动条移动到页面的顶部
# js_="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js_)
# time.sleep(3

'''获取对象的属性'''
# 选择页面上所有的 tag name 为 input 的元素
# inputs = driver.find_elements_by_tag_name('input')
# #然后循环遍历出 data-node 为594434493的元素，单击勾选
# for input in inputs:
# if input.get_attribute('data-node') == '594434493':
# input.click()

'''验证码问题'''
# 通过向浏览器中添加 cookie 可以绕过登录的验证码，这是比较有意思的一种解决方案。我们可以在
# 用户登录之前，通过 add_cookie(）方法将用户名密码写入浏览器 cookie ，再次访问系统登录链接将自
# 动登录。例如下面的方式：
# #访问 xxxx 网站
# driver.get("http://www.xxxx.cn/")
# #将用户名密码写入浏览器 cookie
# driver.add_cookie({'name':'Login_UserNumber', 'value':'username'})
# driver.add_cookie({'name':'Login_Passwd', 'value':'password'})
# #再次访问 xxxx 网站，将会自动登录
# driver.get("http://www.xxxx.cn/")
# time.sleep(3)
# ....
# driver.quit()


'''参数化csv'''
# import csv #导入 csv 包
# #读取本地 CSV 文件
# my_file='D:\\selenium_python\\data\\userinfo.csv'
# data=csv.reader(file(my_file,'rb'))
# #循环输出每一行信息
# for user in data:
#     print user[0]
#     print user[1]
#     print user[2]
#     print user[3]


'''异常断言'''
# try:
# print aa
# except NameError, msg:
# print msg

'''截图'''
#捕捉百度输入框异常
# try:
# browser.find_element_by_id("kwsss").send_keys("selenium")
# browser.find_element_by_id("su").click()
# except:
# browser.get_screenshot_as_file("/home/fnngj/python/error_png.png")


class Widget:

    def abc(self, a, b, c):
        print(a+b+c)

        return a+b+c
