import pygame

SQ_SIZE = 20
BORD_SIZE = 15
B_WIDTH = 10
B_HEIGHT = 20
WIDTH = B_WIDTH*SQ_SIZE + 2*BORD_SIZE
HEIGHT = B_HEIGHT*SQ_SIZE + 2*BORD_SIZE

FPS = 60
PAUSE = 1

BLACK = (0, 0, 0) # BG
RED = (255, 0, 0) # L
GREEN = (0, 255, 0) # Box
BLUE = (0, 0, 255) # Z
YELLOW = (255, 255, 0) # Long
MAGENTA = (255, 0, 255) # T
CYAN = (0, 255, 255) # S
ORANGE = (255, 128, 0) # Reversed L
GRAY = (128, 128, 128) # Border

L = 0
BOX = 1
Z = 2
LONG = 3
T = 4
S = 5
REV_L = 6