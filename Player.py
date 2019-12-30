import pygame
pygame.init()
from copy import deepcopy

H = 600
W = 650
GRAVITY = 1
player_icon = pygame.image.load('duck.png')
playerX = 300
playerY = 550

class Player:
	width = 30
	height = 50
	vel_x = 0
	vel_y = 0
	max_falling_speed = 20
	acceleration = 0.5
	max_vel_x = 7
	speed = 5

	def __init__(self):
		self.x = 30
		self.y = 500
		self.score = -10 # negate floor platform

		self.player_icon = pygame.image.load('duck.png')
		self.player_icon = pygame.Surface((33, 57), pygame.SRCALPHA, 32)
		self.player_icon.blit(self.player_icon, (playerX, playerY), (75, 112, 33, 57))

	def update(self):
		self.x += self.vel_x
		self.y += self.vel_y
		self.vel_y += GRAVITY
		if self.vel_y > self.max_falling_speed:
			self.vel_y = self.max_falling_speed
		if self.x <= 0:
			self.x = 0
		if self.x + self.width >= W:
			self.x = W - self.width

	def combo(self):
		if self.x == 0:
			if self.vel_y < 0:
				if self.vel_x < 0:
					self.vel_y -= 10
					self.vel_x *= -2.5
		if self.x + self.width >= W:
			if self.vel_y < 0:
				if self.vel_x > 0:
					self.vel_y -= 10
					self.vel_x *= -2.5

	def on_platform(self, platform):
		# return platform.rect.top <= self.y + self.height
		return platform.rect.collidepoint((self.x, self.y + self.height)) or \
			platform.rect.collidepoint((self.x+self.width, self.y + self.height))

	def on_any_platform(self, platform_controller, floor):
		for p in platform_controller.platform_set:
			if self.on_platform(p):
				return True
		if self.on_platform(floor):
			return True
		return False

	def collide_platform(self, platform, index):
		for i in range(0,self.vel_y):
			if pygame.Rect(self.x, self.y-i, self.width, self.height).colliderect(platform.rect):
				if platform.rect.collidepoint((self.x, self.y + self.height-i)) or \
		 	platform.rect.collidepoint((self.x+self.width, self.y + self.height-i)): #do not change! no on_platform here
					self.y = platform.y - self.height
					if not platform.collected_score:
						self.score += 10
						if self.score < index * 10:
							self.score = index * 10
						platform.collected_score = True

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def fallen_off_screen(self, camera):
		if self.y - camera.y + self.height >= H:
			return True
		return False
