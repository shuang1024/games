import time, random

import pygame

from constants import *
from player import Player
from zombie import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")


def draw_weapons(display, curr_weapon_ind):
    for i in range(len(WEAPONS)):
        if i == curr_weapon_ind:
            pygame.draw.rect(display, BLACK, (100 + 50*i, HEIGHT-50, 50, 50), 5)
            display.blit(WEAPONS[i], (100 + 50*i, HEIGHT-50))
        else:
            pygame.draw.rect(display, WHITE, (100 + 50*i, HEIGHT-50, 50, 50), 5)
            display.blit(WEAPONS[i], (100 + 50*i, HEIGHT-50))


def main():
    player = Player()
    zombies = [Zombie(50, 50)]
    start = time.time()
    last_zombie = time.time()
    last_boss = time.time()
    last_fast = time.time()
    last_fire = time.time()
    last_explode = time.time()
    max_zombies = 15
    pos = [(50, 50), (WIDTH-65, 50), (50, HEIGHT-65), (WIDTH-65, HEIGHT-65)]
    curr_weapon_ind = 0

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    curr_weapon_ind = 0
                    player.weapon = "pistol"
                if event.key == pygame.K_2:
                    curr_weapon_ind = 1
                    player.weapon = "shotgun"
                if event.key == pygame.K_3:
                    curr_weapon_ind = 2
                    player.weapon = "assault rifle"
                if event.key == pygame.K_4:
                    curr_weapon_ind = 3
                    player.weapon = "360deg"

        display.fill(BG)
        draw_weapons(display, curr_weapon_ind)
        player.draw(display)
        player.move(keys)
        player.shoot(mouse, display)
        for z in zombies:
            player.check_damage(z)
            z.draw(display)
            z.move(player)
            if z.health <= 0:
                player.score += z.damage
                zombies.remove(z)

            if z.type == "fire":
                z.shoot(player, display)

        if time.time() - last_zombie >= 1.5 and len(zombies) <= max_zombies:
            last_zombie = time.time()
            zombies.append(Zombie(*random.choice(pos)))
            
        if time.time() - start > 20 and time.time():
            if time.time() - last_boss >= 5 and len(zombies) <= max_zombies:
                last_boss = time.time()
                zombies.append(Zombie_Boss(*random.choice(pos)))
            
        if time.time() - start > 40:
            if time.time() - last_fast >= 3 and len(zombies) <= max_zombies:
                last_fast = time.time()
                zombies.append(Fast_Zombie(*random.choice(pos)))
            
        if time.time() - start > 60:
            if time.time() - last_fire >= 5 and len(zombies) <= max_zombies:
                last_fire = time.time()
                zombies.append(Fire_Zombie(*random.choice(pos)))
            
        if time.time() - start > 80:
            if time.time() - last_explode >= 5 and len(zombies) <= max_zombies:
                last_explode = time.time()
                zombies.append(Explode_Zombie(*random.choice(pos)))

        while player.health <= 0:
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
                    return
            lose_font = STDFONT.render("You died!", True, BLACK)
            lose_font2 = STDFONT.render("Click to play again.", True, BLACK)
            display.blit(lose_font, (WIDTH//2 - lose_font.get_width()//2, HEIGHT//2 - lose_font.get_height()//2 - 40))
            display.blit(lose_font2, (WIDTH//2 - lose_font2.get_width()//2, HEIGHT//2 - lose_font2.get_height()//2 + 40))


main()
