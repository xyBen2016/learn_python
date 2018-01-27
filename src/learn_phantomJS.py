from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get("http://www.qiushibaike.com/")
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.prettify())
print("pyinstaller hello world")
