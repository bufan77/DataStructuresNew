#注册牛客网，LeetCode()
#若果a+b+c = 1000， 并且a^2 + b^2 = c^2,求出a,b,c可能的组合
#解决同一个问题，时间短的算法更好
#第一种算法
# import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()
# print('运行时间为：%f'%(end_time - start_time))

#为了让执行时间更短，提出第二种算法，双重循环
import time  
start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 -a -b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d,%d,%d"%(a,b,c))

end_time = time.time()
print('运行时间为：%f'%(end_time - start_time))