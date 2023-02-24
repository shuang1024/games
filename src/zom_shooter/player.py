import pygame

from constants import *


class Player:
    def __init__(self):
        self.radius = 30
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.color = PLAYER
        self.drag = 0.7
        self.speed = 5
        self.x_speed = 0
        self.y_speed = 0

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def move(self, keys):
        self.x_speed *= self.drag
        self.y_speed *= self.drag
        # for i in map:
        #     if pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2).colliderect(*i):
        #         return

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