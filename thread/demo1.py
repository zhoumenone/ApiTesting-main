import threading
import time

exitFlag = 0

class myThead(threading.Thread):
    def __init__(self,threadID,name,delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("开始线程:" + self.name)
        print_time(self.name,self.delay,5)
        print(("退出线程:" + self.name))

def print_time(threadName)