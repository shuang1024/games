import math, time

import pygame

from constants import *


class Player:
    def __init__(self):
        self.radius = 15
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.color = PLAYER
        self.drag = 0.9
        self.speed = 5
        self.x_speed = 0
        self.y_speed = 0
        self.bullets = []
        self.last_shot = time.time()
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.health = 100
        self.score = 0
        self.weapon = "pistol"

    def draw(self, display):
        pygame.draw.circle(display, BLACK, (self.x, self.y), self.radius+1)
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def move(self, keys):
        self.rect = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.x_speed *= self.drag
        self.y_speed *= self.drag

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > self.radius:
            self.x_speed = -self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < WIDTH-self.radius:
            self.x_speed = self.speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > self.radius:
            self.y_speed = -self.speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < HEIGHT-self.radius:
            self.y_speed = self.speed
    
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x < self.radius:
            self.x = self.radius
        elif self.x > WIDTH-self.radius:
            self.x = WIDTH-self.radius
        if self.y < self.radius:
            self.y = self.radius
        elif self.y > HEIGHT-self.radius:
            self.y = HEIGHT-self.radius

    def shoot(self, mouse, display):
        delay = 0
        if self.weapon == "shotgun":
            delay = 1
        elif self.weapon == "pistol":
            delay = 0.5
        elif self.weapon == "assault rifle":
            delay = 0.1

        if mouse.get_pressed()[0] and time.time() - self.last_shot > delay:
            self.last_shot = time.time()
            mouse_pos = mouse.get_pos()
            dir = (mouse_pos[0]-self.x, mouse_pos[1]-self.y)
            dir = math.atan2(dir[1], dir[0])
            if self.weapon == "shotgun":
                for i in range(-5, 6):
                    self.bullets.append(Bullet(self.x, self.y, dir - i * 0.1))
            else:
                self.bullets.append(Bullet(self.x, self.y, dir))

        for i in self.bullets:
            if i.gone:
                self.bullets.remove(i)
            else:
                i.update(display)

    def check_damage(self, zombie):
        if self.rect.colliderect(zombie.rect):
            self.health -= zombie.damage


class Bullet:
    def __init__(self, x, y, dir):
        self.dir = dir
        self.image = pygame.transform.rotate(BULLET, 180 - math.degrees(self.dir))
        self.x = x - self.image.get_width()//2
        self.y = y - self.image.get_height()//2
        self.speed = 10
        self.gone = 0

    def update(self, display):
        dir_x = math.cos(self.dir) * self.speed
        dir_y = math.sin(self.dir) * self.speed
        self.x += dir_x
        self.y += dir_y
        display.blit(self.image, (self.x, self.y))
