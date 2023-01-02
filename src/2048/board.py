import random
import math
from copy import deepcopy

import pygame

from constants import *


class Board:
    def __init__(self):
        self.board = []
        self.reset_board()

        x1 = random.randint(0, 3)
        y1 = random.randint(0, 3)
        x2 = random.randint(0, 3)
        y2 = random.randint(0, 3)
        while (x1, y1) == (x2, y2):
            x2 = random.randint(0, 3)
            y2 = random.randint(0, 3)
        self.board[y1][x1] = random.choice(("2", "4"))
        self.board[y2][x2] = "2"

    def reset_board(self):
        self.board = []
        for i in range(4):
            self.board.append([])
            for j in range(4):
                self.board[i].append("0")

    def spawn_block(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while self.board[y][x] != "0":
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.board[y][x] = "2"

    def text_block_loc(self, text, i, j):
        x = j*(SQ_SIZE + PADDING) + PADDING + SQ_SIZE//2 - text.get_width()//2
        y = i*(SQ_SIZE + PADDING) + PADDING + SQ_SIZE//2 - text.get_height()//2
        return x, y

    def move_step(self, direction):
        if direction == "r":
            for i in range(4):
                for j in range(4):
                    if j < 3 and self.board[i][j] != "0":
                        if self.board[i][j+1] == self.board[i][j]:
                            self.board[i][j], self.board[i][j+1] = "0", str(int(self.board[i][j]) * 2)
                        if self.board[i][j+1] == "0":
                            self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]

        if direction == "l":
            for i in range(4):
                for j in reversed(range(4)):
                    if j > 0 and self.board[i][j] != "0":
                        if self.board[i][j-1] == self.board[i][j]:
                            self.board[i][j], self.board[i][j-1] = "0", str(int(self.board[i][j]) * 2)
                        if self.board[i][j-1] == "0":
                            self.board[i][j], self.board[i][j-1] = self.board[i][j-1], self.board[i][j]

        if direction == "u":
            for i in reversed(range(4)):
                for j in range(4):
                    if i > 0 and self.board[i][j] != "0":
                        if self.board[i-1][j] == self.board[i][j]:
                            self.board[i][j], self.board[i-1][j] = "0", str(int(self.board[i][j]) * 2)
                        if self.board[i-1][j] == "0":
                            self.board[i][j], self.board[i-1][j] = self.board[i-1][j], self.board[i][j]

        if direction == "d":
            for i in range(4):
                for j in range(4):
                    if i < 3 and self.board[i][j] != "0":
                        if self.board[i+1][j] == self.board[i][j]:
                            self.board[i][j], self.board[i+1][j] = "0", str(int(self.board[i][j]) * 2)
                        if self.board[i+1][j] == "0":
                            self.board[i][j], self.board[i+1][j] = self.board[i+1][j], self.board[i][j]

    def move(self, direction):
        revs = 0
        while True:
            prev_brd = deepcopy(self.board)
            self.move_step(direction)
            if self.board == prev_brd:
                break
            revs += 1

        if revs:
            self.spawn_block()

    def draw(self, display):
        pygame.draw.rect(display, DARK_BROWN, (0, 0, WIDTH, HEIGHT-100))
        for r in range(4):
            for c in range(4):
                pygame.draw.rect(display, LIGHT_BROWN, (c*(SQ_SIZE + PADDING) + PADDING, r*(SQ_SIZE + PADDING) + PADDING, SQ_SIZE, SQ_SIZE), 0, 5)

        for i in range(4):
            for j in range(4):
                if bool(int(self.board[i][j])):
                    color = BLOCK_COLORS[int(math.log(int(self.board[i][j])-1, 2))]
                    pygame.draw.rect(display, color, (j*(SQ_SIZE + PADDING) + PADDING, i*(SQ_SIZE + PADDING) + PADDING, SQ_SIZE, SQ_SIZE), 0, 5)
                    if int(self.board[i][j])-1 <= 4:
                        text = NUMBER_FONTS[int(math.log(int(self.board[i][j])-1, 2))].render(self.board[i][j], True, DARK_TEXT)
                    else:
                        text = NUMBER_FONTS[int(math.log(int(self.board[i][j])-1, 2))].render(self.board[i][j], True, LIGHT_TEXT)
                    display.blit(text, (self.text_block_loc(text, i, j)[0], self.text_block_loc(text, i, j)[1], SQ_SIZE, SQ_SIZE))