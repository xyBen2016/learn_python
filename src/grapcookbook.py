from selenium import webdriver
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
import pickle
import requests
import os
import re
import time

list_caipu = []


def save_obj(obj_custom):
    """存储对象"""
    print("已将pickle文件保存在:E:\logs\caipu\caipu.pkl")
    f = open("E:\logs\caipu\caipu.pkl", "wb")
    pickle.dump(obj_custom, f)
    f.close()


def load_obj():
    """读取、返回对象"""
    print("正在读取pickle文件:E:\logs\caipu\caipu.pkl")
    f = open("E:\logs\caipu\caipu.pkl", "rb")
    obj_custom = pickle.load(f)
    return obj_custom


class step_cp:
    """步骤"""
    step_desc = ""
    step_pic = ""

    def __init__(self, step_desc, step_pic):
        self.step_desc = step_desc
        self.step_pic = step_pic


class cookbook:
    """菜谱"""
    cp_id = ""
    cp_name = ""
    cp_pic = ""
    cp_seasoning = ""
    cp_list_step = []

    def __init__(self, cp_id, cp_name, cp_pic, cp_seasoning, cp_list_step):
        self.cp_id = cp_id
        self.cp_name = cp_name
        self.cp_pic = cp_pic
        self.cp_seasoning = cp_seasoning
        self.cp_list_step = cp_list_step

    def show_info(self):
        print("cp_id:%s" % self.cp_id)
        print("cp_name:%s" % self.cp_name)
        print("cp_pic:%s" % self.cp_pic)
        print("cp_seasoning:%s" % self.cp_seasoning)
        for step_bean in self.cp_list_step:
            print("step_desc:%s" % step_bean.step_desc)
            print("step_pic:%s" % step_bean.step_pic)


