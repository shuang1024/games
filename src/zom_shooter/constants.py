import pygame

WIDTH, HEIGHT = 800, 800
FPS = 60

BLACK = (0, 0, 0)
BG = (230, 217, 184)
TAN = (255, 200, 166)
PLAYER = (92, 47, 0)
BULLET = pygame.transform.scale(pygame.image.load("bullet.png"), (1920/100, 1080/100))
PISTOL = pygame.transform.scale(pygame.image.load("pistol.png"), (50, 50))
SHOTGUN = pygame.transform.scale(pygame.image.load("shotgun.png"), (50, 50))
ASSAULT_RIFLE = pygame.transform.scale(pygame.image.load("shotgun.png"), (50, 50))
ZOMBIE = (0, 176, 12)
BOSS = (0, 59, 16)
FAST = (0, 158, 76)
FIRE = (255, 68, 0)
WHITE = (255, 255, 255)

WEAPONS = [PISTOL, SHOTGUN, ASSAULT_RIFLE]