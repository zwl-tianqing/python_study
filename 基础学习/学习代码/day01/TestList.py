# 二进制数
a = 13
count = 0
while True:
    mod = a % 2
    a = a // 2
    if mod == 1:
        count = count + 1
    if a == 0:
        print(count)
        break