def get_data(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    html = BeautifulSoup(driver.page_source, "html.parser")
    list_div_container = html.find_all("div", {"id": "container"})
    list_div_cp_box = list_div_container[0].find_all(
        "div", {"class": "cp_box"})

    for div_cp_box in list_div_cp_box:
        a_href = div_cp_box.find_all("a", {"class": "cp_pic"})[0]['href']
        driver.get(a_href)
        content = BeautifulSoup(driver.page_source, "html.parser")
        div_pic = content.find_all("div", {"class": "bmayi mbm"})[0]
        href_pic = div_pic.find_all("img")[0]['src']  # 图片链接
        h1_name = content.find_all("h1", {"id": "page_cm_id"})[
            0].get_text()  # 菜名
        table_seasoning = content.find_all("table", {"class": "retamr"})[0]
        list_tr = table_seasoning.find_all("tr", {"class": ""})
        list_seasoning = []
        for tr in list_tr:
            td_s_left = tr.find_all("td", {"class": "lirre"})
            td_s_right = tr.find_all("td", {"class": ""})
            if len(td_s_left) > 0:
                list_seasoning.append(td_s_left[0].get_text().strip())  # 左食材
            if len(td_s_right) > 0:
                list_seasoning.append(td_s_right[0].get_text().strip())  # 右食材

        div_step = content.find_all("div", {"class": "step clearfix"})[0]
        list_div_step = div_step.find_all(
            "div", {"class": "stepcont mll libdm pvl clearfix"})
        list_step = []
        for step in list_div_step:
            ls_div = step.find_all("div", {"class": "pldc"})
            if len(ls_div) > 0:
                step_pic = step.find_all("div", {"class": "pldc"})[0]
                step_src_pic = step_pic.find_all(
                    "img")[0]['original']  # 步骤图片链接

            step_desc = step.find_all("p")[0].get_text().strip()  # 步骤说明
            step_bean = step_cp(step_desc, step_src_pic)
            list_step.append(step_bean)

        cb = cookbook(len(list_caipu), h1_name.strip(), href_pic,
                      "、".join(list_seasoning), list_step)
        # cb.show_info()
        list_caipu.append(cb)
        print("已获取【%s】菜谱数据" % cb.cp_name)

    driver.quit()


def download_pic(url_pic, file_name):
    try:
        pic = requests.get(url_pic, timeout=10)
    except requests.exceptions.ConnectionError:
        print("【错误】当前图片无法下载:%s" % url_pic)
    file = open(file_name, "wb")
    file.write(pic.content)
    file.close()


# 去除标题中的非法字符 (Windows)
def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
    new_title = re.sub(rstr, "", title)
    return new_title


def grap_data():
    for i in range(0, 61, 30):  # 3990+1
        # "http://www.douguo.com/caipu/%E5%B7%9D%E8%8F%9C/"川菜地址
        # "http://www.douguo.com/caipu/%E6%B9%98%E8%8F%9C/"湘菜地址
        # "http://www.douguo.com/caipu/%E9%B2%81%E8%8F%9C/"鲁菜地址
        # "http://www.douguo.com/caipu/%E7%B2%A4%E8%8F%9C/"粤菜地址
        # "http://www.douguo.com/caipu/%E8%8B%8F%E8%8F%9C/"苏菜地址
        # "http://www.douguo.com/caipu/%E9%97%BD%E8%8F%9C/"闽菜地址
        # "http://www.douguo.com/caipu/%E5%BE%BD%E8%8F%9C/"徽菜地址
        # "http://www.douguo.com/caipu/%E6%B5%99%E8%8F%9C/"浙菜地址
        url_dest = "http://www.douguo.com/caipu/%E6%B5%99%E8%8F%9C/" + str(i)
        get_data(url_dest)

    save_obj(list_caipu)


def grap_pic():
    ls_cp = load_obj()
    for cp in ls_cp:
        print("保存菜谱:【%s】" % cp.cp_name)
        dir_path = r"E:\logs\caipu\%s_%s" % (
            cp.cp_id, validate_title(cp.cp_name))
        os.makedirs(dir_path)
        pic_name = r"%s\0.jpg" % dir_path
        # print("正在下载图片:%s" % cp.cp_pic)
        download_pic(cp.cp_pic, pic_name)
        f_seasoning = open(r"%s\seasoning.txt" %
                           dir_path, "w", encoding='utf-8')
        f_seasoning.write(cp.cp_seasoning)
        f_seasoning.close()

        f_step = open(r"%s\step.txt" % dir_path, "a", encoding='utf-8')
        index = 1
        for step_cp in cp.cp_list_step:
            step_pic_name = r"%s\%d.jpg" % (dir_path, index)
            # print("正在下载图片:%s" % step_cp.step_pic)
            f_step.write(step_cp.step_desc)
            f_step.write("\n")
            download_pic(step_cp.step_pic, step_pic_name)
            index += 1

        f_step.close()


if __name__ == "__main__":
    grap_data()
    grap_pic()
    # insert_data()


# def insert_data():
#     driver = webdriver.PhantomJS()
#     login(driver)
#     driver.get("http://www.secomid.net/dynamicManage/seDynamicList/doInput.do?pid=1")
#     # "http://www.secomid.net/dynamicManage/seDynamicList/doInput.do?pid=1"
#     time.sleep(1)
#     # print(driver.page_source)
#     # return
#
#     wait = ui.WebDriverWait(driver, 10)
#     wait.until(lambda dr: driver.find_element_by_id("pageTitle").is_displayed())
#
#     driver.find_element_by_id("pageTitle").send_keys("孜然土豆")
#     time.sleep(1)
#     driver.find_element_by_id("content").send_keys("孜然土豆")
#     time.sleep(1)
#     driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[1]/li").click()
#     time.sleep(1)
#     driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/span[2]/input").click()
#     time.sleep(1)
#     driver.find_element_by_xpath("/html/body/div[2]/div[3]/span[6]/input[2]").click()
#     time.sleep(1)
#
#     iframe_0 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/iframe")
#     driver.switch_to.frame(iframe_0)
#     time.sleep(1)
#     driver.find_element_by_id("SWFUpload_0").send_keys(r"E:\logs\caipu\6_孜然土豆\0.jpg")
#     time.sleep(3)
#     driver.switch_to.default_content()
#     time.sleep(1)
#
#     driver.find_element_by_class_name("close_img").click()
#     time.sleep(1)
#     add_btn = driver.find_element_by_xpath("/html/body/div[2]/div[3]/button[1]")
#     for i in range(1, 3):
#         add_btn.click()
#         time.sleep(1)
#
#     div_add = driver.find_element_by_class_name("addStepListdiv")
#     ls_iframe_1 = div_add.find_elements_by_class_name("uploadframe")
#     ls_iframe_1.pop(0)
#
#     for iframe_1 in ls_iframe_1:
#         driver.switch_to.frame(iframe_1)
#         time.sleep(1)
#         driver.find_element_by_class_name("uploadImg").send_keys(r"E:\logs\caipu\6_孜然土豆\0.jpg")
#         time.sleep(3)
#         driver.switch_to.default_content()
#         time.sleep(1)
#
#     ls_step_titile = div_add.find_elements_by_css_selector(".h4.stepTitle")
#     ls_step_cont = div_add.find_elements_by_css_selector(".h4.stepCont")
#     ls_step_state = div_add.find_elements_by_css_selector(".stepState.h4")
#     for i in range(0, len(ls_step_titile)):
#         ls_step_titile[i].send_keys("标题 %d" % i)
#         time.sleep(1)
#         ls_step_cont[i].send_keys("内容 %d" % i)
#         time.sleep(1)
#         ls_step_state[i].send_keys("说明 %d" % i)
#         time.sleep(1)
#
#     driver.find_element_by_css_selector(".h3.commit").click()
#
#     time.sleep(0.5)
#     warn_box = driver.find_element_by_css_selector(".warnbox.box")
#     print(warn_box.is_displayed())
#     print(warn_box.text)
#     time.sleep(3)
#     print(warn_box.is_displayed())
#
#     # 主要问题，插入图片出错，使用的不是input，无法利用sendKeys方法添加图片文件,智能用autoit之类的工具
#     # 通过python调用生成的exe世上无难事，只要肯放弃
#     # driver.get("http://www.secomid.net/dynamicManage/seDynamicList/index.do")
#     # time.sleep(1)
#     # print(driver.page_source)


# def login(driver):
#     driver.get("http://www.secomid.net/admin/login/login.do")
#     wait = ui.WebDriverWait(driver, 10)
#     wait.until(lambda dr: driver.find_element_by_css_selector(".login.h3").is_displayed())
#     driver.find_element_by_css_selector(".login.h3").click()
#     # driver.find_element_by_class_name("userdiv").click()
#     time.sleep(2)
#     wait.until(lambda dr: driver.find_element_by_id("username").is_displayed())
#     driver.find_element_by_id("username").send_keys("xy001")
#     driver.find_element_by_id("password").send_keys("888888")
#     driver.find_element_by_name("myCheckbox").click()
#     driver.find_element_by_css_selector(".login.h2").click()
#     time.sleep(2)
