"""
    @Author : koolook_long
    @Time   : 2022-07-23
    @File   : 01_输入函数.py
    输入函数 ： input()
        1. 使用 input() 函数后，并不会立即往下执行程序，会一直等到你输入结束回车（enter键）后才算结束
        2. input()方法执行后会自动的的返回你输入的内容，为一段字符串，可用变量接受
"""
password = input('请输入你的密码：')
print(f"你的密码是：{password}")
