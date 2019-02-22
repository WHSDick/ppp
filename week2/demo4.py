# 生成随机数1000个字母
import random
str1 = "qwertyuiopasdfghjklzxcvbnm"
str2 = ""
# 随机生成一个包含1000个字母的字符串
for i in range(1000):
    str2 += random.choice(str1)
print("字符串长度: ", len(str2))

dict1 = {}
for i in str2:
    key1 = dict1.get(i)
    # 每个字母的数量:
    if key1 == None:
        dict1[i] = 1
    else:
        dict1[i] += 1
# 输出结果
print(dict1)
