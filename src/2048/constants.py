import pygame
pygame.init()

ROWS, COLS = 4, 4
PADDING = 10
SQ_SIZE = 100
WIDTH, HEIGHT = SQ_SIZE*COLS + PADDING*(COLS+1), SQ_SIZE*ROWS + PADDING*(ROWS+1) + 100
FPS = 60

WHITE = (240, 225, 200)
DARK_BROWN = (163, 148, 137)
LIGHT_BROWN = (194, 179, 169)
BLOCK_COLORS = [
    (252, 239, 230), #2
    (242, 232, 203), #4
    (245, 182, 130), #8
    (242, 147, 70), #16
    (255, 119, 92), #32
    (230, 77, 46), #64
    (237, 226, 145), #128
    (252, 225, 48), #256
    (255, 219, 74), #512
    (240, 185, 34), #1024
    (250, 215, 77), #2048
]

NUMBER_FONTS = [
    pygame.font.SysFont("helvetica", 55, True),
    pygame.font.SysFont("helvetica", 55, True),
    pygame.font.SysFont("helvetica", 55, True),
    pygame.font.SysFont("helvetica", 50, True),
    pygame.font.SysFont("helvetica", 50, True),
    pygame.font.SysFont("helvetica", 50, True),
    pygame.font.SysFont("helvetica", 45, True),
    pygame.font.SysFont("helvetica", 45, True),
    pygame.font.SysFont("helvetica", 45, True),
    pygame.font.SysFont("helvetica", 40, True),
    pygame.font.SysFont("helvetica", 40, True),
]

LIGHT_TEXT = (255, 255, 255)
DARK_TEXT = (105, 92, 87)
LOSE_TEXT = pygame.font.SysFont("helvetica", 40, True)
SCORE_TEXT = pygame.font.SysFont("helvetica", 30, True)