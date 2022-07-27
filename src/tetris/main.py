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


def remove_rows(board):
    indexes = []
    for i in range(B_HEIGHT):
        clear = False
        for j in range(B_WIDTH):
            if board[j][i] == BG:
                clear = False
                break
            else:
                clear = True
        if clear:
            indexes.append(i)

    for i in indexes:
        print(i)
        print(len(board))
        board.pop(i)
        board.insert(0, [])
        for _ in range(B_WIDTH):
            board[0].append(BG)

    return board


def main():
    clock = pygame.time.Clock()
    pause = 0.75
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
    down = False

    while True:
        board_copy = deepcopy(board)
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and curr_block:
                if event.key == pygame.K_LEFT:
                    curr_block.move("left", board_copy)
                if event.key == pygame.K_RIGHT:
                    curr_block.move("right", board_copy)
                if event.key == pygame.K_DOWN:
                    down = True
                    pause = 0.1
                if event.key == pygame.K_a:
                    curr_block.rotate("left", board_copy)
                if event.key == pygame.K_d:
                    curr_block.rotate("right", board_copy)

                if curr_block:
                    curr_block.update_board(board_copy)
                    draw(display, board_copy)
            if event.type == pygame.KEYUP and down:
                pause = 0.75
                down = False

        if curr_block:
            curr_block.clear_self(board_copy)

        board = remove_rows(board)
        if time.time() - start > pause:
            if not curr_block:
                index = random.randint(0, min(len(BLOCK_COLORS), len(BLOCK_OFFSETS))-1)
                curr_block = Block(BLOCK_COLORS[index], BLOCK_OFFSETS[index])
            
            curr_block.y += 1
            display.fill(BORDER)
            start = time.time()

            curr_block.update_board(board_copy)
            draw(display, board_copy)

            if curr_block.is_end(board):
                curr_block = None
                board = board_copy



main()
