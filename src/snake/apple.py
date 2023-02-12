import random

import pygame

from constants import *


class Apple:
    def __init__(self, snake):
        self.snake = snake
        self.random_pos(self.snake)
        self.color = APPLE

    def random_pos(self, snake):
        self.x, self.y = random.randint(0, COLS), random.randint(0, ROWS)

        while (self.x, self.y) in snake.positions:
            self.x, self.y = random.randint(0, COLS), random.randint(0, ROWS)

    def draw(self, display):
        pygame.draw.circle(display, self.color, (MARGIN + self.x*SQ_SIZE + SQ_SIZE//2, MARGIN + self.y*SQ_SIZE + SQ_SIZE//2), SQ_SIZE//2)