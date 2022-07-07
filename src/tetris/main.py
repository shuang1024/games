from lib2to3.pgen2.token import VBAR
import time
import random
from copy import deepcopy

import pygame

from constants import *
from block import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


def draw(display, board):
    for i in range(B_WIDTH):
        for j in range(B_HEIGHT):
            pygame.draw.rect(display, board[i][j], (BORD_SIZE+SQ_SIZE*i, BORD_SIZE+SQ_SIZE*j, SQ_SIZE, SQ_SIZE))


def main():
    clock = pygame.time.Clock()
    board = []
    for i in range(B_WIDTH):
        board.append([])
        for _ in range(B_HEIGHT):
            board[i].append(BG)
    board_copy = deepcopy(board)

    curr_block = None
    start = time.time()
    display.fill(BORDER)
    draw(display, board_copy)

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and curr_block:
                if event.key == pygame.K_LEFT:
                    curr_block.move("left", board)
                if event.key == pygame.K_RIGHT:
                    curr_block.move("right", board)
                if event.key == pygame.K_DOWN:
                    curr_block.move("down", board)
                    curr_block.update_board(board)
                    board_copy = board
                    curr_block = None

        if time.time() - start > PAUSE:
            if not curr_block:
                curr_block = Block(BOX, BOX_OFFSETS)
            
            curr_block.y += 1
            display.fill(BORDER)
            start = time.time()

            board_copy = deepcopy(board)
            curr_block.update_board(board_copy)
            draw(display, board_copy)

            if curr_block.is_end(board):
                board = board_copy
                curr_block = None


main()
