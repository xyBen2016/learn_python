import xlrd
import xlwt
from xlutils.copy import copy
import pickle
from grapBugfree import BugFreeBug
import xlwings as xw


f = open("E:/logs/bugfreeebugs/bugdata.pkl", "rb")
bug_list = pickle.load(f)
# for bug in bug_list:
#     bug.bug_info()

# 写excel
# 创建一个workbook
work_book = xlwt.Workbook(encoding="utf-8")
# 创建表
sheet = work_book.add_sheet("MyWorkSheet")
# 写表头
list_topic = ["id", "名称", "状态", "严重程度", "优先级", "创建者", "创建时间", "解决方案", "注释", "附件"]
index_topic = 0
for topic in list_topic:
    sheet.write(0, index_topic, label=topic)
    index_topic += 1

for row in range(1, len(bug_list)):
    bug = bug_list[row]
    # 向单元格中写入内容
    sheet.write(row, 0, label=bug.bug_id)
    sheet.write(row, 1, label=bug.title)
    sheet.write(row, 2, label=bug.status)
    sheet.write(row, 3, label=bug.severity)
    sheet.write(row, 4, label=bug.priority)
    sheet.write(row, 5, label=bug.created_by)
    sheet.write(row, 6, label=bug.created_at)
    sheet.write(row, 7, label=bug.solution)
    sheet.write(row, 8, label="\n".join(bug.list_comments))
    sheet.write(row, 9, label="\n".join(bug.list_files))
# 保存
work_book.save("C:/Users/Administrator/Desktop/test.xls")




# 读excel
# 打开文件
# work_book = xlrd.open_workbook("C:/Users/Administrator/Desktop/03-BUG信息表(SSVA).xls")
# # 获取一个工作表
# # 通过索引获取第一个sheet
# sheet0 = work_book.sheets()[0]
# # 通过索引顺序获取
# sheet1 = work_book.sheet_by_index(0)
# # 通过名称获取
# sheet2 = work_book.sheet_by_name("BUG信息")
# # 获取整行整列的值
# row_value = sheet1.row_values(0)
# col_value = sheet1.col_values(1)
# # 获取行数和列数
# nrows = sheet1.nrows
# ncols = sheet2.ncols
# # 获取单元格
# cell00 = sheet1.cell(0, 0).value
# cell23 = sheet1.cell(2, 3).value
#
# for i in range(9, 10):
#     rowva = sheet2.row_values(i)
#     for cell in rowva:
#         print(cell)


# 写excel
# 创建一个workbook
# work_book2 = xlwt.Workbook(encoding="utf-8")
# # 创建表
# sheet3 = work_book2.add_sheet("MyWorkSheet")
# # 向单元格中写入内容
# sheet3.write(0, 0, label = 'Row 0, Column 0 Value')
# sheet3.write(0, 1, label = 'Row 0, Column 1 Value')
# sheet3.write(2, 0, label = 'Row 2, Column 0 Value')
# sheet3.write(2, 1, label = 'Row 2, Column 1 Value')
# # 保存
# work_book2.save("C:/Users/Administrator/Desktop/test.xls")

# work_book3 = xlrd.open_workbook("C:/Users/Administrator/Desktop/test2.xls", formatting_info=True)
# sheet = work_book3.sheet_by_index(0)
# wb_temp = copy(work_book3)
# st_MyWorkSheet = wb_temp.get_sheet(0)
# cell = sheet.cell(0, 0)
# print("cell.xf_index is ", cell.xf_index)
# fmt = work_book3.xf_list[cell.xf_index]
# print("type(fmt) is", type(fmt))
# print("fmt.dump():", fmt.dump())

# st_MyWorkSheet.write(0, 0, "00xfxvalue", style=fmt)
# st_MyWorkSheet.write(0, 1, "01xfxvalue")
# st_MyWorkSheet.write(2, 0, "20xfxvalue")
# st_MyWorkSheet.write(2, 1, "21xfxvalue")
# wb_temp.save("C:/Users/Administrator/Desktop/test.xls")
