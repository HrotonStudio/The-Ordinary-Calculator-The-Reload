import os, sys, time, pygame, threading, playsound
from concurrent.futures import ThreadPoolExecutor
os.system("cls")

music_dir = "resources\\music"

the_music_list = [os.path.join(music_dir, f) for f in os.listdir(music_dir)]


def play_music(music_list: list):
    pygame.mixer.init()
    for music in music_list:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()

    