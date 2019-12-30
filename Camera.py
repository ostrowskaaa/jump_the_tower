import pygame
import math

H = 600

class Camera:
	def __init__(self, player):
		self.y = 0
		self.player = player

	def update(self, score):
		if self.player.y - self.y <= H / 2:
			self.y = self.player.y - H /2
		if self.player.y < H / 2:
			change = int(math.sqrt(score))/10
			if not change:
				self.y -= 1
			if(change<4):
				self.y -= change
			else:
				self.y -= 4
