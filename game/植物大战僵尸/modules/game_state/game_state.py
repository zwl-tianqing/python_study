"""'
    游戏状态类
"""
# 导入 pygame 游戏库
import pygame


class Game_State:

    # 初始化设置
    def __init__(self, width, height, title):
        # 游戏初始化
        pygame.display.init()
        # 设置游戏标题
        self.title = title
        pygame.display.set_caption(self.title)
        # 设置窗口大小
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    # 游戏开始加载方法
    def start_game(self, img_path):
        # 加载图片
        bg_img = pygame.image.load(img_path).convert()
        # 绘制图片
        self.screen.blit(bg_img, (0, 0))
