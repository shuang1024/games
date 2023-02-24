import pygame

from constants import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")


def draw_map(display):
    pygame.draw.rect(display, BLACK, (140, 140, 170, 320), 0, 5)
    pygame.draw.rect(display, TAN, (150, 150, 150, 300))


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
        draw_map(display)


main()
