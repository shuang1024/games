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

    last_draw = time.time()
    with open("highscore.txt", "r") as fp:
        snake.highsore = int(fp.read())
    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                with open("highscore.txt", "w") as fp:
                    fp.write(str(snake.highscore))
                return

        display.fill(BORDER)
        for i in range(ROWS):
            for j in range(COLS):
                if (j + i) % 2 == 0:
                    pygame.draw.rect(display, LIGHT_GREEN, (MARGIN + i*SQ_SIZE, MARGIN + j*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    pygame.draw.rect(display, DARK_GREEN, (MARGIN + i*SQ_SIZE, MARGIN + j*SQ_SIZE, SQ_SIZE, SQ_SIZE))

        if time.time() - last_draw > 1 / SNAKE_FPS:
            snake.update(apple)
            last_draw = time.time()
        snake.draw(display)
        snake.keys(keys)
        if snake.check_lose():
            with open("highscore.txt", "w") as fp:
                fp.write(str(snake.highscore))
            snake.reset()
        apple.draw(display)

        score_text = SCORE_FONT.render(f"Score: {snake.score}", True, BLACK)
        display.blit(score_text, (10, WIDTH - MARGIN + 10))
        highscore_text = SCORE_FONT.render(f"Highscore: {snake.highscore}", True, BLACK)
        display.blit(highscore_text, (10, WIDTH - MARGIN + 10 + score_text.get_height()))

main()
