import pygame

from constants import *
from board import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


def rc_mousepos(mousepos):
    return ((mousepos[1]-MARGIN)//(SQ_SIZE + MARGIN), (mousepos[0]-MARGIN)//(SQ_SIZE + MARGIN))

def main():
    board = Board()

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.click(*rc_mousepos(mousepos))
            
        display.fill(BG)
        board.draw(display)


main()
