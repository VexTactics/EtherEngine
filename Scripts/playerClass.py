###Player Object Class

import pygame
import collisions
import globalVars as gv

class Player:
	hp, speed, sprite, location, = 0,0,0,0
	attackCooldown = 500
	lastAttacked = -1000

	facing = gv.dirUp

	def __init__(self, sprite):
		self.hp = 10
		self.speed = 10
		self.sprite = sprite
		self.location = sprite.get_rect()

	def actions(self, keys):

		#movement
		new_location = self.location.copy()
		new_facing = 0

		if keys[pygame.K_a]:
			new_location[0] -= 10
			new_facing = gv.dirLeft
		if keys[pygame.K_d]:
			new_location[0] += 10
			new_facing = gv.dirRight
		if keys[pygame.K_w]:
			new_location[1] -= 10
			new_facing = gv.dirUp
		if keys[pygame.K_s]:
			new_location[1] += 10
			new_facing = gv.dirDown



		if new_facing:
			self.facing = new_facing


		curTime = pygame.time.get_ticks()
		#if attack has cooled 
		if curTime - self.attackCooldown > self.lastAttacked:

			if not collisions.doesCollide(new_location):
				self.location = new_location

			#attacking
			if keys[pygame.K_j]:
				self.lastAttacked = curTime
				self.attack()


	def attack(self):

		#do attack
		attackLocation = [self.location[0], self.location[1]]
		attackLocation = [a+(b*30) + 8 for a,b in zip(attackLocation,self.facing)]
		newAttack = attackLocation + [30]

		gv.effects.append(newAttack)