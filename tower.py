import pygame
from pygame.locals import *
import sys

#colors
background = (123, 174, 163)

#window
pygame.init()
H, W = 600, 650
window = pygame.display.set_mode((H, W))
window.fill(background)

#title and icon
pygame.display.set_caption("Jump the tower")
icon = pygame.image.load('duck.png')
pygame.display.set_icon(icon)

#player
player_icon = pygame.image.load('duck.png')
playerX = 300
playerY = 550
jumping = False
jumping_count = 10

#events and jump
def jump(player):
    global jumping
    global jumping_count
    global playerY
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping = True
    else:
        if jumping_count >= -10:
            playerY -= (jumping_count ** 2) * 0.5
            jumping_count -= 1
        else:
            jumping = False
            jumping_count = 10


def event():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

duck = window.blit(player_icon, (playerX, playerY))

#game loop
while True:
    event()
    jump(duck)
    pygame.display.update()
