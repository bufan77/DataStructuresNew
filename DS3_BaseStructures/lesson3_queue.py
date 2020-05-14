'''
    队列：是一系列有顺序的元素的集合，新元素加入在队列的一端，这一端叫做“队尾(rear)”
         已有元素的移除发生在队列的另一端，叫做“队首(front)”。当一个元素被加入到队列之后，它就从队尾向队首前进，直到它成为下一个即将被移出队列的二元素
         先进先出(FIFO):最新被加入的元素处于队尾，在队列中停留最长时间的元素处于队首


    ---------------------

    抽象数据类型(ADT):
        Queue()        创建一个空队列队象，无需参数，返回空的队列
        enqueue(item)  将数据项添加到队尾，无返回值
        dequeue()      从队首移出数据项，无需参数，返回值为队首数据项
        isEmpty()      是否队列为空，无需参数，返回值为布尔值
        size()         返回队列中的数据项的个数，无需参数
    
    用python list实现队列
    队尾在列表的0的位置
    enqueue   insert()
    dequeue   pop()
'''

# class Queue():
#     def __init__(self):
#         self.items = []

#     def enqueue(self,item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()

#     def isEmpty(self):
#         return self.items == []

#     def size(self):
#         return len(self.items)

# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(True)
# q.dequeue()

# print(q.size())
# print(q.isEmpty())
# print(q.dequeue())

# -----------------------------------
# rear                         front
# -----------------------------------

'''
    马铃薯游戏(击鼓传花) 选定一个人作为开始的人，数到num个人，将此人淘汰
'''
# from pythonds.basic.queue import Queue

# name_list = ['红','明','强','丽','马','王','赵','三','四','五','啦']
# num = 7
# def send_flower(name_list,num):
#     q = Queue()
#     for name in name_list:
#         q.enqueue(name)
#     while q.size() > 1:
#         for i in range(num):
#             q.enqueue(q.dequeue())
#         n = q.dequeue()
#         print(n)
#     return q.dequeue()

# print(send_flower(name_list,num))

'''
    模拟打印机

    平均每天任意一个小时有大约10个学生在实验室里，在这一小时中通常每人发起2次打印任务，每个打印任务的页数从1到20页不等。实验室中的打印机比较老旧，如果以草稿模式打印，每分钟可以打印10页；打印机可以转换成较高品质的打印模式，但每分钟只能打印5页。较慢的打印速度可能使学生等待太长时间。应该采取哪种打印模式？

    学生       (等待时间 + 打印时间)
    打印任务   (打印任务队列)
    打印机     (状态：打印中，空闲)

    1-20不等，随机数模拟

    总共10*2 = 20次打印任务，平均每3分钟产生一个打印任务
    在三分钟内的任意一秒产生一个打印任务的概率是：task/180，随机数模拟，如果生成的随机数是180，就可以认为生成了一个任务

    过程：
        1.创建一个空打印任务队列，每个任务在生成时被赋予一个“时间戳“
        2.一个小时中的每一秒（currentSecond）都需要判断：
            是否有新的打印任务生成，如果有，把它加入打印队列；
            如果打印机空闲并且队列不为空：
            1.从队列中拿出一个任务交给打印机
            2.从加入打印机时间减去 - 加入队列的时间 = 等待时间
            3.将改任务的等待时间加入到一个列表中，方便后续时候，计算总的学生打印花费的时间
            4.基于打印的页数的随机数，求出需要多长时间打印
        3.打印机工作中，那对于打印机而言，就是工作了一秒：对于打印任务而言，它离打印结束又近了一秒
        4.打印任务完成，剩余时间为0，打印机进入空闲状态
        python实现：
            1.三个对象：打印机（Printer） 打印任务(Task)  打印队列（PrintQueue）
            2.Printer需要实时监测是否正在执行打印任务，判断自己处于空闲还是打印任务中的状态
                设置是打印草稿还是打印高品质的
                如果打印中，需要结合随机的打印的页数，计算打印的时间
                打印结束后，将打印机状态设置为空闲

'''
# import random
# from pythonds.basic.queue import Queue
# class Printer:
#     #打印机初始化
#     def __init__(self,ppm):
#         #设置打印的速率    pagerate为每页打印所需要的时间，设定好后便是恒定的值
#         self.pagerate = ppm
#         #记录当前正在处理的任务
#         self.currentTask = None
#         #打印机当前任务的剩余时间
#         self.timeRemaining = 0

