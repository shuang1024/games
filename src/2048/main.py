import random

import pygame
pygame.init()

from constants import *
from board import Board

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def main():
    clock = pygame.time.Clock()
    board = Board()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        mouse = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT: board.move("r")
                    case pygame.K_LEFT: board.move("l")
                    case pygame.K_UP: board.move("u")
                    case pygame.K_DOWN: board.move("d")

        display.fill(WHITE)
        board.draw(display)
        if board.detect_lose():
            display.fill((DARK_BROWN))
            lose1 = LOSE_TEXT.render("You lost!", True, LIGHT_TEXT)
            lose2 = LOSE_TEXT.render("Click to play again.", True, LIGHT_TEXT)
            display.blit(lose1, (WIDTH//2 - lose1.get_width()//2, HEIGHT//2 - lose1.get_height()))
            display.blit(lose2, (WIDTH//2 - lose2.get_width()//2, HEIGHT//2))
            if mouse[0] or mouse[1] or mouse[2]:
                main()
                return


main()