from copy import deepcopy

import pygame

from constants import *


class Block:
    def __init__(self, type):
        self.type = type
        if self.type == 3:
            self.x = B_WIDTH//2-2
        else:
            self.x = B_WIDTH//2-1
        self.y = -1

    def update_board(self, board):
        if self.y != 0:
            board[self.x][self.y-1] = 7
        board[self.x][self.y] = self.type

    def move(self, dir, board):
        if dir == "left" and self.x != 0:
            board[self.x][self.y] = 7
            self.x -= 1
        if dir == "right" and self.x != B_WIDTH-1:
            board[self.x][self.y] = 7
            self.x += 1
        if dir == "down":
            board[self.x][self.y] = 7
            for i in range(self.y+1, B_HEIGHT):
                if board[self.x][i] != 7:
                    max_y = i-1
                    break
                else:
                    max_y = B_HEIGHT-1
            self.y = max_y
            self.update_board(board)
