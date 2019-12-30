import pygame
from Camera import Camera
from Player import Player
from Platform import Platform
from Platform_controller import PlatformController

#colors
background = (123, 174, 163)
black = (0,0,0)
blue = (0,0, 255)
white = (255,255,255)

#window
pygame.init()
H = 600
W = 650
GRAVITY = 1
JUMP_VELOCITY = 15
MAX_JUMP = 150
window = pygame.display.set_mode((H, W))
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
platform_controller = PlatformController()
floor = Platform(0, H-36, W, 36)

selected_option = 0.30
camera = Camera(player)
clock = pygame.time.Clock()
fps = 60

def event():
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

#game loop
while True:
        event()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            if player.on_any_platform(platform_controller, floor):
                player.sprite_index_y = 3
                if player.vel_y >= JUMP_VELOCITY/2:
                    player.vel_y = -JUMP_VELOCITY
            if player.fallen_off_screen(camera):
                window.fill(black)
                if event.type == pygame.K_SPACE:
                    reinit()

        player.update()
        player.combo()
        player.collide_platform(floor,0)
        platform_controller.collide_set(player)
        platform_controller.score = player.score
        camera.update(player.score)
        platform_controller.generate_new_platforms(camera)


        pygame.display.update()
        clock.tick(fps)
