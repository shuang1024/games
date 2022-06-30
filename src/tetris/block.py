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
            board[self.x][self.y] = 7
        board[self.x][self.y] = self.type
