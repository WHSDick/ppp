# 编写写程序,生成一个包含20个随机整数的列表

import random
list1 = [] # 定义列表
for i in range(20):
    list1.append(random.randint(0, 20)) # 存放随机整数
# 使用切片对偶数下标降序排序
str1 = list1[0:20:2]
str1.sort()
str1.reversed()

# 打印
print(str)
