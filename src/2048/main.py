import pygame
pygame.init()

from constants import *
from board import Board

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
pygame.display.set_icon(pygame.image.load("icon.png"))


def main():
    clock = pygame.time.Clock()
    board = Board()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    board.move("r", False)
                if event.key == pygame.K_LEFT:
                    board.move("l", False)
                if event.key == pygame.K_UP:
                    board.move("u", False)
                if event.key == pygame.K_DOWN:
                    board.move("d", False)

        display.fill(WHITE)
        board.draw(display)

        while board.detect_lose():
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
                    return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            lose1 = LOSE_TEXT.render("You lost!", True, (0, 0, 0))
            lose2 = LOSE_TEXT.render("Click to play again.", True, (0, 0, 0))
            display.blit(lose1, (WIDTH//2 - lose1.get_width()//2, HEIGHT//2 - lose1.get_height()))
            display.blit(lose2, (WIDTH//2 - lose2.get_width()//2, HEIGHT//2))
            pygame.display.update()
            
            with open("highscore.txt", "w") as fp:
                fp.write(str(board.highscore))


main()
