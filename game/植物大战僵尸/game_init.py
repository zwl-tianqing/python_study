"""
    游戏初始化类
"""
# 导入包
import pygame
import sys
from modules.game_state.game_state import Game_State
from modules.game_music.music import Music
from modules.plant.peashooter import Peashooter


class Game_Init:

    # 定义主方法
    def main(self):
        # 创建游戏状态对象
        game_state = Game_State(960, 720, "植物大战僵尸")
        # 加载游戏开始场景
        game_state.start_game('./resources/Image/map/bg.png')
        # 创建音乐对象
        music = Music()
        # 播放音乐
        music.music_play('./resources/music/尘ah_ - 落霜.mp3')
        # 创建豌豆射手类
        peashooter = Peashooter('./resources/Image/plant/Peashooter/')
        # 获取精灵组
        all_sprite = pygame.sprite.Group()
        # 将豌豆射手加入模组
        all_sprite.add(peashooter)
        # 设置游戏运行状态
        run = True
        # 创建更新频率
        FPS = 30        # 获取适中
        clock = pygame.time.Clock()
        # 开始游戏
        while run:
            # 判断点击事件
            for event in pygame.event.get():
                # 判断是否点击退出
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # 重新绘制背景
            game_state.start_game('./resources/Image/map/bg.png')
            # 调用精灵组刷新方法
            all_sprite.update()
            all_sprite.draw(game_state.screen)
            # 刷新屏幕
            pygame.display.update()
            # 设置刷新频率
            clock.tick(FPS)


if __name__ == '__main__':
    game_init = Game_Init()
    game_init.main()
