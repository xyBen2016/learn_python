from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.baidu.com")
print(driver.page_source)
time.sleep(3)
driver.quit()

# import random
#
#
# ls_room = [[], [], []]
# ls_person = ["a", "b", "c", "d", "e", "f", "g", "h"]
#
# for index in range(0, 3):
#     person = ls_person[random.randint(0, (len(ls_person) - 1))]
#     ls_room[index].append(person)
#     ls_person.remove(person)
#
# for index in range(0, 5):
#     person = ls_person[index]
#     r = random.randint(0, 2)
#     ls_room[r].append(person)
#
# print(ls_room)


# for j in range(1, 3):
#     for i in range(1, 10):
#         if i == 5:
#             break
#         else:
#             print(i)


# for i in range(1, 6, 2):
#     print(i)

# print({"a": 0, "b": 1}["b"])


# for i in range(1, 10):
#     print("*", end="")
# # 定义一个list用于存放结果
# ls_result = []
#
# # 百位
# for i in range(1, 5):
#     # 十位
#     for j in range(1, 5):
#         # 个位
#         for k in range(1, 5):
#             # 计算这三个数组成的数值
#             num = i * 100 + j * 10 + k
#             # 初始化标志位
#             flag = True
#             # 如果本次循环得到的数字的数值重复，将标志位置为false
#             for n in ls_result:
#                 if num == n:
#                     flag = False
#                     break
#                 # 如果百位、十位、个位有重复的数字，将标志位置为false
#             if i == j or j == k or k == i:
#                 flag = False
#
#             # 如果标志位为true，说明该数字符合条件，将该数字添加到结果集
#             if flag:
#                 ls_result.append(num)
#
# # 打印所有结果
# print(ls_result)
# # 打印结果集长度
# print(len(ls_result))
