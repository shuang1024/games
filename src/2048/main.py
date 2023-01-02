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
        keys = pygame.key.get_pressed()
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


main()