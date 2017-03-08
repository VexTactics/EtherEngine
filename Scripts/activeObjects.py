###Active Objects

import pygame
import globalVars


class EnemyObject:
	hp, sprite, location = 0,0,0
	
	def __init__(self, location = [1, 1, 16, 16], sprite = pygame.image.load(globalVars.spriteDirectory + "spr_enemy.png"), hp = 3):
		self.location = location.copy()
		self.sprite = sprite
		self.hp = hp





