###Wall Object Class

import pygame
import globalVars as gv

class Wall:
	sprite = 0
	location = [0,0,0,0]
	
	def __init__(self, coords = [1, 1], sprite = pygame.image.load(gv.spriteDirectory + "spr_wall.png")):
		self.sprite = sprite
		self.location = sprite.get_rect()
		self.location[0] = coords[0]
		self.location[1] = coords[1]

		gv.walls.append(self)