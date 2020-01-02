import pygame
from Camera import Camera
from Player import Player
from Platform import Platform
from Platform_controller import PlatformController
from pygame.locals import *

#colors
background = (123, 174, 163)
black = (0,0,0)
blue = (0,0, 255)
white = (255,255,255)

#window
pygame.init()
H = 650
W = 600
GRAVITY = 1
JUMP_SPEED = 15
MAX_JUMP = 150
window = pygame.display.set_mode((W, H))
window.fill(background)

#title and icon
pygame.display.set_caption("Jump the tower")
icon = pygame.image.load('duck.png')
pygame.display.set_icon(icon)

def reinit():
    global player
    global camera
    global platform_controller
    global floor
    player = Player()
    platform_controller = PlatformController()
    camera = Camera(player)
    floor = Platform(0, H-36, W, 36)

player = Player()
player.icon('duck-player.png')
platform_controller = PlatformController()
floor = Platform(0, H-36, W, 36)

selected_option = 0.30
camera = Camera(player)
clock = pygame.time.Clock()
fps = 60

def event():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game == False
                pygame.quit()
            # PLAYER JUMPS
            if event.key == K_SPACE:
                if player.on_any_platform(platform_controller, floor):
                    if player.speed_y >= JUMP_SPEED/2:
                        player.speed_y = -JUMP_SPEED

def game_over():
    if player.fallen_off_screen(camera) == True:
        window.fill(black)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reinit()
    return None

game = True
#game loop
while game:
        event()

        platform_controller.update()
        player.collide_platform(floor,0)
        player.update(platform_controller)
        platform_controller.collide_set(player)
        platform_controller.score = player.score
        camera.update(player.score)
        platform_controller.generate_new_platforms(camera)

        game_over()

        window.fill(background)
        floor.draw(window, camera)
        platform_controller.draw(window, camera)
        player.draw(window, camera)

        pygame.display.update()
        clock.tick(fps)
