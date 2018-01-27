import xlwings
import pickle
from grapBugfree import BugFreeBug


def bug_status(bug):
    str_status = ""
    if "Active" == bug.status:
        str_status = "待修复"
    elif "Resolved" == bug.status:
        str_status = "待验证"
    elif "Closed" == bug.status:
        str_status = "已解决"
        if "遗留" == bug.solution:
            str_status = "遗留"
        elif "注销" == bug.solution:
            str_status = "注销"

    return str_status

if __name__ == "__main__":
    f = open("E:/logs/bugfreeebugs/bugdata.pkl", "rb")
    bug_list = pickle.load(f)

    app = xlwings.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    file_path = r"C:/Users/Administrator/Desktop/03-BUG信息表(SSVA).xls"
    wb = app.books.open(file_path)
    sheet = wb.sheets["BUG信息"]

    index_row = 8
    for bug in bug_list:
        str_title = "E%s" % index_row
        str_seriers = "BN%s" % index_row
        str_again = "BU%s" % index_row
        str_statu = "CB%s" % index_row
        str_by_whom = "CI%s" % index_row
        str_by_when = "CQ%s" % index_row
        str_cqid = "CZ%s" % index_row
        str_comments = "DL%s" % index_row
        str_imgs = "DF%s" % index_row
        sheet.range(str_title).value = bug.title
        sheet.range(str_seriers).value = bug.severity
        sheet.range(str_again).value = "稳定必现"
        sheet.range(str_statu).value = bug_status(bug)
        sheet.range(str_by_whom).value = bug.created_by
        sheet.range(str_by_when).value = bug.created_at
        sheet.range(str_cqid).value = bug.bug_id

        cell_comments = sheet.range(str_comments)
        cell_comments.value = "\n".join(bug.list_comments)
        # + "\n".join(bug.list_files)

        if len(bug.list_files) >= 1:
            sht_name = "图%s" % bug.bug_id
            sheet.range(str_imgs).value = sht_name
            # wb.sheets.add(sht_name, after="BUG信息")

        index_row += 1
        if 0 == ((index_row-8) % 20):
            print("已写入%d条" % (index_row-8))

    print("完成：共%d条" % (index_row-8))
    wb.save(r"C:/Users/Administrator/Desktop/03-BUG信息表(SSVA)_导出.xls")
    wb.close()
    app.quit()



    # elif "重新设计" == bug.solution:
    #     str_status = "已解决"
    # elif "重复" == bug.solution:
    #     str_status = "已解决"
    # elif "外部原因" == bug.solution:
    #     str_status = "已解决"
    # elif "修复" == bug.solution:
    #     str_status = "已解决"
    # elif "无法再现" == bug.solution:
    #     str_status = "已解决"
    # elif "遗留" == bug.solution:
    #     str_status = "遗留"
    # elif "注销" == bug.solution:
    #     str_status = "注销"
    # elif "非Bug" == bug.solution:
    #     str_status = "非BUG"

# -------------------------------------------------教程-------------------------------------------------------------
# 打开以保存的Excel文档
# 导入xlwings模块，打开excel程序默认设置：程序不可见，只打开不新建工作薄，屏幕更新关闭
# import xlwings as xw
# app = xw.App(visible=False, add_book=False)
# app.display_alerts = False
# app.screen_updating = False
# # 文件位置：filePath，打开text文档，保存、关闭、结束程序
# filePath = r"C:/Users/Administrator/Desktop/03-BUG信息表(SSVA)2.xls"
# wb = app.books.open(filePath)
# wb.save()
# wb.close()
# app.quit()

# 新建Excel文档，命名为test.xlsx，并保存在D盘
# import xlwings as xw
# app = xw.App(visible=True, add_book=True)
# wb = app.books.add()
# wb.save(r"d:\text.xlsx")
# wb.close()
# app.quit()

# 单元格输入值
# 新建Excel，text.xlsx ，在sheet1的第一个单元格输入“人生”，然后保存关闭，退出excel程序
# import xlwings as xw
#
# app = xw.App(visible=True, add_book=False)
# wb = app.books.add()
# # wb 就是新建的工作簿(workbook),下面则对wb的sheet1的A1单元格赋值
# wb.sheets["sheet1"].range["A1"].value = "人生"
# wb.save(r"d:\text.xlsx")
# wb.close()
# app.quit()

# 打开已保存的text.xlsx，在sheet2的第二个单元格输入“苦短”，然后保存关闭，退出excel程序
# app = xlwings.App(visible=True, add_book=False)
# wb = app.books.open(r"d:\text.xlsx")
# wb.sheets["sheet2"].range["A2"].value = "苦短"
# wb.save()
# wb.close()
# app.quit()

# 引用工作簿、工作表、单元格
# 1、 应用工作簿，注意工作簿应该首先被打开
# wb = xlwings.books['工作簿的名字']

