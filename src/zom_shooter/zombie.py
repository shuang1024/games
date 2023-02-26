import math, random, time

import pygame

from constants import *


class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.normal_color = ZOMBIE
        self.damage_color = WHITE
        self.color = self.normal_color
        self.speed = random.randint(3, 5)
        self.health = 5
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.damage = 0.5
        self.last_damage = time.time()
        self.last_dir_change = 0
        self.rand_dir = 0
        self.type = "zombie"
        self.know_player = False

    def draw(self, display):
        pygame.draw.circle(display, BLACK, (self.x, self.y), self.radius+1)
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def move(self, player):
        curr_know = self.know_player
        if self.type == "zombie":
            distance = math.hypot(self.x-player.x, self.y-player.y)
            if distance < 300:
                curr_know = True
        else:
            curr_know = True

        if curr_know:
            dir = math.degrees(math.atan2(player.y - self.y, player.x - self.x))
        else:
            if time.time() - self.last_dir_change > 2 or self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
                self.rand_dir = random.uniform(0, 360)
                self.last_dir_change = time.time()
            dir = self.rand_dir

        dir_x = math.cos(math.radians(dir)) * self.speed
        dir_y = math.sin(math.radians(dir)) * self.speed
        self.x += dir_x
        self.y += dir_y
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

        for i in player.bullets:
            if i.image.get_rect(topleft=(i.x, i.y)).colliderect(self.rect):
                self.know_player = True
                self.health -= 1
                self.color = self.damage_color
                i.gone = True
                self.last_damage = time.time()
            else:
                if time.time() - self.last_damage > 0.1:
                    self.color = self.normal_color


class Zombie_Boss(Zombie):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 30
        self.speed = 2
        self.normal_color = BOSS
        self.health = 10
        self.damage = 2
        self.type = "boss"


class Fast_Zombie(Zombie):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 10
        self.speed = 8
        self.normal_color = FAST
        self.health = 5
        self.damage = 2
        self.type = "fast"