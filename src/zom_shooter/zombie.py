import math, random

import pygame

from constants import *


class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = ZOMBIE
        self.damage_color = WHITE
        self.speed = random.randint(3, 5)
        self.health = 10
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

    def draw(self, display):
        pygame.draw.circle(display, BLACK, (self.x, self.y), self.radius+1)
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def move(self, player):
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        dir = math.degrees(math.atan2(player.y - self.y, player.x - self.x))
        dir_x = math.cos(math.radians(dir)) * self.speed
        dir_y = math.sin(math.radians(dir)) * self.speed
        self.x += dir_x
        self.y += dir_y

        for i in player.bullets:
            if i.image.get_rect(topleft=(i.x, i.y)).colliderect(self.rect):
                self.health -= 1
                i.gone = True