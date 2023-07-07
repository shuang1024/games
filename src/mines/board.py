import random

import pygame

from constants import *


class Board:
    def __init__(self):
        self.d_board = []
        for i in range(ROWS):
            self.d_board.append([])
            for j in range(COLS):
                self.d_board[i].append(-1)

        self.g_board = []
        for i in range(ROWS):
            self.g_board.append([])
            for j in range(COLS):
                self.g_board[i].append(-1)
        self.mines = self._place_mines()
        for y in range(ROWS):
            for x in range(COLS):
                if self.g_board[y][x] != -2:
                    self.g_board[y][x] = self._get_value(y, x)

    def _place_mines(self):
        xy = []
        for i in range(MINES):
            mx = random.randint(0, COLS-1)
            my = random.randint(0, ROWS-1)
            while (my, mx) in xy:
                mx = random.randint(0, COLS-1)
                my = random.randint(0, ROWS-1)
            xy.append((my, mx))
            self.g_board[my][mx] = -2

        return xy

    def _valid(self, y, x):
        if y > -1 and y < ROWS:
            if x > -1 and x < COLS:
                return True
            return False
        return False

    def _get_value(self, y, x):
        value = 0
        try:
            if self.g_board[y-1][x-1] == -2 and self._valid(y-1, x-1):
                value += 1
        except:
            pass
        try:
            if self.g_board[y][x-1] == -2 and self._valid(y, x-1):
                value += 1
        except:
            pass
        try:
            if self.g_board[y+1][x-1] == -2 and self._valid(y+1, x-1):
                value += 1
        except:
            pass
        try:
            if self.g_board[y-1][x] == -2 and self._valid(y-1, x):
                value += 1
        except:
            pass
        try:
            if self.g_board[y+1][x] == -2 and self._valid(y+1, x):
                value += 1
        except:
            pass
        try:
            if self.g_board[y-1][x+1] == -2 and self._valid(y-1, x+1):
                value += 1
        except:
            pass
        try:
            if self.g_board[y][x+1] == -2 and self._valid(y, x+1):
                value += 1
        except:
            pass
        try:
            if self.g_board[y+1][x+1] == -2 and self._valid(y+1, x+1):
                value += 1
        except:
            pass

        return value

    def _get_neighbors(self, y, x):
        neighbors = []
        try:
            neighbors.append(self.g_board[y-1][x-1])
        except:
            pass
        try:
            neighbors.append(self.g_board[y][x-1])
        except:
            pass
        try:
            neighbors.append(self.g_board[y+1][x-1])
        except:
            pass
        try:
            neighbors.append(self.g_board[y-1][x])
        except:
            pass
        try:
            neighbors.append(self.g_board[y+1][x])
        except:
            pass
        try:
            neighbors.append(self.g_board[y-1][x+1])
        except:
            pass
        try:
            neighbors.append(self.g_board[y][x+1])
        except:
            pass
        try:
            neighbors.append(self.g_board[y+1][x+1])
        except:
            pass

        return neighbors

    '''
    1    4    6

    2         7

    3    5    8
    '''

    def click(self, y, x):
            self.d_board[y][x] = self.g_board[y][x]

    def draw(self, display):
        for r in range(ROWS):
            for c in range(COLS):
                pygame.draw.rect(display, COLORS[self.d_board[r][c]], (MARGIN + c*(SQ_SIZE + MARGIN), MARGIN + r*(SQ_SIZE + MARGIN), SQ_SIZE, SQ_SIZE), border_radius=MARGIN)
