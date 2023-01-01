import random

import pygame
pygame.init()

from constants import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        display.fill(WHITE)
        pygame.draw.rect(display, DARK_BROWN, (0, 0, WIDTH, HEIGHT-100))
        for r in range(4):
            for c in range(4):
                pygame.draw.rect(display, LIGHT_BROWN, (c*(SQ_SIZE + PADDING) + PADDING, r*(SQ_SIZE + PADDING) + PADDING, SQ_SIZE, SQ_SIZE), 0, 5)


main()