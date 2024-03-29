import pygame
pygame.init()

SQ_SIZE = 20
BORD_SIZE = 20
B_WIDTH = 10
B_HEIGHT = 20
WIDTH = B_WIDTH*SQ_SIZE + 2*BORD_SIZE+SQ_SIZE*9
HEIGHT = B_HEIGHT*SQ_SIZE + 2*BORD_SIZE

FONT = pygame.font.SysFont(None, 30)

FPS = 60

BG = (0, 0, 0)
Z = (255, 0, 0)
S = (0, 255, 0)
REV_L = (0, 0, 255)
BOX = (255, 255, 0)
T = (255, 0, 255)
LONG = (0, 255, 255)
L = (255, 128, 0)
BORDER = (128, 128, 128)
WHITE = (255, 255, 255)

Z_OFFSETS = [[(0, 0), (0, -1), (-1, -1), (1, 0)], [(0, 0), (1, 0), (1, -1), (0, 1)]]
S_OFFSETS = [[(0, 0), (0, -1), (1, -1), (-1, 0)], [(0, 0), (-1, 0), (-1, -1), (0, 1)]]
REV_L_OFFSETS = [[(0, 0), (-1, -1), (-1, 0), (1, 0)], [(0, 0), (0, -1), (1, -1), (0, 1)], [(0, 0), (-1, 0), (1, 0), (1, 1)], [(0, 0), (0, -1), (0, 1), (-1, 1)]]
BOX_OFFSETS = [[(0, 0), (0, 1), (1, 1), (1, 0)]]
T_OFFSETS = [[(0, 0), (-1, 0), (1, 0), (0, -1)], [(0, 0), (0, -1), (0, 1), (1, 0)], [(0, 0), (1, 0), (-1, 0), (0, 1)], [(0, 0), (0, -1), (0, 1), (-1, 0)]]
LONG_OFFSETS = [[(-2, 0), (-1, 0), (0, 0), (1, 0)], [(0, -1), (0, 0), (0, 1), (0, 2)]]
L_OFFSETS = [[(0, 0), (-1, 0), (1, 0), (1, -1)], [(0, 0), (0, -1), (0, 1), (1, 1)], [(0, 0), (1, 0), (-1, 0), (-1, 1)], [(0, 0), (0, -1), (-1, -1), (0, 1)]]

BLOCK_COLORS = [Z, S, REV_L, BOX, T, LONG, L]
BLOCK_OFFSETS = [Z_OFFSETS, S_OFFSETS, REV_L_OFFSETS, BOX_OFFSETS, T_OFFSETS, LONG_OFFSETS, L_OFFSETS]
