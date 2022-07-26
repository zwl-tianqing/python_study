[toc]

## Python 打印函数的使用

### 1  打印函数 print() 的使用

* print()
  
> 使用 print 进行输出打印
  
```python
# 你好 ，世界。学习语言的第一步
print("hello word")
```

* print 打印多个变量

> print 打印多个变量使用逗号隔开
>
> print(a,b)

* print函数中参数的含义

> print（var,.....,sep=" ")
>
> sep 表示打印变量之间的分隔符，默认使用空格


### 2 格式化输出


格式符号|转换
--:|:--:|
%s|字符串
%d|有符号的十进制数
%f|浮点数
%c|字符
%u|无符号的十进制数（无正负数之分）


```python
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

# 3 我的体重是 --浮点型 %f 在 % 与 f 之间加上 .x 表示保留 x 为小数，默认保留 6为小数
print('我的体重是%.2f' % weight)

"""
 4 输出学号 如何将数据格式化输出
    将 学号 1，使用 格式 001 
    输出三位格式，不足的按 0 补全
    在 %d 之间加上  %0xd 就表示数据按 
    x 位输出，不足的按 0 补齐，超出的数位 按原样输出
"""
print('我的学号是%03d' % stu_id)
stu_id2 = 234542
print('我的学号是%03d' % stu_id2)

# 5 输出多个变量
print('我的学号是%03d,我的年龄是%d,我的体重是%.2f' %(stu_id, age, weight))
```

* f'{ }'表达式，能够简介明了的表达数据 在 3.6 版本出现

```python
name = 'TOM'
age = 18

# 输出数据
print(f'我的名字是{name}, 今年{age} 岁')
```

### 3 转义字符

* `\n`: 换行
* `\t`: 制表符，一个 tab 键（4个字符）的距离

```python
print("hello\nwold")
print("\thello")
```

### 4 结束符

> 想一想，为什么两个print会换行

```python
# print 函数中有个 end 的参数，这个参数默认值为 \n 换行字符
print('内容',end="\n")
```