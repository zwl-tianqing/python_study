# draw: 画
# star: 星星
# 导入海龟画图 取 别名为 tl
import turtle as tl
"""
     画五角星
"""
# 设置画笔大小
tl.pensize(3)
# 设置画笔颜色与填充颜色
print(tl.screensize())
tl.color('red', 'red')
# 设置画笔移动时不划线（抬笔）
tl.penup()
# 设置画笔位置
tl.goto(-200, 150)
# 设置落笔
tl.pendown()
# 开始填充颜色
tl.begin_fill()
for _ in range(5):
    tl.forward(200)
    tl.left(144)
tl.end_fill()
tl.mainloop()
