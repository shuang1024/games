import time

import pygame

from constants import *
from player import Player

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")


def main():
    player = Player()

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        display.fill(WHITE)
        player.draw(display)
        player.move(keys)
        player.shoot(mouse, display)


main()
