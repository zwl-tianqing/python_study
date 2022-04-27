"""
    @author long
    @time 2022/04/16 20:52
    @description 豌豆射手类
"""
import pygame


"""
    豌豆射手类
"""
class Peashooter(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, image_path):
        # 设置 图片连接
        self.image_path = image_path
        # 初始化精灵类
        pygame.sprite.Sprite.__init__(self)
        # 创建图片列表
        self.image_list = []
        # 加载图片
        for i in range(1,13):
            self.image_list.append(pygame.image.load(self.image_path + 'Peashooter-' + str(i) + '.png'))
        # 初始化图像
        self.image = self.image_list[0]
        # 改变图片大小
        self.image = pygame.transform.scale(self.image, (80, 80))
        # 设置图像编号
        self.index = 0
        # 获取矩形
        self.rect = self.image.get_rect()
        # 设置豌豆射手出现的位置
        self.rect.x = 200
        self.rect.y = 300

    # 更新方法
    def update(self):
        # 休眠一段时间
        pygame.time.wait(80)
        # 切换图片
        if self.index > -1:
            self.index = self.index + 1
            # 更换图片
            self.image = self.image_list[self.index]
            # 改变图片大小
            self.image = pygame.transform.scale(self.image, (80, 80))
            if self.index == 11:
                self.index = 0
