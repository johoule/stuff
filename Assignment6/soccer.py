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
        """
        Soccer pygame constructor.
        Optional Argument stars_count and clouds_count for number of objects on screen
        darkness offset changes how dark dark is, positive will make it darker, while negative will make it lighter
        :self, stars_count, clouds_count, darkness_offset
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
        """
        Handle event when passed in.
        :self, event
        """
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                self.lights_on = not self.lights_on
            elif event.key == pygame.K_d:
                self.day = not self.day

    def run(self) -> None:
        """
        Run function starts the game, goes through the game loop and exits.
        :self
        """
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


    def draw_clouds(self, screen) -> None:
        """
        Draw clouds from the list: clouds
        :self, screen
        """
        for cloud in self.clouds:
            self.draw_cloud(cloud[0], cloud[1])
        screen.blit(self.SEE_THROUGH, (0, 0))

    def draw_cloud(self, x, y, cloud_color=None) -> None:
        """
        Draw an individual cloud
        x, y is the position and an optional argument for cloud color
        Default is white
        :self, x, y, cloud_color
        """
        if cloud_color is None:
            cloud_color = WHITE
        
        # animate cloud jiggle
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x+randint(0,1), y+8+randint(0,1), 10+randint(-1,1), 10],)
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x+6+randint(0,1), y+4+randint(0,1), 8+randint(-1,1), 8])
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x+10+randint(0,1), y+randint(0,1), 16+randint(-1,1), 16])
        pygame.draw.ellipse(self.SEE_THROUGH, cloud_color, [x+20+randint(0,1), y+8+randint(0,1), 10+randint(-1,1), 10])
        pygame.draw.rect(self.SEE_THROUGH, cloud_color, [x+6, y+8, 18, 10])
    
    def draw_fence(self, screen, fence_color=None) -> None:
        """
        Draw fence on screen with optional argument fence_color
        Default is night gray
        :self, screen, fence_color
        """
        if fence_color is None:
            fence_color = NIGHT_GRAY

        y = 170
        for x in range(5, 800, 30):
            pygame.draw.polygon(screen, fence_color, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

        y = 170
        for x in range(5, 800, 3):
            pygame.draw.line(screen, fence_color, [x, y], [x, y + 15], 1)

        x = 0
        for y in range(170, 185, 4):
            pygame.draw.line(screen, fence_color, [x, y], [x + 800, y], 1)
    
    def draw_fields(self, screen, field_color, stripe_color) -> None:
        """
        Draw the fields with passed in arguments field_color and stripe_color
        :self, scren, field_color, stripe_color
        """
        pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
        pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
        pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
        pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
        pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    def draw_sun_moon(self, screen, sky_color, sun_color=None, moon_color=None,
                      x_offset=0, y_offset=0, size_offset=0) -> None:
        """
        Draw sun or moon depending if it is day.
        optional arguments sun_color and moon_color can be passed in
        default is bright yellow for sun, white for moon
        x_offset, y_offset offset position of sun and moon
        size_offset offset the size of sun and moon
        :self, screen, sky_color, sun_color, moon_color, x_offset, y_offset, size_offset
        """
        if sun_color is None:
            sun_color = BRIGHT_YELLOW
        if moon_color is None:
            moon_color = WHITE
        if self.day:
            pygame.draw.ellipse(screen, sun_color, [520 + x_offset, 50 + y_offset, 40 + size_offset, 40 + size_offset])
        else:
            pygame.draw.ellipse(screen, moon_color, [520 + x_offset, 50 + y_offset, 40 + size_offset, 40 + size_offset]) 
            pygame.draw.ellipse(screen, sky_color, [530 + x_offset, 45 + y_offset, 40 + size_offset, 40 + size_offset])

    def draw_field_lines(self, screen, line_color=None) -> None:
        """
        Draw field lines with an optional argument for line color
        default is white
        :self, screen, line_color
        """
        if line_color is None:
            line_color = WHITE

        # out of bounds lines
        pygame.draw.line(screen, line_color, [0, 580], [800, 580], 5)
        
        # left
        pygame.draw.line(screen, line_color, [0, 360], [140, 220], 5)
        pygame.draw.line(screen, line_color, [140, 220], [660, 220], 3)
        
        # right
        pygame.draw.line(screen, line_color, [660, 220], [800, 360], 5)

        # safety circle
        pygame.draw.ellipse(screen, line_color, [240, 500, 320, 160], 5)

        # 18 yard line goal box
        pygame.draw.line(screen, line_color, [260, 220], [180, 300], 5)
        pygame.draw.line(screen, line_color, [180, 300], [620, 300], 3)
        pygame.draw.line(screen, line_color, [620, 300], [540, 220], 5)

        #arc at the top of the goal box
        pygame.draw.arc(screen, line_color, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

        # 6 yard line goal box
        pygame.draw.line(screen, line_color, [310, 220], [270, 270], 3)
        pygame.draw.line(screen, line_color, [270, 270], [530, 270], 2)
        pygame.draw.line(screen, line_color, [530, 270], [490, 220], 3)
    
    def draw_scoreboard(self, screen, 
            pole_color=None, scoreboard_color=None, scoreboard_border_color=None) -> None:
        """
        Draw scoreboard with the post
        optional arguments for pole_color, scoreboard_color, scoreboard_border_color
        default respective is gray, black and white
        :self, screen, pole_color, scoreboard_color, scoreboard_border_color
        """
        if pole_color is None:
            pole_color = GRAY
        if scoreboard_color is None:
            scoreboard_color = BLACK
        if scoreboard_border_color is None:
            scoreboard_border_color = WHITE
        
        #score board pole
        pygame.draw.rect(screen, pole_color, [390, 120, 20, 70])

        #score board
        pygame.draw.rect(screen, scoreboard_color, [300, 40, 200, 90])
        pygame.draw.rect(screen, scoreboard_border_color, [302, 42, 198, 88], 2)

    def draw_goal(self, screen, goal_color=None, net_color=None) -> None:
        """
        Draw both the goal post and net with optional arguments goal and net color
        both default are white
        :self, screen, goal_color, net_color
        """
        if goal_color is None:
            goal_color = WHITE
        if net_color is None:
            net_color = WHITE

        # goal post
        pygame.draw.rect(screen, goal_color, [320, 140, 160, 80], 5)
        pygame.draw.line(screen, goal_color, [340, 200], [460, 200], 3)
        pygame.draw.line(screen, goal_color, [320, 220], [340, 200], 3)
        pygame.draw.line(screen, goal_color, [480, 220], [460, 200], 3)
        pygame.draw.line(screen, goal_color, [320, 140], [340, 200], 3)
        pygame.draw.line(screen, goal_color, [480, 140], [460, 200], 3)

        # net part 1 vertical back
        for i in range(8):
            pygame.draw.line(screen, net_color, [325+i*5, 140], [341+i*3, 200], 1)
        
        for i in range(20):
            pygame.draw.line(screen, net_color, [364+i*4, 140], [365+i*4, 200], 1)
        
        for i in range(8):
            pygame.draw.line(screen, net_color, [445+i*5, 140], [441+i*3, 200], 1)

        # net part 2 left
        for i in range(8):
            pygame.draw.line(screen, net_color, [320, 140], [324+i*2, 216-i*2], 1)

        # net part 3 right 
        for i in range(8):
            pygame.draw.line(screen, net_color, [480, 140], [476-i*2, 216-i*2], 1)

        # net part 4 horizontal back
        for i in range(14):
            pygame.draw.line(screen, net_color, [324, 144+i*4], [476, 144+i*4], 1)
    
    def draw_light_pole(self, screen, light_color, pole_color = None, 
                        pole1_x_offset=0, pole2_x_offset=0) -> None:
        """
        Draw light pole with optional argument pole_color
        default is gray,
        pole1_x_offset would move the light pole 1 left or right
        pole2_x_offset would move the light pole 2 left or right
        :self, screen, light_color, pole_color, pole1_x_offset, pole2_x_offset
        """
        if pole_color is None:
            pole_color = GRAY

        # light pole 1 left
        pygame.draw.rect(screen, pole_color, [150 + pole1_x_offset, 60, 20, 140])
        pygame.draw.ellipse(screen, pole_color, [150 + pole1_x_offset, 195, 20, 10])

        # lights left
        pygame.draw.line(screen, pole_color, [110 + pole1_x_offset, 60], [210 + pole1_x_offset, 60], 2)
        pygame.draw.ellipse(screen, light_color, [110 + pole1_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [130 + pole1_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [150 + pole1_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [170 + pole1_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [190 + pole1_x_offset, 40, 20, 20])
        pygame.draw.line(screen, pole_color, [110 + pole1_x_offset, 40], [210 + pole1_x_offset, 40], 2)
        pygame.draw.ellipse(screen, light_color, [110 + pole1_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [130 + pole1_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [150 + pole1_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [170 + pole1_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [190 + pole1_x_offset, 20, 20, 20])
        pygame.draw.line(screen, pole_color, [110 + pole1_x_offset, 20], [210 + pole1_x_offset, 20], 2)

        # light pole 2 right
        pygame.draw.rect(screen, pole_color, [630 + pole2_x_offset, 60, 20, 140])
        pygame.draw.ellipse(screen, pole_color, [630 + pole2_x_offset, 195, 20, 10])

        # lights right
        pygame.draw.line(screen, pole_color, [590 + pole2_x_offset, 60], [690 + pole2_x_offset, 60], 2)
        pygame.draw.ellipse(screen, light_color, [590 + pole2_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [610 + pole2_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [630 + pole2_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [650 + pole2_x_offset, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [670 + pole2_x_offset, 40, 20, 20])
        pygame.draw.line(screen, pole_color, [590 + pole2_x_offset, 40], [690 + pole2_x_offset, 40], 2)
        pygame.draw.ellipse(screen, light_color, [590 + pole2_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [610 + pole2_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [630 + pole2_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [650 + pole2_x_offset, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [670 + pole2_x_offset, 20, 20, 20])
        pygame.draw.line(screen, pole_color, [590 + pole2_x_offset, 20], [690 + pole2_x_offset, 20], 2)

    def draw_stands(self, screen, primary_color=None, secondary_color=None) -> None:
        """
        Draw stands with optional argument for primary color and secondary color
        default is red and white
        :self, screen, primary_color, secondary_color
        """
        if primary_color is None:
            primary_color = RED
        if secondary_color is None:
            secondary_color = WHITE

        # stands right
        pygame.draw.polygon(screen, primary_color, [[680, 220], [800, 340], [800, 290], [680, 180]])
        pygame.draw.polygon(screen, secondary_color, [[680, 180], [800, 100], [800, 290]])

        # stands left
        pygame.draw.polygon(screen, primary_color, [[120, 220], [0, 340], [0, 290], [120, 180]])
        pygame.draw.polygon(screen, secondary_color, [[120, 180], [0, 100], [0, 290]])

    def draw_corner_flag(self, screen, flag_pole_color=None, flag_color=None) -> None:
        """
        Draw the corner flag with optional arguments for flag_pole_color and flag_color
        default is bright yellow and red
        :self, screen, flag_pole_color, flag_color
        """
        if flag_pole_color is None:
            flag_pole_color = BRIGHT_YELLOW
        if flag_color is None:
            flag_color = RED
        
        # corner flag left
        pygame.draw.line(screen, flag_pole_color, [140, 220], [139, 190], 3)
        pygame.draw.polygon(screen, flag_color, [[137, 190], [128, 196], [130, 206], [138, 202]])

        # corner flag right
        pygame.draw.line(screen, flag_pole_color, [660, 220], [661, 190], 3)
        pygame.draw.polygon(screen, flag_color, [[663, 190], [671, 196], [668, 205], [662, 202]]) 

def main():
    """
    The main function to initialize a soccer game and run it
    :none
    """
    soccer_game = Soccer(stars_count=1000, clouds_count=20, darkness_offset=30)
    soccer_game.run()

if __name__ == "__main__":
    main()
