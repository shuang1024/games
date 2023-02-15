import time

import pygame

from constants import *
from snake import Snake
from apple import Apple

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def main():
    clock = pygame.time.Clock()

    snake = Snake()
    snake.draw(display)
    apple = Apple(snake)
    
    score = 0

    last_draw = time.time()
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

        if time.time() - last_draw > 1 / SNAKE_FPS:
            snake.move()
            last_draw = time.time()
        snake.draw(display)
        snake.keys(keys)
        snake.check_lose()
        apple.draw(display)

        if (apple.x, apple.y) == snake.positions[0]:
            score += 1
            snake.length += 1
            apple.random_pos(snake)

main()
