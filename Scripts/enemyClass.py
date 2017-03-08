###Enemy Object Class

import random

import pygame
import globalVars as gv

class Enemy:
	hp, sprite, location = 0,0,0
	speed = 5
	
	def __init__(self, coords = [50,50], sprite = pygame.image.load(gv.spriteDirectory + "spr_enemy.png"), hp = 3):
		self.sprite = sprite
		self.location = sprite.get_rect()
		self.location[0] = coords[0]
		self.location[1] = coords[1]


	def randomWalk(self):
		direction = gv.dirList[gv.rand.randrange(4)]
		self.location[0] += direction[0] * self.speed
		self.location[1] += direction[1] * self.speed


