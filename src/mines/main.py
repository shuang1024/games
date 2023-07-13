import time

import pygame

from constants import *
from board import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


def rc_mousepos(mousepos):
    return ((mousepos[1]-MARGIN)//(SQ_SIZE + MARGIN), (mousepos[0]-MARGIN)//(SQ_SIZE + MARGIN))

def main():
    board = Board()
    fclick = False

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
                    if fclick == False:
                        start = time.time()
                    fclick = True
                    board.click(*rc_mousepos(mousepos))
                elif event.button == 3:
                    board.flag(*rc_mousepos(mousepos))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    return

        display.fill(BG)
        board.draw(display)
        board.check_win()

        try:
            mins = int((time.time()-start)/60)
            secs = int((time.time()-start)%60)
        except:
            pass

        while board.stat == True:
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main()
                        return

            if mins != 0:
                print("Your time: " + str(int(mins)) + "minutes and " + str(secs) + " seconds.")
            else:
                print("Your time: " + str(secs) + " seconds.")
            text = STDFONT.render("You win!", True, BLACK)
            text1 = STDFONT.render("Click or press the spacebar to play again!", True, BLACK)
            display.blit(text, (WIDTH//2-text.get_width()//2, HEIGHT//2-text.get_height()//2))
            display.blit(text1, (WIDTH//2-text1.get_width()//2, HEIGHT//2+text1.get_height()//2))

        while board.stat == False:
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main()
                        return
            text = STDFONT.render("You lost.", True, BLACK)
            text1 = STDFONT.render("Click or press the spacebar to play again!", True, BLACK)
            display.blit(text, (WIDTH//2-text.get_width()//2, HEIGHT//2-text.get_height()//2))
            display.blit(text1, (WIDTH//2-text1.get_width()//2, HEIGHT//2+text1.get_height()//2))



main()