#     #内部任务需要的时间计算函数
#     def tick(self):
#         if self.currentTask != None: #有任务需要处理
#             self.timeRemaining = self.timeRemaining - 1  # 打印，也就是将剩余打印时间减1
#             if self.timeRemaining <= 0:   # 当前任务打印结束
#                 self.currentTask = None

#     #切换打印机状态
#     def busy(self):
#         if self.currentTask != None:
#             if self.currentTask != None:
#                 return True
#             else:
#                 return False
    
#     def startNew(self,newTask):
#         # newtask 为新的任务
#         self.currentTask = newTask
#         self.timeRemaining = newTask.getPages()*60/self.pagerate  #计算新的剩余打印时间


# class Task:
#     #任务初始化
#     def __init__(self,time):
#          # time 为传入的任务创建时间，也就是入队时间
#         self.timestamp = time
#         self.pages = random.randrange(1,21)  # 随机生成1到20页之间的页数

#     def getStamp(self):
#         return self.timestamp

#     def getPages(self):
#         return self.pages
    
#     def waitTime(self,currenttime):
#         # out_time为当前时间戳
#         return currenttime - self.timestamp

# def main(numSeconds,pagesPerMinute):
#     #numSeconds为总的实验时间，pagesPerMinute为每页打印所需要的时间
#     labPrinter = Printer(pagesPerMinute)   #初始化打印机
#     printQueue = Queue()  #初始化任务等待队列
#     watingtimes = []  #记录每个任务的等待时间

#     for currentSeconds in range(numSeconds):
#         if newPrintTask():
#             task = Task(currentSecond)
#             printQueue.enqueue(task)

#         if(not labPrinter.is_busy()) and (not printQueue.isEmpty()):  #打印机空闲并且有任务在等待
#             nexttask = printQueue.dequeue()  # 弹出下一个任务
#             watingtimes.append(nexttask.waitTime(currentSeconds))  # 计算并记录等待时间
#             labPrinter.startNew(nexttask)  #载入新的任务
#         labPrinter.tick()   #打印
#         averageWaite = sum(watingtimes) / len(watingtimes)
#         print("平均等待%6.2f秒  还剩%3d任务"%(averageWaite,printQueue.size()))

# def newPrintTask():
#     num = random.randrange(1,180)
#     if num == 180:
#         return True
#     else:
#         return False

# if __name__ == '__main__':
#     for i in range(10):
#         simulation(3600,10)




'''
    1.学生数变为20
    2.不局限在一个小时之内的话，这些学生
'''

import random
from pythonds.basic.queue import Queue

class Printer:
    def __init__(self,ppm):
        # 设置打印的速率
        self.pagerate = ppm
        self.currentTask = None
        # 打印机当前任务的剩余时间
        self.timeRemaining = 0

    # 内部任务需要的时间计算函数
    def tick(self):
        if self.currentTask != None: 
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    # 切换打印机状态
    def is_busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNew(self,newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages()*60/self.pagerate


class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currenttime):
        return currenttime - self.timestamp



def simulation(numSeconds,pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    watingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if(not labPrinter.is_busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            watingtimes.append(nexttask.waitTime(currentSecond))
            labPrinter.startNew(nexttask)

        labPrinter.tick()
    averageWait=sum(watingtimes)/len(watingtimes)
    print("平均等待时间 %6.2f secs 剩下%3d任务"%(averageWait,printQueue.size()))
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,10)


'''
    1. 学生数变为20
    2. 不局限在一个小时之内的话，这些学生都打印完需要多长时间
'''
#一小时等于60分钟   一小时内有20次打印任务
# import random
# used = 10*60  #600
# new = 5*60   #300
# # page = random.randint(1, 20)
# for page in range(1,21):
#     print_page = 20*page
#     if print_page > new:
#         print(print_page)
#         print('使用草稿模式打印')
#     else:
#         print(print_page)
#         print('使用较高品质的打印模式')
        
