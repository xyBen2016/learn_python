from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


class Job:
    job_id = ""
    job_name = ""
    job_salary = ""
    job_company = ""
    job_release_time = ""
    job_type = ""
    job_desc = ""

    def __init__(self, job_id, job_name, job_salary, job_company, job_release_time, job_type, job_desc):
        self.job_id = job_id
        self.job_name = job_name
        self.job_salary = job_salary
        self.job_company = job_company
        self.job_release_time = job_release_time
        self.job_type = job_type
        self.job_desc = job_desc

    def show_info(self):
        print("job_id:%s" % self.job_id)
        print("job_name:%s" % self.job_name)
        print("job_salary:%s" % self.job_salary)
        print("job_company:%s" % self.job_company)
        print("job_release_time:%s" % self.job_release_time)
        print("job_type:%s" % self.job_type)
        print("job_desc:%s" % self.job_desc)
        print("----------------------------------------------")


def get_data(my_driver):
    html = BeautifulSoup(my_driver.page_source, "html.parser")
    # print(html)
    list_div = html.find_all(
        "div", {"class": "jobs-list"})  # jobsList pull-left
    if len(list_div) <= 0:
        return

    div = list_div[0]
    list_dd = div.find_all("dd")

    global list_job
    global count
    for dd in list_dd:
        p1 = dd.find_all("p", {"class": "job-name"})[0]  # work
        str_job_name = p1.find_all("a")[0].get_text()
        str_job_salary = p1.find_all("span")[0].get_text().strip()  # i
#         str_job_release_time = p1.find_all("span")[0].get_text()
        p_time = dd.find_all("p", {"class": "time-btn"})[0]
        str_job_release_time = p_time.find_all("span")[0].get_text()
        p2 = dd.find_all("p", {"class": "corp-name"})[0]  # corp
        str_job_company = p2.find_all("a", {"class": "corpName"})[0].get_text()
        str_job_type = dd.find_all(
            "p", {"class": "type-info"})[0].get_text()  # info
        str_job_desc = dd.find_all("p", {"class": "describe"})[
            0].get_text()  # jobInfo
        count += 1
        job = Job(str(count), str_job_name, str_job_salary, str_job_company, str_job_release_time, str_job_type,
                  str_job_desc)
        list_job.append(job)


def show_jobs():
    global list_job
    global count

    print("共找到" + str(count) + "个适合您的岗位:")

    for job in list_job:
        job.show_info()

    print("共找到%s个合适岗位" % len(list_job))


def writeToTxt():
    global count
    f_txt = open(
        r"E:/xy/test/eclipse_python/cx/workspace/learnpython/src/jobs.txt", "a", encoding='utf-8')
    f_txt.write("共找到" + str(count) + "个适合您的岗位:")
    f_txt.write("\n")

    for job in list_job:
        f_txt.write(
            "*******************************************************************************************************")
        f_txt.write("\n")
        f_txt.write("岗位id：" + job.job_id)
        f_txt.write("\n")
        f_txt.write("岗位名称：" + job.job_name)
        f_txt.write("\n")
        f_txt.write("岗位薪资：" + job.job_salary)
        f_txt.write("\n")
        f_txt.write("公司名称：" + job.job_company)
        f_txt.write("\n")
        f_txt.write("发布时间：" + job.job_release_time)
        f_txt.write("\n")
        f_txt.write("职位类型：" + job.job_type)
        f_txt.write("\n")
        f_txt.write("职责描述：" + job.job_desc)
        f_txt.write("\n")
        f_txt.write(
            "*******************************************************************************************************")

    f_txt.close()


list_job = []
count = 0

if __name__ == "__main__":
    driver = webdriver.PhantomJS()
#     driver = webdriver.Chrome(
# executable_path="C:/Program Files
# (x86)/Google/Chrome/Application/chromedriver")

    driver.get("http://www.vvjob.com/gl/")
    driver.find_element_by_id("search_jobs").send_keys("软件测试")
    driver.find_element_by_xpath(
        '//*[@id="search"]/div[4]/div[1]/form/input[3]').click()

    while True:
        try:
            get_data(driver)
            li_next = driver.find_element_by_class_name("next")
#             li_next.click()
            a_next = li_next.find_element_by_tag_name("a")
            a_next.click()
        except NoSuchElementException:
            #             print("已是最后一页")
            break

#     show_jobs()
#     print("over")
    driver.quit()

    writeToTxt()
