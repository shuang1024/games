import pygame

WIDTH, HEIGHT = 800, 800
FPS = 60

BLACK = (0, 0, 0)
WHITE = (230, 217, 184)
TAN = (255, 200, 166)
PLAYER = (92, 47, 0)
BULLET = pygame.transform.scale(pygame.image.load("bullet.png"), (1920/40, 1080/40))