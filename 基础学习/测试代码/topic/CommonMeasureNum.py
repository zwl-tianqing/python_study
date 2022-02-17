# 求两个数之间公约数的个数
import math
a = 24
b = 36
min_num = min(a, b)
max_num = max(a, b)
max_common_measure = 0
# 求最大公約数
while True:
    mod = max_num % min_num
    if mod == 0:
        max_common_measure = min_num
        break
    max_num = min_num
    min_num = mod
# 分解最大公约数
count = 0
for i in range(1, max_common_measure + 1):
    if max_common_measure % i == 0:
        count += 1
print(count)
