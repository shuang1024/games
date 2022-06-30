import time
import random
from copy import deepcopy

import pygame

from constants import *
from block import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

type_col = {0:RED, 1:GREEN, 2:BLUE, 3:YELLOW, 4:MAGENTA, 5:CYAN, 6:ORANGE, 7:BLACK}

def draw(display, board):
    for i in range(B_WIDTH):
        for j in range(B_HEIGHT):
            pygame.draw.rect(display, type_col[board[i][j]], (BORD_SIZE+SQ_SIZE*i, BORD_SIZE+SQ_SIZE*j, SQ_SIZE, SQ_SIZE))


def main():
    clock = pygame.time.Clock()
    board = []
    for i in range(B_WIDTH):
        board.append([])
        for j in range(B_HEIGHT):
            board[i].append(7)

    curr_block = None
    start = time.time()
    display.fill(GRAY)
    draw(display, board)

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


        if time.time() - start > PAUSE:
            if not curr_block:
                curr_block = Block(random.randint(0, 6))
            elif curr_block.y == B_HEIGHT-1 or board[curr_block.x][curr_block.y+1] != 7:
                    curr_block = None
                    continue

            curr_block.y += 1
            curr_block.update_board(board)
            start = time.time()
            display.fill(GRAY)
            draw(display, board)


main()