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

    def __init__(self, stars_count=200, clouds_count=20, darkness_offset=0):
        """Soccer pygame constructor.
        Optional Argument stars_count and clouds_count
        for number of objects on screen
        darkness offset changes how dark dark is, positive will make it darker,
        negative will make it lighter
        """
        # config
        pygame.display.set_caption(self.TITLE)

        alpha = 200 + darkness_offset
        if alpha > 255:
            alpha = 255
        elif alpha < 0:
            alpha = 0
        self.DARKNESS.set_alpha(alpha)
        self.DARKNESS.fill((0, 0, 0))

        self.SEE_THROUGH.set_alpha(150)
        self.SEE_THROUGH.fill((124, 118, 135))

        # stars and cloud random placement
        self.STARS_COUNT = stars_count
        self.CLOUDS_COUNT = clouds_count
        for _ in range(self.STARS_COUNT):
            x = random.randrange(0, 800)
            y = random.randrange(0, 200)
            r = random.randrange(1, 2)
            self.stars.append([x, y, r, r])


        for _ in range(self.CLOUDS_COUNT):
            x = random.randrange(-100, 1600)
            y = random.randrange(0, 150)
            self.clouds.append([x, y])
    
    def event_handler(self, event) -> None:
        """handle event when pass in."""
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                self.lights_on = not self.lights_on
            elif event.key == pygame.K_d:
                self.day = not self.day

    def run(self) -> None:
        """run starts the game, go through the game loop and exit"""
        while not self.done:
            # Event processing (React to key presses, mouse clicks, etc.)
            for event in pygame.event.get():
                self.event_handler(event)

            # Game logic (Check for collisions, update points, etc.)
            if self.lights_on:
                light_color = YELLOW
            else:
                light_color = SILVER

            if self.day:
                sky_color = BLUE
                field_color = GREEN
                stripe_color = DAY_GREEN
                cloud_color = WHITE
            else:
                sky_color = DARK_BLUE
                field_color = DARK_GREEN
                stripe_color = NIGHT_GREEN
                cloud_color = NIGHT_GRAY

            for cloud in self.clouds:
                cloud[0] -= 0.5
                if cloud[0] < -100:
                    cloud[0] = random.randrange(800, 1600)
                    cloud[1] = random.randrange(0, 150)
                    
            # Drawing code (Describe the picture. It isn't actually drawn yet.)
            self.screen.fill(sky_color)
            self.SEE_THROUGH.fill(ck)
            self.SEE_THROUGH.set_colorkey(ck)
            
            # stars
            if not self.day:
                for star in self.stars:
                    pygame.draw.ellipse(self.screen, WHITE, star)

            self.draw_fields(self.screen, field_color, stripe_color)
            self.draw_fence(self.screen)
            self.draw_sun_moon(self.screen, sky_color, x_offset=-10, size_offset=5)
            self.draw_clouds(self.screen) 
            self.draw_field_lines(self.screen)
            self.draw_scoreboard(self.screen)
            self.draw_light_pole(self.screen, light_color, pole1_x_offset=40, pole2_x_offset=-40)
            self.draw_goal(self.screen)
            self.draw_stands(self.screen)
            self.draw_corner_flag(self.screen)

            # DARKNESS
            if not self.day and not self.lights_on:
                self.screen.blit(self.DARKNESS, (0, 0))    

            # Update screen (Actually draw the picture in the window.)
            pygame.display.flip()

            # Limit refresh rate of game loop 
            self.clock.tick(self.refresh_rate)

        # Close window and quit
        pygame.quit()
