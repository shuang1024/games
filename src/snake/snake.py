import pygame

from constants import *


class Snake:
    def __init__(self):
        self.reset()
        self.color = SNAKE

    def reset(self):
        self.length = 3
        self.x = 3
        self.y = 7
        self.positions = [(self.x, self.y)]
        self.dir = (0, 0)
        self.score = 0

    def draw(self, display):
        for i in self.positions:
            pygame.draw.rect(display, self.color, (MARGIN + i[0]*SQ_SIZE, MARGIN + i[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def move(self):
        head = self.positions[0]
        x, y = self.dir
        new_head = (((head[0] + x*SQ_SIZE) % COLS), ((head[1] + y*SQ_SIZE) % ROWS))
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()

        self.x += self.dir[0]
        self.y += self.dir[1]
        if self.x < 0 or self.x > COLS-1 or self.y < 0 or self.y > ROWS-1:
            self.reset()
        self.positions[0] = (self.x, self.y)

    def keys(self, keys):
        if keys[pygame.K_LEFT] and self.dir != (1, 0):
            self.dir = (-1, 0)
        if keys[pygame.K_RIGHT] and self.dir != (-1, 0):
            self.dir = (1, 0)
        if keys[pygame.K_UP] and self.dir != (0, 1):
            self.dir = (0, -1)
        if keys[pygame.K_DOWN] and self.dir != (0, -1):
            self.dir = (0, 1)
