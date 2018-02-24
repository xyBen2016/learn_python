import time

# 函数方法装饰器
# def decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(end_time - start_time)
#
#     return wrapper
#
#
# @decorator
# def func():
#     time.sleep(0.8)
#
#
# func()

# 类函数装饰器
# def decorator(func):
#     def wrapper(sss):
#         start_time = time.time()
#         func(sss)
#         end_time = time.time()
#         print(end_time - start_time)
#
#     return wrapper
#
#
# class Method(object):
#
#     @decorator
#     def func(self):
#         time.sleep(0.5)
#
#
# p1 = Method()
# p1.func()

# 类装饰器
# class decorator(object):
#
#     def __init__(self, f):
#         self.f = f
#
#     def __call__(self):
#         print("decorator start")
#         self.f()
#         print("decorator end")
#
#
# @decorator
# def func():
#     print("func")
#
#
# func()

# 装饰器链
# def first(f):
#     return lambda: "<b>" + f() + "</b>"
#
#
# def second(f):
#     return lambda: "<i>" + f() + "</i>"
#
#
# @first
# @second
# def say():
#     return "hello"
#
#
# print(say())

# 装饰器库functools
from functools import wraps


def decorator(f):
    @wraps(f)
    def inner_func():
        pass

    return inner_func


@decorator
def func():
    pass


print(func.__name__)
