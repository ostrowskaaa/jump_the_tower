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
JUMP = 50
jumping = False

#events and jump
def jump():
    global playerY
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping =True
        playerY -= JUMP

def event():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


#game loop
while True:
    event()
    jump()
    duck = window.blit(player_icon, (playerX, playerY))
    pygame.display.update()
