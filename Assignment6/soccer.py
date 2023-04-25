import pygame
import math
import random
from random import randint

# color constant init (R, G, B)
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

# Initialize game engine
pygame.init()

class Soccer():
    # Window
    SIZE = (800, 600)
    TITLE = "Major League Soccer"
    screen = pygame.display.set_mode(SIZE)

    # Timer
    clock = pygame.time.Clock()
    refresh_rate = 60

    # Surface for night and no light
    DARKNESS = pygame.Surface(SIZE)
    SEE_THROUGH = pygame.Surface((800, 180))

    # config
    lights_on: bool = True
    day: bool = True

    STARS_COUNT: int = 200
    CLOUDS_COUNT: int = 20
    stars: list[list[int]] = []
    clouds: list[list[int]] = []

    # Game loop
    done: bool = False
    