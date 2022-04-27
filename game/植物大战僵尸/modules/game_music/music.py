"""
    音乐播放类
"""
import pygame


class Music:

    # 初始化
    def __init__(self):
        # 初始化 pygame 音乐类
        pygame.mixer.init()

    # 播放音乐
    def music_play(self, music_path):
        # 加载音乐
        pygame.mixer.music.load(music_path)
        # 播放音乐 -1表示重复播放
        pygame.mixer.music.play(-1)
