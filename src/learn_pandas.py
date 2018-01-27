import pandas as pd
import pickle as pk


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


f = open("E:/logs/bugfreeebugs/bugdata.pkl", "rb")
data = pk.load(f)

ls_bug_id = []
ls_bug_title = []
ls_bug_status = []
ls_bug_severity = []
ls_bug_priority = []
ls_bug_solution = []
for bug in data:
    ls_bug_id.append(bug.bug_id)
    ls_bug_title.append(bug.title)
    ls_bug_status.append(bug.status)
    ls_bug_severity.append(bug.severity)
    ls_bug_priority.append(bug.priority)
    ls_bug_solution.append(bug.solution)

bug_id_column = pd.Series(ls_bug_id, name='bugid')
bug_title_column = pd.Series(ls_bug_title, name='title')
bug_status_column = pd.Series(ls_bug_status, name='status')
bug_severity_column = pd.Series(ls_bug_severity, name='severity')
bug_priority_column = pd.Series(ls_bug_priority, name='priority')
bug_solution_column = pd.Series(ls_bug_solution, name='solution')
predictions = pd.concat(
    [bug_id_column, bug_title_column, bug_status_column, bug_severity_column, bug_priority_column, bug_solution_column],
    axis=1)
# another way to handle
save = pd.DataFrame({'bugid': ls_bug_id, 'title': ls_bug_title, 'status': ls_bug_status, 'severity': ls_bug_severity,
                     'priority': ls_bug_priority, 'solution': ls_bug_solution})
save.to_csv(r'C:\Users\Administrator\Desktop\b.csv', index=False, encoding="utf-8")
