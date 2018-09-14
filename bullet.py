# -*- coding: utf-8 -*-

# Created on Sun Jan 14 19:45:07 2018
import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('image/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position  #???    位置参数
        self.speed = 12
        self.active = False    # ???
        self.mask = pygame.mask.from_surface(self.image) # 标记子弹1非透明区域
        
    def move(self):
        self.rect.top -= self.speed
        
        
        if self.rect.top < 0:
            self.active = False
            
    def reset(self,position):
        self.rect.left,self.rect.top = position  #位置参数
        self.active = True
        
class Bullet2(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('image/bullet2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position  #???    位置参数
        self.speed = 12
        self.active = False     # ???
        self.mask = pygame.mask.from_surface(self.image) # 标记子弹1非透明区域
        
    def move(self):
        self.rect.top -= self.speed
        
        
        if self.rect.top < 0:
            self.active = False
            
    def reset(self,position):
        self.rect.left,self.rect.top = position  #位置参数
        self.active = True
        
        


