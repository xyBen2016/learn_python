import _thread
import time
import threading


# thread
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time("Thread-1", 2))
    _thread.start_new_thread(print_time("Thread-2", 4))
except:
    print("error:无法启动线程")

while 1:
    pass

# threading
exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread" + self.name)
        print_time2(self.name, 5, self.counter)
        print("end thread " + self.name)


def print_time2(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出线程")
