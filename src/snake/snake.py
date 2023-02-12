import pygame

from constants import *


class Snake:
    def __init__(self):
        self.reset()
        self.color = SNAKE

    def reset(self):
        self.length = 1
        self.x = 3
        self.y = 7
        self.positions = [(self.x, self.y)]
        self.dir = (0, 0)

    def draw(self, display):
        self.x += self.dir[0]
        self.y += self.dir[1]
        if self.x < 0 or self.x > COLS or self.y < 0 or self.y > ROWS:
            self.reset()
        self.positions[0] = (self.x, self.y)
        for i in self.positions:
            pygame.draw.rect(display, self.color, (MARGIN + i[0]*SQ_SIZE, MARGIN + i[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.dir = (-1, 0)
        if keys[pygame.K_RIGHT]:
            self.dir = (1, 0)
        if keys[pygame.K_UP]:
            self.dir = (0, -1)
        if keys[pygame.K_DOWN]:
            self.dir = (0, 1)

        head = self.positions[0]
        x, y = self.dir
        new_head = (((head[0] + x*SQ_SIZE) % COLS), ((head[1] + y*SQ_SIZE) % ROWS))
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            pass
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()

