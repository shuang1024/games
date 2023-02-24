import pygame

from constants import *
from player import Player

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")


# def draw_map(display, map):
#     for i in map:
#         pygame.draw.rect(display, BLACK, (i[0]-5, i[1]-5, i[2]+10, i[3]+10), 0, 5)
#         pygame.draw.rect(display, TAN, i)


def main():
    player = Player()

    clock = pygame.time.Clock()
    #map = [[150, 150, 100, 300], [WIDTH-450, HEIGHT-250, 300, 100]]

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        display.fill(WHITE)
        #draw_map(display)
        player.draw(display)
        player.move(keys)


main()
