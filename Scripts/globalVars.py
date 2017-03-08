###Global Variables
import random

import pygame
import collisions

global spriteDirectory 
spriteDirectory = "../sprites/"


global dirUp, dirDown, dirLeft, dirRight
dirUp, dirDown, dirLeft, dirRight = (0, -1), (0, 1), (-1, 0), (1, 0)
global dirList
dirList = [dirUp, dirLeft, dirDown, dirRight]


global rand
rand = random.Random()




def initialize():
	pygame.init()

	global walls
	global enemies	
	global effects
	global clock


	walls = []
	enemies = []
	effects = []
	clock = pygame.time.Clock()