# 2、引用活动工作簿
# wb = xlwings.books.active

# 3、引用工作簿中的sheet
# sht = xlwings.books["工作簿的名字"].sheets["sheet的名字"]
# #或者
# wb = xlwings.books["工作簿的名字"]
# sht = wb.sheets["sheet的名字"]

# 4、引用活动sheet
# sht = xlwings.books["工作簿的名字"].sheets.active
# 5、引用A1单元格
# cell_A1 = sht.range("A1")

# 单元格的完全引用路径是
# cell_A1 = xlwings.apps[0].books[0].sheets[0].range("A1")

# A1单元格的引用
#       xw.Range(1,1)
#       #A1:C3单元格的引用
#       xw.Range((1,1),(3,3))


# 储存数据
# 1、储存单个值
#    # 注意".value“
#    sht.range('A1').value=1
# 1、储存列表
#     # 将列表[1,2,3]储存在A1：C1中
#     sht.range('A1').value=[1,2,3]
#     # 将列表[1,2,3]储存在A1:A3中
#     sht.range('A1').options(transpose=True).value=[1,2,3]
#     # 将2x2表格，即二维数组，储存在A1:B2中，如第一行1，2，第二行3，4
#    sht.range('A1').options(expand='table')=[[1,2],[3,4]]

# 读取数据
# 读取单个值
#  # 将A1的值，读取到a变量中
#  a=sht.range('A1').value
# 将值读取到列表中
#  #将A1到A2的值，读取到a列表中
#  a=sht.range('A1:A2').value
#  # 将第一行和第二行的数据按二维数组的方式读取
#  a=sht.range('A1:B2').value

# wb.activate()激活为当前工作簿
# wb.fullname 返回工作簿的绝对路径
# wb.name 返回工作簿的名称
# wb.save(path=None) 保存工作簿，默认路径为工作簿原路径，若未保存则为脚本所在的路径
# wb. close() 关闭工作簿


# # 激活sheet为活动工作表
# sht.activate()
# # 清除sheet的内容和格式
# sht.clear()
# # 清除sheet的内容
# sht.contents()
# # 获取sheet的名称
# sht.name
# # 删除sheet
# sht.delete

# range常用的api
 # 引用当前活动工作表的单元格
 # rng=xw.Range('A1')
 # # 加入超链接
 # # rng.add_hyperlink(r'www.baidu.com','百度',‘提示：点击即链接到百度')
 # # 取得当前range的地址
 # rng.address
 # rng.get_address()
 # # 清除range的内容
 # rng.clear_contents()
 # # 清除格式和内容
 # rng.clear()
 # # 取得range的背景色,以元组形式返回RGB值
 # rng.color
 # # 设置range的颜色
 # rng.color=(255,255,255)
 # # 清除range的背景色
 # rng.color=None
 # # 获得range的第一列列标
 # rng.column
 # # 返回range中单元格的数据
 # rng.count
 # # 返回current_region
 # rng.current_region
 # # 返回ctrl + 方向
 # rng.end('down')
 # # 获取公式或者输入公式
 # rng.formula='=SUM(B1:B5)'
 # # 数组公式
 # rng.formula_array
 # # 获得单元格的绝对地址
 # rng.get_address(row_absolute=True, column_absolute=True,include_sheetname=False, external=False)
 # # 获得列宽
 # rng.column_width
 # # 返回range的总宽度
 # rng.width
 # # 获得range的超链接
 # rng.hyperlink
 # # 获得range中右下角最后一个单元格
 # rng.last_cell
 # # range平移
 # rng.offset(row_offset=0,column_offset=0)
 # #range进行resize改变range的大小
 # rng.resize(row_size=None,column_size=None)
 # # range的第一行行标
 # rng.row
 # # 行的高度，所有行一样高返回行高，不一样返回None
 # rng.row_height
 # # 返回range的总高度
 # rng.height
 # # 返回range的行数和列数
 # rng.shape
 # # 返回range所在的sheet
 # rng.sheet
 # #返回range的所有行
 # rng.rows
 # # range的第一行
 # rng.rows[0]
 # # range的总行数
 # rng.rows.count
 # # 返回range的所有列
 # rng.columns
 # # 返回range的第一列
 # rng.columns[0]
 # # 返回range的列数
 # rng.columns.count
 # # 所有range的大小自适应
 # rng.autofit()
 # # 所有列宽度自适应
 # rng.columns.autofit()
 # # 所有行宽度自适应
 # rng.rows.autofit()

# books 工作簿集合的api
#  # 新建工作簿
#  xw.books.add()
#  # 引用当前活动工作簿
#  xw.books.active

# sheets 工作表的集合
#  # 新建工作表
#  xw.sheets.add(name=None,before=None,after=None)
#  # 引用当前活动sheet
#  xw.sheets.active