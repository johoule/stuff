# Imports
import pygame
import math
import random


# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
REFRESH_RATE = 60


# Colors
''' add colors you use as RGB values here '''
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
CK = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

def draw_cloud(color, x, y, scale):
    '''
    This function draws a cloud shape on the Pygame surface specified by the global variable SEE_THROUGH. 
    The cloud shape consists of four ellipses and one rectangle, all with the same color specified by the 
    global variable cloud_color. The coordinates of the ellipses and rectangle are calculated based on the
    given x and y coordinates.

    Parameters:
    color (tuple): The color for the cloud as a tuple of 3 integers representing the RGB color.
    x (int): The x-coordinate of the top-left corner of the cloud shape.
    y (int): The y-coordinate of the top-left corner of the cloud shape.
    scale (float): Scale factor to resize the cloud.

    Returns:
    None
    '''

    pygame.draw.ellipse(SEE_THROUGH, color, [x, y + 8*scale, 10*scale, 10*scale])
    pygame.draw.ellipse(SEE_THROUGH, color, [x + 6*scale, y + 4*scale, 8*scale, 8*scale])
    pygame.draw.ellipse(SEE_THROUGH, color, [x + 10*scale, y, 16*scale, 16*scale])
    pygame.draw.ellipse(SEE_THROUGH, color, [x + 20*scale, y + 8*scale, 10*scale, 10*scale])
    pygame.draw.rect(SEE_THROUGH, color, [x + 6*scale, y + 8*scale, 18*scale, 10*scale])

def drawGrass(color1, color2):
    pygame.draw.rect(screen, color1, [0, 180, 800 , 420])
    pygame.draw.rect(screen, color2, [0, 180, 800, 42])
    pygame.draw.rect(screen, color2, [0, 264, 800, 52])
    pygame.draw.rect(screen, color2, [0, 368, 800, 62])
    pygame.draw.rect(screen, color2, [0, 492, 800, 82])

def lights(a, b):
        '''lights(a,b) function creates the head of a stadium lights

        :param: a determines positioning of the stadium head graphic
        :param: b figures out the length of where the pygame draws
        '''
        pygame.draw.line(screen, GRAY, [a, 60], [b, 60], 2)
        pygame.draw.ellipse(screen, light_color, [a, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+20, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+40, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+60, 40, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+80, 40, 20, 20])
        pygame.draw.line(screen, GRAY, [a, 40], [b, 40], 2)
        pygame.draw.ellipse(screen, light_color, [a, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+20, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+40, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+60, 20, 20, 20])
        pygame.draw.ellipse(screen, light_color, [a+80, 20, 20, 20])
        pygame.draw.line(screen, GRAY, [a, 20], [b, 20], 2)

def netPartOne(color, width):
    #net
    pygame.draw.line(screen, color, [325, 140], [341, 200], width) 
    pygame.draw.line(screen, color, [330, 140], [344, 200], width)
    pygame.draw.line(screen, color, [335, 140], [347, 200], width)
    pygame.draw.line(screen, color, [340, 140], [350, 200], width)
    pygame.draw.line(screen, color, [345, 140], [353, 200], width)
    pygame.draw.line(screen, color, [350, 140], [356, 200], width)
    pygame.draw.line(screen, color, [355, 140], [359, 200], width)
    pygame.draw.line(screen, color, [360, 140], [362, 200], width)
    pygame.draw.line(screen, color, [364, 140], [365, 200], width)
    pygame.draw.line(screen, color, [368, 140], [369, 200], width)
    pygame.draw.line(screen, color, [372, 140], [373, 200], width)
    pygame.draw.line(screen, color, [376, 140], [377, 200], width)
    pygame.draw.line(screen, color, [380, 140], [380, 200], width)
    pygame.draw.line(screen, color, [384, 140], [384, 200], width)
    pygame.draw.line(screen, color, [388, 140], [388, 200], width)
    pygame.draw.line(screen, color, [392, 140], [392, 200], width)
    pygame.draw.line(screen, color, [396, 140], [396, 200], width)
    pygame.draw.line(screen, color, [400, 140], [400, 200], width)
    pygame.draw.line(screen, color, [404, 140], [404, 200], width)
    pygame.draw.line(screen, color, [408, 140], [408, 200], width)
    pygame.draw.line(screen, color, [412, 140], [412, 200], width)
    pygame.draw.line(screen, color, [416, 140], [416, 200], width)
    pygame.draw.line(screen, color, [420, 140], [420, 200], width)
    pygame.draw.line(screen, color, [424, 140], [423, 200], width)
    pygame.draw.line(screen, color, [428, 140], [427, 200], width)
    pygame.draw.line(screen, color, [432, 140], [431, 200], width)
    pygame.draw.line(screen, color, [436, 140], [435, 200], width)
    pygame.draw.line(screen, color, [440, 140], [438, 200], width)
    pygame.draw.line(screen, color, [445, 140], [441, 200], width)
    pygame.draw.line(screen, color, [450, 140], [444, 200], width)
    pygame.draw.line(screen, color, [455, 140], [447, 200], width)
    pygame.draw.line(screen, color, [460, 140], [450, 200], width)
    pygame.draw.line(screen, color, [465, 140], [453, 200], width)
    pygame.draw.line(screen, color, [470, 140], [456, 200], width)
    pygame.draw.line(screen, color, [475, 140], [459, 200], width)

