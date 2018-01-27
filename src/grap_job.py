from selenium import webdriver
from bs4 import BeautifulSoup
import time

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
    list_div = html.find_all("div", {"class": "jobs-list"})  # jobsList pull-left
    if len(list_div) <= 0:
        return

    div = list_div[0]
    list_dd = div.find_all("dd")

    list_job = []
    count = 0
    for dd in list_dd:
        p1 = dd.find_all("p", {"class": "job-name"})[0]  # work
        str_job_name = p1.find_all("a")[0].get_text()
        str_job_salary = p1.find_all("span")[0].get_text().strip()  # i
        str_job_release_time = p1.find_all("span")[0].get_text()
        p2 = dd.find_all("p", {"class": "corp-name"})[0]  # corp
        str_job_company = p2.find_all("a", {"class": "corpName"})[0].get_text()
        str_job_type = dd.find_all("p", {"class": "type-info"})[0].get_text()  # info
        str_job_desc = dd.find_all("p", {"class": "describe"})[0].get_text()  # jobInfo
        count += 1
        job = Job(str(count), str_job_name, str_job_salary, str_job_company, str_job_release_time, str_job_type,
                  str_job_desc)
        list_job.append(job)
        
    print(count)

    for job in list_job:
        job.show_info()

    print("共找到%s个合适岗位" % len(list_job))


if __name__ == "__main__":
    driver = webdriver.PhantomJS()
    driver.get("http://www.vvjob.com/gl/")
    driver.find_element_by_id("search_jobs").send_keys("测试")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[4]/div[1]/form/input[2]").click()

    get_data(driver)
    print("over")
#     driver.find_element_by_class_name("next").click()
#     time.sleep(3)
#     print(driver.page_source)
