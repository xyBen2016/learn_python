from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox(executable_path = 'C:/Program Files (x86)/Mozilla Firefox/geckodriver');
# browser = webdriver.Firefox();
browser.get("http://127.0.0.1/bugfree3.0.4/index.php/site/login");
# assert  "百度一下，你就知道" in browser.title;
print(browser.title);
elem = browser.find_element_by_id("LoginForm_username").send_keys("user1");
time.sleep(0.2);
elem = browser.find_element_by_id("LoginForm_password").send_keys("aa123321");
time.sleep(0.2);
# elem.send_keys("seleniumhq" + Keys.RETURN);
browser.find_element_by_id("SubmitLoginBTN").click();
time.sleep(0.2);

browser.find_element_by_id("PostQuery").click();

# browser.find_element_by_xpath("id('create_div')/x:a").click();
# # browser.find_element_by_tag_name("_blank").click();
# browser.find_element_by_id("BugInfoView_title").send_keys("test selenium");
# browser.find_element_by_id("BugInfoView_assign_to_name").send_keys("user1");
# browser.find_element_by_id("BugInfoView_severity").send_keys("2");
# browser.find_element_by_class_name("ke-content").send_keys("test test test 1 2 3");
# browser.find_element_by_name("yt0").click();


# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]");
# except NoSuchElementException:
#     assert 0,"can't find seleniumhq"
browser.close();