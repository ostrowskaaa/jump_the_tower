import pygame
pygame.init()
from copy import deepcopy

H = 600
W = 650
GRAVITY = 1
background = (123, 174, 163)
window = pygame.display.set_mode((H, W))
window.fill(background)

class Player:
	width = 30
	height = 50
	speed_x = 0
	speed_y = 0
	max_falling_speed = 20
	acceleration = 0.5
	max_speed_x = 7

	def __init__(self):
		self.x = W/2 - 16
		self.y = 590
		self.player_icon = None
		self.rect = None
		self.score = -10

	def icon(self, player_icon):
		self.player_icon = pygame.image.load(player_icon)
		self.rect = self.player_icon.get_rect()

	def draw(self, window, camera):
		window.blit(self.player_icon, (self.x, self.y - camera.y))

	def update(self, platform_controller):
		platform = self.get_platform_player_standing(platform_controller)
		if platform:
			self.speed_x = platform.speed_x
		else:
			self.speed_x = 0

		self.x += self.speed_x
		self.y += self.speed_y
		self.speed_y += GRAVITY
		if self.speed_y > self.max_falling_speed:
			self.speed_y = self.max_falling_speed
		if self.x <= 0:
			self.x = 0
		if self.x + self.width >= W:
			self.x = W - self.width

	def get_platform_player_standing(self, platform_controller):
		for p in platform_controller.platform_set:
			if self.on_platform(p):
				return p
		return None 

	def on_platform(self, platform):
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
		for i in range(0,self.speed_y):
			if pygame.Rect(self.x, self.y-i, self.width, self.height).colliderect(platform.rect):
				if platform.rect.collidepoint((self.x, self.y + self.height-i)) or \
		 	platform.rect.collidepoint((self.x+self.width, self.y + self.height-i)): #do not change! no on_platform here
					self.y = platform.y - self.height
					if not platform.collected_score:
						self.score += 10
						if self.score < index * 10:
							self.score = index * 10
						platform.collected_score = True

	def fallen_off_screen(self, camera):
		if self.y - camera.y + self.height >= H:
			return True
		return False
