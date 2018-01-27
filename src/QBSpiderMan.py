from selenium import webdriver
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui

# 爬取qb
driver = webdriver.PhantomJS()
count = 0
for i in range(1, 4):
    str_Url = "http://www.qiushibaike.com/8hr/page/%s/?s=4967466" % i
    # driver.get("http://www.qiushibaike.com/")
    driver.get(str_Url)
    # http://www.qiushibaike.com/8hr/page/2/?s=4967466
    # http://www.qiushibaike.com/8hr/page/3/?s=4967466
    html = BeautifulSoup(driver.page_source, "html.parser")
    list_div = html.find_all("div", {"class": "content"})
    # print(html)
    # print(list_content)

    for content in list_div:
        print(content.get_text())
        print("*************************************************")
        count += 1

print("count = %d" % count)
driver.quit()

"""登录bugfree"""
# # 使用PhantomJS创建一个浏览器驱动
# driver = webdriver.PhantomJS()
# # 得到登录页面信息
# driver.get("http://192.168.1.2:8081/bugfree/index.php/site/login")
# # 最多等待10秒
# wait = ui.WebDriverWait(driver, 10)
# # 等待，直至页面显示用户名输入框
# wait.until(lambda dr: driver.find_element_by_id("LoginForm_username").is_displayed())
# # 得到用户名输入框，输入用户名
# driver.find_element_by_id("LoginForm_username").send_keys("xingyi")
# # 得到密码输入框，输入密码
# driver.find_element_by_id("LoginForm_password").send_keys("aa123321")
# # 得到登录按钮，触发点击事件
# driver.find_element_by_id("SubmitLoginBTN").click()
# # 等待，直至页面显示登录成功用户信息
# wait.until(lambda dr: driver.find_element_by_class_name("user-info").is_displayed())
#
# print(BeautifulSoup(driver.page_source, "html.parser"))

