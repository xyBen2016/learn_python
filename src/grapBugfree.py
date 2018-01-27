from selenium import webdriver
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui
import pickle

url_root = "http://192.168.1.2:8081"  # 定义根地址目录
url_project = url_root + "/bugfree/index.php/bug/list/8?productmodule_id=4&page=%s"  # 定义项目路径
list_bugs = []  # 创建一个临时列表用于存放bug信息
page_start = 1  # 开始页数
page_end = 19  # 结束页数


class BugFreeBug:
    # 定义一个bug信息类
    # bug id
    bug_id = ""
    # bug名称
    title = ""
    # bug链接
    href = ""
    # bug状态
    BugInfoView_bug_status = ""
    # bug严重程度
    BugInfoView_severity = ""
    # bug优先级
    BugInfoView_priority = ""
    # bug创建者
    BugInfoView_created_by = ""
    # bug创建时间
    BugInfoView_created_at = ""
    # bug解决方案
    BugInfoView_solution = ""
    # bug注释
    list_comments = []
    # bug附件
    list_files = []

    def __init__(self, bug_id, title, href, status, severity, priority, created_by,
                 created_at, solution, comments, list_files):
        # 初始化
        self.bug_id = bug_id
        self.title = title
        self.href = href
        self.status = status
        self.severity = severity
        self.priority = priority
        self.created_by = created_by
        self.created_at = created_at
        self.solution = solution
        self.list_comments = comments
        self.list_files = list_files

    def bug_info(self):
        # 打印bug信息
        print("-----------------------------------------")
        print("bug_id:" + self.bug_id)
        print("title:" + self.title)
        print("href:" + self.href)
        print("status:" + self.status)
        print("severity:" + self.severity)
        print("priority:" + self.priority)
        print("created_by:" + self.created_by)
        print("created_at:" + self.created_at)
        print("solution:" + self.solution)
        print("list_comments:" + "[" + ",".join(self.list_comments) + "]")
        print("list_files:" + "[" + ",".join(self.list_files) + "]")
        print("-----------------------------------------")


def value_routine(att_value, html_detail):
    # 得到某一个bug的常规值
    det_value = html_detail.findAll("label", {"for": att_value})[0].find_parent().contents[2].string
    det_value = det_value.strip()
    return det_value


def login_bugfree():
    # 登录bugfree
    # 使用PhantomJS创建一个浏览器驱动

    driver = webdriver.PhantomJS()
    # 得到登录页面信息
    driver.get("http://192.168.1.2:8081/bugfree/index.php/site/login")
    # 最多等待10秒
    wait = ui.WebDriverWait(driver, 10)
    # 等待，直至页面显示用户名输入框
    wait.until(lambda dr: driver.find_element_by_id("LoginForm_username").is_displayed())
    # 得到用户名输入框，输入用户名
    driver.find_element_by_id("LoginForm_username").send_keys(u"xingyi")
    # 得到密码输入框，输入密码
    driver.find_element_by_id("LoginForm_password").send_keys(u"aa123321")
    # 得到登录按钮，触发点击事件
    driver.find_element_by_id("SubmitLoginBTN").click()
    # 等待，直至页面显示登录成功用户信息
    wait.until(lambda dr: driver.find_element_by_class_name("user-info").is_displayed())
    return driver


