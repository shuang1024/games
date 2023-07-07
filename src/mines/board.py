import random

import pygame

from constants import *


class Board:
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
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
        for i in self.offsets:
            if self._valid(y+i[0], x+i[1]):
                if self.g_board[y+i[0]][x+i[1]] == -2:
                    value += 1
        return value

    def _get_neighbors(self, y, x):
        neighbors = []
        for i in self.offsets:
            if self._valid(y+i[0], x+i[1]):
                neighbors.append((i, self.g_board[y+i[0]][x+i[1]]))
        return neighbors

    '''
    1    4    6

    2         7

    3    5    8
    '''

    def click(self, y, x):
        if self.g_board[y][x] != 0:
            self.d_board[y][x] = self.g_board[y][x]
        else:
            update = [(y, x)]
            prev_update = None
            while update != prev_update:
                prev_update = update
                for u in update:
                    n = self._get_neighbors(u[0], u[1])
                    for i in n:
                        if i[1] == 0:
                            if (u[0]+i[0][0], u[1]+i[0][1]) not in update:
                                update.append((u[0]+i[0][0], u[1]+i[0][1]))

            a = []
            for u in update:
                n = self._get_neighbors(u[0], u[1])
                for i in n:
                    if (u[0]+i[0][0], u[1]+i[0][1]) not in update:
                        a.append((u[0]+i[0][0], u[1]+i[0][1]))

            for i in a:
                update.append(i)

            for i in update:
                self.d_board[i[0]][i[1]] = self.g_board[i[0]][i[1]]

    def draw(self, display):
        for r in range(ROWS):
            for c in range(COLS):
                x = MARGIN + c*(SQ_SIZE + MARGIN)
                y = MARGIN + r*(SQ_SIZE + MARGIN)
                pygame.draw.rect(display, COLORS[self.d_board[r][c]], (x, y, SQ_SIZE, SQ_SIZE), border_radius=MARGIN)
                if self.d_board[r][c] in (1, 2, 3, 4, 5, 6, 7, 8):
                    tx = x + SQ_SIZE//2
                    ty = y + SQ_SIZE//2
                    text = STDFONT.render(str(self.d_board[r][c]), True, BLACK)
                    display.blit(text, (tx-text.get_width()//2, ty-text.get_height()//2))
