import random

import pygame

from constants import *


class Board:
    def __init__(self):
        self.board = []
        for i in range(ROWS):
            self.board.append([])
            for j in range(COLS):
                self.board[i].append("-")
        self._place_mines()
        self._update()

    def _place_mines(self):
        xy = []
        for i in range(MINES):
            mx = random.randint(0, COLS-1)
            my = random.randint(0, ROWS-1)
            while (my, mx) in xy:
                mx = random.randint(0, COLS-1)
            xy.append((my, mx))
            self.board[my][mx] = "X"

    def _get_value(self, x, y):
        value = 0
        try:
            if self.board[y-1][x-1] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y][x-1] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y+1][x-1] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y-1][x] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y+1][x] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y-1][x+1] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y][x+1] == "X":
                value += 1
        except:
            pass
        try:
            if self.board[y+1][x+1] == "X":
                value += 1
        except:
            pass

        return value

    def _get_neighbors(self, x, y):
        neighbors = []
        try:
            neighbors.append(self.board[y-1][x-1])
        except:
            pass
        try:
            neighbors.append(self.board[y][x-1])
        except:
            pass
        try:
            neighbors.append(self.board[y+1][x-1])
        except:
            pass
            neighbors.append(self.board[y-1][x])
        try:
            neighbors.append(self.board[y+1][x])
        except:
            pass
        try:
            neighbors.append(self.board[y-1][x+1])
        except:
            pass
        try:
            neighbors.append(self.board[y][x+1])
        except:
            pass
        try:
            neighbors.append(self.board[y+1][x+1])
        except:
            pass

        return neighbors

    def _update(self):
        for y in range(ROWS):
            for x in range(COLS):
                if self.board[y][x] != "X":
                    self.board[y][x] = self._get_value(x, y)

    def draw(self, display):
        self._update()
        display.fill(BG)
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] != "X":
                    pygame.draw.rect(display, COLORS[int(self.board[r][c])], (MARGIN + c*(SQ_SIZE + MARGIN), MARGIN + r*(SQ_SIZE + MARGIN), SQ_SIZE, SQ_SIZE), border_radius=5)
