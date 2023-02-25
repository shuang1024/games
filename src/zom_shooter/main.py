import time, random

import pygame

from constants import *
from player import Player
from zombie import Zombie
from zombie_boss import Zombie_Boss

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")


def main():
    player = Player()

    zombies = [Zombie(50, 50)]
    start = time.time()
    last_zombie = time.time()
    last_boss = time.time()
    max_zombies = 12
    pos = [(50, 50), (WIDTH-65, 50), (50, HEIGHT-65), (WIDTH-65, HEIGHT-65)]

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

        display.fill(BG)
        player.draw(display)
        player.move(keys)
        player.shoot(mouse, display)
        for z in zombies:
            player.check_damage(z)
            z.draw(display)
            z.move(player)
            if z.health == 0:
                zombies.remove(z)

        if time.time() - last_zombie >= 1.5 and len(zombies) <= max_zombies:
            last_zombie = time.time()
            zombies.append(Zombie(*random.choice(pos)))
        if time.time() - start > 20:
            if time.time() - last_boss >= 5 and len(zombies) <= max_zombies:
                last_boss = time.time()
                zombies.append(Zombie_Boss(*random.choice(pos)))

        print(player.health)


main()
