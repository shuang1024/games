import pygame

from constants import *


class Snake:
    def __init__(self):
        self.reset()
        self.color = SNAKE
        self.head_color = SNAKE_HEAD

    def reset(self):
        self.length = 3
        self.x = 3
        self.y = 7
        self.positions = [(self.x, self.y)]
        self.dir = (0, 0)
        self.score = 0

    def draw(self, display):
        for i in self.positions:
            if self.positions.index(i) == 0:
                pygame.draw.rect(display, self.head_color, (MARGIN + i[0]*SQ_SIZE, MARGIN + i[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                pygame.draw.rect(display, self.color, (MARGIN + i[0]*SQ_SIZE, MARGIN + i[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def check_lose(self):
        if self.positions[0][0] < 0 or self.positions[0][0] > COLS-1 or self.positions[0][1] < 0 or self.positions[0][1] > ROWS-1 \
            or self.positions[0] in self.positions[1:]:
            self.reset()

    def move(self):
        head = self.positions[0]
        x, y = self.dir
        new_head = (((head[0] + x*SQ_SIZE) % COLS), ((head[1] + y*SQ_SIZE) % ROWS))
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

        self.x += self.dir[0]
        self.y += self.dir[1]
        self.positions[0] = (self.x, self.y)

    def keys(self, keys):
        if keys[pygame.K_LEFT] and self.dir[0] == 0:
            self.dir = (-1, 0)
        if keys[pygame.K_RIGHT] and self.dir[0] == 0:
            self.dir = (1, 0)
        if keys[pygame.K_UP] and self.dir[1] == 0:
            self.dir = (0, -1)
        if keys[pygame.K_DOWN] and self.dir[1] == 0:
            self.dir = (0, 1)
