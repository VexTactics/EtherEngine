###Collisions

import pygame
import globalVars

def doesCollide(location):
	enemy_locations = []
	for enemy in globalVars.enemies:
		enemy_locations.append(enemy.location)
	wall_locations = []
	for wall in globalVars.walls:
		wall_locations.append(wall.location)

	if location.collidelist(enemy_locations) >= 0 or location.collidelist(wall_locations) >= 0:
		return True
	else:
		return False
