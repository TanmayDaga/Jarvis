import os
import json
from pygame import mixer
import pygame
import time
from parallelProcessing import createProcesses
from tinytag import TinyTag
from functools import partial

class Music:
    def __init__(self) -> None:
        
        self.__play= False
        self.__curr_index = 0
        self.__music_list = []
        i = 0
        for root, dir, files in os.walk("/Users/tanmay06daga/Music/Music/Media.localized/Music"):
            for file in files:
                if file.endswith('.mp3'):
                    path = os.path.join(root, file)
                    self.__music_list.append((i,path))
                    i+=1
        
    def get_music_list(self):
        """Music list with its index"""
        ls = []
        for items in self.__music_list:
            ls.append((items[0], os.path.basename(items[1])))
        return ls
    def play(self, index):
        if self.__play == False:
            createProcesses(partial(self.__playMusic, index))
        else:
            mixer.music.stop()
            createProcesses(partial(self.__playMusic, index))

    def __playMusic(self, index = 0):
        mixer.init()
      
        mixer.music.load(str(self.__music_list[index][1]))
        mixer.music.play(loops=-1)
        self.__play = True
        self.__curr_index = index
  
                    
obj = Music()
print(obj.play(0))