def get_buglist(driver):
    # 获取整个列表页面的bug信息
    # 使用bs4解析页面html
    html = BeautifulSoup(driver.page_source, "html.parser")
    # 得到所有的table元素
    bugTable = html.findAll("table", {"class": "items"})
    # 得到第一个table元素，并获取其下的所有tr元素
    ls_tr = bugTable[0].findAll("tr")

    # 循环便利所有tr元素
    for tr in ls_tr:
        # 得到tr元素下所有span
        span = tr.findAll("span", {"class": "title"})

        if len(span) != 0:
            # 得到span下所有a标签
            a = span[0].findAll("a")
            # 得到a标签下href的属性值，即bug地址。href:/bugfree/index.php/bug/613
            str_href = a[0]['href']
            # 获取bug详细信息
            driver.get(url_root + str_href)
            # 解析bug详细信息页面html
            html_detail = BeautifulSoup(driver.page_source, "html.parser")
            # 得到bug标题input元素
            bug_input = html_detail.findAll("input", {"id": "BugInfoView_title"})[0]
            # 得到bug标题title
            bug_info = bug_input['title']
            # 得到所有常规信息span元素
            bug_id = html_detail.findAll("span", {"id": "span_info_id"})[0].get_text()
            # 得到状态
            bug_status = value_routine("BugInfoView_bug_status", html_detail)
            # 得到严重程度
            bug_severity = value_routine("BugInfoView_severity", html_detail)
            # 得到优先级
            bug_priority = value_routine("BugInfoView_priority", html_detail)
            # 得到创建人
            bug_created_by = value_routine("BugInfoView_created_by", html_detail)
            # 得到创建时间
            bug_created_at = value_routine("BugInfoView_created_at", html_detail)
            # 得到修复方案
            bug_solution = value_routine("BugInfoView_solution", html_detail)
            # 得到所有注释元素fieldset
            tag_fieldset = html_detail.findAll("fieldset", {"id": "fieldset_comment"})[0]
            # 得到注释存放元素blockquote列表
            tag_comments = tag_fieldset.findAll("blockquote")
            # 定义一个临时列表
            list_temp = []
            # 遍历注释tag列表
            for comment in tag_comments:
                # 得到某一条注释的字符串
                str_com = comment.get_text()
                # 将字符串存入临时列表
                list_temp.append(str_com)

            # 附件
            list_href_file = []
            div_files_upload = html_detail.findAll("div", {"id": "uploaded_file"})[0]
            span_files_upload = div_files_upload.findAll("span")
            # print("len(list_files_upload) = %d" % len(span_files_upload))
            for span in span_files_upload:
                href_img = url_root + span.findAll("a")[0]['href']
                list_href_file.append(href_img)

            # 筛选条件
            if "曾梦瑶" != bug_created_by:
                continue

            # 创建一个BugFreeBug对象，设置对象初始值
            bug = BugFreeBug(bug_id, bug_info, str_href, bug_status, bug_severity, bug_priority, bug_created_by,
                             bug_created_at, bug_solution, list_temp, list_href_file)
            # 打印BugFreeBug对象的基本信息
            # bug.bug_info()
            # 存入临时数组
            list_bugs.append(bug)

    return list_bugs


def save_bug(bug_list):
    print("已将pickle文件保存在 E:/logs/bugfreeebugs/bugdata.pkl")
    # 存储bug列表
    f = open("E:/logs/bugfreeebugs/bugdata.pkl", "wb")
    pickle.dump(bug_list, f)
    f.close()


def load_bug():
    # 读取bug列表
    f = open("E:/logs/bugfreeebugs/bugdata.pkl", "rb")
    bug_list = pickle.load(f)
    return bug_list
    # print(bug_list)
    # print(type(bug_list))
    # for bug in bug_list:
    #     bug.bug_info()


if __name__ == "__main__":
    # 主方法
    # 登录bugfree
    driver = login_bugfree()
    # 进入某个项目路径
    for page_num in range(page_start, page_end):
        # 翻页
        # driver.get("http://192.168.1.2:8081/bugfree/index.php/bug/list/8?page=%s" % page_num)
        # print(url_project % page_num)
        driver.get(url_project % page_num)
        # driver.get("http://192.168.1.2:8081/bugfree/index.php/bug/list/8?productmodule_id=4&page=%s" % page_num)
        # 获取整个列表页面的bug信息
        get_buglist(driver)
        print("已处理%d条数据" % len(list_bugs))


    print("共%d条数据" % len(list_bugs))
    # 退出浏览器驱动
    driver.quit()
    # 保存数据
    save_bug(list_bugs)
    # 读取数据
    # bug_list = load_bug()
    # # 打印bug列表
    # print(bug_list)
    # for bug in bug_list:
    #     bug.bug_info()
