import time
import random
from copy import deepcopy

import pygame
pygame.init()

from constants import *
from block import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


def draw(display, board, score, next, hold):
    for i in range(B_WIDTH):
        for j in range(B_HEIGHT):
            pygame.draw.rect(display, board[j][i], (BORD_SIZE+SQ_SIZE*i, BORD_SIZE+SQ_SIZE*j, SQ_SIZE, SQ_SIZE))

    score_text = FONT.render(f"{score}", True, WHITE)
    display.blit(FONT.render("Score:", True, WHITE), (SQ_SIZE*12, SQ_SIZE*2))
    pygame.draw.rect(display, BG, (SQ_SIZE*12, SQ_SIZE*3, SQ_SIZE*8, SQ_SIZE*4))
    display.blit(score_text, (SQ_SIZE*16-score_text.get_width()//2, SQ_SIZE*4.5))

    display.blit(FONT.render("Hold:", True, WHITE), (SQ_SIZE*12, SQ_SIZE*8))
    pygame.draw.rect(display, BG, (SQ_SIZE*12, SQ_SIZE*9, SQ_SIZE*8, SQ_SIZE*4))
    if hold:
        hold_display = deepcopy(hold)
        hold_display.rot_index = 0
        if hold_display.type == LONG:
            hold_display.x = SQ_SIZE*16
            hold_display.y = SQ_SIZE*10.5
        elif hold_display.type == BOX:
            hold_display.x = SQ_SIZE*15
            hold_display.y = SQ_SIZE*10
        else:
            hold_display.x = SQ_SIZE*15.5
            hold_display.y = SQ_SIZE*11
        hold_display.update_next(display)

    display.blit(FONT.render("Next:", True, WHITE), (SQ_SIZE*12, SQ_SIZE*14))
    pygame.draw.rect(display, BG, (SQ_SIZE*12, SQ_SIZE*15, SQ_SIZE*8, SQ_SIZE*4))
    next_display = deepcopy(next)
    if next_display.type == LONG:
        next_display.x = SQ_SIZE*16
        next_display.y = SQ_SIZE*16.5
    elif next_display.type == BOX:
        next_display.x = SQ_SIZE*15
        next_display.y = SQ_SIZE*16
    else:
        next_display.x = SQ_SIZE*15.5
        next_display.y = SQ_SIZE*17
    next_display.update_next(display)


def remove_rows(board, score):
    indexes = []
    for i in range(B_HEIGHT):
        clear = False
        for j in range(B_WIDTH):
            if board[i][j] == BG:
                clear = False
                break
            else:
                clear = True
        if clear:
            indexes.append(i)

    for i in indexes:
        score += 10
        board.pop(i)
        board.insert(0, [])
        for _ in range(B_WIDTH):
            board[0].append(BG)

    return board, score


def main():
    clock = pygame.time.Clock()
    pause = 0.75
    board = []
    for i in range(B_HEIGHT):
        board.append([])
        for _ in range(B_WIDTH):
            board[i].append(BG)
    board_copy = deepcopy(board)

    curr_block = None
    index = random.randint(0, min(len(BLOCK_COLORS), len(BLOCK_OFFSETS))-1)
    next = Block(BLOCK_COLORS[index], BLOCK_OFFSETS[index])
    start = time.time()
    display.fill(BORDER)
    down = False
    score = 0
    hold = None
    draw(display, board_copy, score, next, hold)

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
                if event.key in (pygame.K_DOWN, pygame.K_SPACE):
                    curr_block.move("drop", board_copy)
                    board = board_copy
                    curr_block.update_board(board)
                    draw(display, board, score, next, hold)
                    curr_block = None
                    score += 5

                if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                    if hold:
                        a = curr_block
                        curr_block = hold
                        hold = a
                    else:
                        hold = curr_block
                        curr_block = None
                    if hold.type == LONG:
                        hold.x = B_WIDTH//2+1
                    else:
                        hold.x = B_WIDTH//2-1
                    hold.update_min_max_x_y()
                    hold.y = hold.min_y

                if event.key == pygame.K_a:
                    curr_block.rotate("left", board_copy)
                if event.key == pygame.K_d:
                    curr_block.rotate("right", board_copy)
                if event.key == pygame.K_s:
                    curr_block
                    down = True
                    pause = 0.1

                if curr_block:
                    curr_block.update_board(board_copy)
                    draw(display, board_copy, score, next, hold)
            if event.type == pygame.KEYUP and down:
                pause = 0.75
                down = False

        board, score = remove_rows(board, score)
        if time.time() - start > pause:
            if not curr_block:
                curr_block = next
                index = random.randint(0, min(len(BLOCK_COLORS), len(BLOCK_OFFSETS))-1)
                next = Block(BLOCK_COLORS[index], BLOCK_OFFSETS[index])
            
            curr_block.y += 1
            display.fill(BORDER)
            start = time.time()

            curr_block.update_board(board_copy)
            draw(display, board_copy, score, next, hold)

            if curr_block.is_end(board):
                curr_block = None
                board = board_copy
                score += 5


main()
