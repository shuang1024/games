from copy import deepcopy

import pygame

from constants import *


class Block:
    def __init__(self, type, offsets):
        self.type = type
        if self.type == LONG:
            self.x = B_WIDTH//2-2
        else:
            self.x = B_WIDTH//2-1
        self.y = -1
        self.offsets = offsets

        self.max_off_y = 0
        for i in self.offsets:
            self.max_off_y = max(i[1], self.max_off_y)
        self.max_off_x = 0
        for i in self.offsets:
            self.max_off_x = max(i[0], self.max_off_x)

    def is_end(self, board):
        for i in self.offsets:
            currx = self.x+i[0]
            curry = self.y+i[1]
            if curry < B_HEIGHT-self.max_off_y:
                if board[currx][curry+1] != BG:
                    return True
            else:
                return True

    def update_board(self, board):
        for i in self.offsets:
            board[self.x+i[0]][self.y+i[1]] = self.type

    def move(self, dir, board):
        if dir == "left" and self.x > 0:
            for i in self.offsets:
                board[self.x+i[0]][self.y+i[1]] = BG
            self.x -= 1
        if dir == "right" and self.x < B_WIDTH-self.max_off_x-1:
            for i in self.offsets:
                board[self.x+i[0]][self.y+i[1]] = BG
            self.x += 1
        if dir == "down":
            for i in self.offsets:
                board[self.x+i[0]][self.y+i[1]] = BG
            for i in range(B_HEIGHT-self.y):
                self.y += 1
                if self.is_end(board):
                    break
