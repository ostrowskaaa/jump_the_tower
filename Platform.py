from random import randint
import pygame
pygame.init()
from copy import deepcopy
'''
X<600
Y<650
'''
class Platform:
	color = (0, 100, 100)
	vel_x = 0
	vel_y = 0
	vel = 1
	def __init__(self, x, y, width, height):
		self.direction = -1 if randint(0, 1) == 0 else 1
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.rect = pygame.Rect(x, y, width, height)
		self.collected_score = False

	def update(self):
		if self.x + self.width < 600:
			self.vel_x = self.direction * self.vel
			self.x += self.vel_x
			if self.x <= 0 or self.x + self.width >= 600:
				self.direction *= -1
				self.vel_x = self.direction * self.vel
				self.x += self.vel_x
			self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self, window, camera):
		rect = deepcopy(self.rect)
		rect.top -= camera.y
		pygame.draw.rect(window, self.color, rect)
