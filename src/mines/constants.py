import pygame
pygame.init()

SQ_SIZE = 113
MARGIN = 3
ROWS = 8
COLS = 8
MINES = 10

WIDTH = COLS * SQ_SIZE + (COLS + 1) * MARGIN
HEIGHT = ROWS * SQ_SIZE + (ROWS + 1) * MARGIN
FPS = 60

BLACK = (46, 52, 54)
BG = (62, 62, 62)
ZERO = (222, 222, 220)
ONE = (221, 250, 195)
TWO = (236, 237, 191)
THREE = (237, 218, 180)
FOUR = (237, 195, 138)
FIVE = (247, 161, 162)
SIX = (254, 167, 133)
SEVEN = (255, 125, 96)
EIGHT = (255, 50, 60)
MINE = (200, 0, 0)
UNACTIVE = (185, 187, 181)

COLORS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, MINE, UNACTIVE]

CELLFONT = pygame.font.SysFont("helvetica", 80, True)
STDFONT = pygame.font.SysFont("helvetica", 40, True)
