"""
    格式化输出数据
"""
# 年龄 10
age = 10
# 姓名
name = '张三'
# 体重
weight = 75.5
# 学生 ID
stu_id = 1

# 1. 我今年多少岁 --整型 %d
print("我今年%d岁"% age)

# 2. 我的名字是 --字符串 %s
print('我的名字是%s'% name)

# 3 我的体重是 --浮点型 %f
print('我的体重是%.2f' % weight)

"""
 4 输出学号 如何将数据格式化输出
    将 学号 1, 使用 格式 001 
    输出三位格式，不足的按 0 补全
    在 %d 之间加上  %0xd 就表示数据按 
    x 位输出，不足的按 0 补齐，超出的数位 按原样输出
"""
print('我的学号是%03d' % stu_id)

stu_id2 = 234542
print('我的学号是%03d' % stu_id2)


# 5 输出多个字符
print('我的学号是%03d,我的年龄是%d,我的体重是%.2f' %(stu_id, age, weight))

# 6 f'{}' f 表达式 的使用
print(f'我的名字是:{name}, 我今年{age}岁了')

# 测试
print('测试提交')