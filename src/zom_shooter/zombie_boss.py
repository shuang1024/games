from zombie import Zombie
from constants import *

class Zombie_Boss(Zombie):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 30
        self.speed = 2
        self.normal_color = BOSS
        self.health = 15
        self.damage = 2