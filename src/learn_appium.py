from appium import webdriver

# 计算器
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.2'
desired_caps['deviceName'] = '192.168.1.120:5555'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_id("del").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()

# result = driver.find_element_by_id("formula").text
# print(result)
# assert result == "1601"
driver.quit()


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.2'
# desired_caps['deviceName'] = '0123456789ABCDEF'
# desired_caps['appPackage'] = 'com.secomid.smarthood_phone'
# desired_caps['appActivity'] = '.LoginActivity'  # .homepage.HomeActivity
# # desired_caps['waitActivity'] = '.homepage.HomeActivity'
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#
# driver.find_element_by_id("login_edit_account").send_keys("xy001")
# driver.find_element_by_id("login_edit_password").send_keys("888888")
# driver.find_element_by_id("login_btn_login").click()
#
# driver.find_element_by_id("item_mine").click()
# driver.quit()