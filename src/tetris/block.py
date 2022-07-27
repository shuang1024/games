import pygame

from constants import *


class Block:
    def __init__(self, type, offsets):
        self.type = type
        if self.type == LONG:
            self.x = B_WIDTH//2-2
        else:
            self.x = B_WIDTH//2-1
        self.offsets = offsets
        self.rot_index = 0
        
        self.update_min_max_x_y()
        self.y = abs(self.min_y)-1

    def is_end(self, board):
        for i in self.offsets[self.rot_index]:
            currx = self.x+i[0]
            curry = self.y+i[1]
            if curry >= B_HEIGHT-self.max_y-1:
                self.y += 1
                return True
            elif board[curry+1][currx] != BG:
                self.y += 1
                return True

    def update_board(self, board):
        if self.x < self.min_x+1:
            self.x = self.min_x
        if self.x > B_WIDTH-self.max_x-1:
            self.x = B_WIDTH-self.max_x-1
        for i in self.offsets[self.rot_index]:
            board[self.y+i[1]][self.x+i[0]] = self.type

    def update_min_max_x_y(self):
        self.min_x = 10
        self.max_x = -10
        for i in self.offsets[self.rot_index]:
            self.min_x = min(self.min_x, i[0])
            self.max_x = max(self.max_x, i[0])
        self.min_x = abs(self.min_x)
        self.max_x = abs(self.max_x)

        self.min_y = 10
        self.max_y = -10
        for i in self.offsets[self.rot_index]:
            self.min_y = min(self.min_y, i[1])
            self.max_y = max(self.max_y, i[1])
        self.min_y = abs(self.min_y)
        self.max_y = abs(self.max_y)

    def clear_self(self, board):
        for i in self.offsets[self.rot_index]:
            board[self.y+i[1]][self.x+i[0]] = BG

    def rotate(self, dir, board):
        if dir == "left":
            self.clear_self(board)
            self.rot_index -= 1
        if dir == "right":
            self.clear_self(board)
            self.rot_index += 1

        self.rot_index %= len(self.offsets)
        self.update_min_max_x_y()

    def move(self, dir, board):
        if dir == "left" and self.x > self.min_x:
            self.clear_self(board)
            for i in self.offsets[self.rot_index]:
                if board[self.y+i[1]][self.x+i[0]-1] != BG:
                    return
            self.x -= 1

        if dir == "right" and self.x < B_WIDTH-self.max_x-1:
            self.clear_self(board)
            for i in self.offsets[self.rot_index]:
                if board[self.y+i[1]][self.x+i[0]+1] != BG:
                    return
            self.x += 1

        if dir == "drop":
            self.clear_self(board)
            for i in range(B_HEIGHT):
                if self.is_end(board):
                    self.y -= 1
                    return
                self.y += 1