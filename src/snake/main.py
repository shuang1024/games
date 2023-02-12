import time

import pygame

from constants import *
from snake import Snake

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def main():
    clock = pygame.time.Clock()

    snake = Snake()
    snake.draw(display)
    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        display.fill(BORDER)
        for i in range(ROWS):
            for j in range(COLS):
                if (j + i) % 2 == 0:
                    pygame.draw.rect(display, LIGHT_GREEN, (MARGIN + i*SQ_SIZE, MARGIN + j*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    pygame.draw.rect(display, DARK_GREEN, (MARGIN + i*SQ_SIZE, MARGIN + j*SQ_SIZE, SQ_SIZE, SQ_SIZE))

        snake.draw(display)
        snake.move(keys)


main()
