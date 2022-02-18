# 智能抠图
# 引入removebg中的RemoveBg工具
from removebg import RemoveBg

# 调用RemoveBg工具创建抠图实例，将抠图实例重新命名为rmbg
rmbg = RemoveBg("sMUAw4jKgQHaoyvsH4HKR4U3", "error.log")

# 调用工具的rmbgremove_background_from_img_file()方法进行扣图
rmbg.remove_background_from_img_file("meixi.jpg")