def netPartTwo(color, width):
        
        StartingXAxis = 320
        StartingYAxis = 140
        endingXAxis =324
        endingYAxis = 216

        for i in range(8):
            pygame.draw.line(screen, color, [StartingXAxis, StartingYAxis], [endingXAxis, endingYAxis], width)
            endingXAxis += 2
            endingYAxis -= 2


def netPartThree(color, width):

    StartingXAxis = 480
    StartingYAxis = 140
    endingXAxis = 476
    endingYAxis = 216
   
    for i in range(8):
        pygame.draw.line(screen, color, [StartingXAxis, StartingYAxis], [endingXAxis, endingYAxis], width)
        endingXAxis -= 2
        endingYAxis -= 2         

def netPartFour(color, width):

    #net part 4
    pygame.draw.line(screen, color, [324, 144], [476, 144], width)
    pygame.draw.line(screen, color, [324, 148], [476, 148], width)
    pygame.draw.line(screen, color, [324, 152], [476, 152], width)
    pygame.draw.line(screen, color, [324, 156], [476, 156], width)
    pygame.draw.line(screen, color, [324, 160], [476, 160], width)
    pygame.draw.line(screen, color, [324, 164], [476, 164], width)
    pygame.draw.line(screen, color, [324, 168], [476, 168], width)
    pygame.draw.line(screen, color, [324, 172], [476, 172], width)
    pygame.draw.line(screen, color, [324, 176], [476, 176], width)
    pygame.draw.line(screen, color, [335, 180], [470, 180], width)
    pygame.draw.line(screen, color, [335, 184], [465, 184], width)
    pygame.draw.line(screen, color, [335, 188], [465, 188], width)
    pygame.draw.line(screen, color, [335, 192], [465, 192], width)
    pygame.draw.line(screen, color, [335, 196], [465, 196], width)

def drawGoalPost(color, width):
    netPartOne(color,width)
    netPartTwo(color, width)
    netPartThree(color,width)
    netPartFour(color, width)

def drawStands (upperStandColor, lowerStandColor):
    #stands right
    pygame.draw.polygon(screen, lowerStandColor, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, upperStandColor, [[680, 180], [800, 100], [800, 290]])

    #stands left
    pygame.draw.polygon(screen, lowerStandColor, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, upperStandColor, [[120, 180], [0, 100], [0, 290]])

def drawLeftFlag(x, y, poleColor, flagColor):
    pygame.draw.line(screen, poleColor, [x, y], [x-5, y-30], 3)
    pygame.draw.polygon(screen, flagColor, [[x-8, y-30], [x-15, y-24], [x-5, y-15]])

def drawRightFlag(x, y, poleColor, flagColor):
    pygame.draw.line(screen, poleColor, [x, y], [x+5, y-30], 3)
    pygame.draw.polygon(screen, flagColor, [[x+8, y-30], [x+15, y-24], [x+5, y-15]]) 

def drawFieldLines(color):
    #bottom side of out of bounds
    pygame.draw.line(screen, color, [0, 580], [800, 580], 5)

    #left side of out of bounds
    pygame.draw.line(screen, color, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, color, [140, 220], [660, 220], 3)

    #right side of out of bounds
    pygame.draw.line(screen, color, [660, 220], [800, 360], 5)

    #safety circle
    pygame.draw.ellipse(screen, color, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, color, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, color, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, color, [620, 300], [540, 220], 5)

    #6 yard line goal box
    pygame.draw.line(screen, color, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, color, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, color, [530, 270], [490, 220], 3)

    #arc at the top of the goal box
    pygame.draw.arc(screen, color, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    
def drawStar(x, y, color, scale):
    pygame.draw.ellipse(screen, color, [x,y,scale,scale])

# Config
lights_on = True
day = True


stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    color = random.choice([RED,GREEN,BLUE,YELLOW,WHITE])
    scale = random.uniform(0.5, 3)
    stars.append([x, y, color, scale])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    scale = random.uniform(0.5, 3)
    clouds.append([x, y, scale])
    
# Game loop
done = False


# Counter to allow flags to bounce up and down
flagVerticalCounter = 0

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(CK)
    SEE_THROUGH.set_colorkey(CK)
    
    if not day:
    #stars
        for s in stars:
            drawStar(s[0], s[1], s[2], s[3])
            
    drawGrass(field_color, stripe_color)
    


    '''fence'''
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    
    
    for c in clouds:
        draw_cloud(cloud_color, c[0], c[1], c[2])
    screen.blit(SEE_THROUGH, (0, 0))   
    

    drawFieldLines(WHITE)
    
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)

    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)


    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #lights pole 1
    lights(110,210)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights
    lights(590,690)

    #Function to draw the goal post with parameters Colour and width
    drawGoalPost(WHITE,1)
    drawStands(WHITE, RED)


    #flag moving code
    flagVerticalCounter+=0.75
    offset = flagVerticalCounter % 40 - 20
    if (offset > 0):
        offset *= -1

    #corner flag left
    drawLeftFlag(140, 220 + offset, YELLOW, RED)

    #corner flag right
    drawRightFlag(660, 220 + offset, YELLOW, RED)

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(REFRESH_RATE)


# Close window and quit
pygame.quit()
