# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:07:06 2018

@author: sb
"""

import pygame
import time

pygame.mixer.init()



pygame.time.delay(1000)

game__music = pygame.mixer.Sound("sound1/game_music.wav")

game__music.play()


enemy3_fly_sound = pygame.mixer.Sound("sound1/bullet.wav")
pygame.mixer.music.set_volume(0.4)
#pygame.mixer.music.play()
enemy3_fly_sound.play()

pygame.time.delay(1000)

#game_bullet = pygame.mixer.music.load('sound/enemy2_down.wav')

#pygame.mixer.music.play()


#game_over = pygame.mixer.music.load('sound1/game_over.mp3')
#pygame.mixer.music.play()


#get_bomb = pygame.mixer.music.load('sound1/get_bomb.mp3')
#pygame.mixer.music.play()




