
# Imports
import pygame
import math
import random

#easy modifications such as altering object locations, quantities, and sizes
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

def stadium_light(pole_color, pole_dimensions, lights_color, light_dimension_x, light_dimension_y ):
        '''stadium_light function creates the stadium lights that include the pole and 10 lights. The parameters allow the change of
        colors and positioning of the pole and lights.
        Parameters:
        pole_color (String):            desired color for the pole
        pole_dimensions (int List):     dimensions of the pole. [left, top, width, height]
        lights_color (String):          desired color for the lights
        light_dimension_x:              where the desired rows of lights would start being drawn from
        light_dimension_y:              where the desired rows of lights would end at
        Returns:
        None        
        '''

        pygame.draw.rect(screen, pole_color, pole_dimensions)
        pygame.draw.ellipse(screen, pole_color, [pole_dimensions[0],pole_dimensions[1]+135, pole_dimensions[2], pole_dimensions[3]-130])
        n = 0
        height = 0
        for i in range(2):
            pygame.draw.line(screen, pole_color, [light_dimension_x, 60-height], [light_dimension_y, 60-height], 2)
            for i in range(5):
                pygame.draw.ellipse(screen, lights_color, [light_dimension_x + n, 40 - height, 20, 20])
                n += 20
            n = 0
            height += 20
        pygame.draw.line(screen, pole_color, [light_dimension_x, 20], [light_dimension_y, 20], 2)

        #pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
        #pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])
        #lights(110,210)

def fence(color):
        '''fence function determines the background fence of the graphic. With the parameters able to change the color and positioning
        of the fence.
        
        Parameters:
        color (String):     desired color of the fence
        x_pos (int):        x position of the fence
        y_pos (int):        y position of the fence
        Returns:
        None
        '''
        y = 170
        for x in range(5, 800, 30):
            pygame.draw.polygon(screen, color, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

        y = 170
        for x in range(5, 800, 3):
            pygame.draw.line(screen, color, [x, y], [x, y + 15], 1)

        x = 0
        for y in range(170, 185, 4):
            pygame.draw.line(screen, color, [x, y], [x + 800, y], 1)

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
    '''pygame draw line function are commands used to draw the net. The color and width specified in the function
    parameter are applied to each line drawing. each line beginning and end points coordinates'''

def netPartTwo(color, width):
        
        StartingXAxis = 320
        StartingYAxis = 140
        endingXAxis =324
        endingYAxis = 216

        for i in range(8):
            pygame.draw.line(screen, color, [StartingXAxis, StartingYAxis], [endingXAxis, endingYAxis], width)
            endingXAxis += 2
            endingYAxis -= 2
'''uses a for loop to draw a series of diagonal lines with a constant slope. The loop iterates 8 times, and on each iteration
 a new diagonal line is drawn using pygame.draw.line.

 
StartingXAxis, StartingYAxis, endingXAxis, and endingYAxis variables. These variables are initialized before the loop, and their values are updated on each iteration to create the diagonal slope.
variables are updated on each iteration of the loop using the += operator to increase the X.
'''

def netPartThree(color, width):

    StartingXAxis = 480
    StartingYAxis = 140
    endingXAxis = 476
    endingYAxis = 216
   
    for i in range(8):
        pygame.draw.line(screen, color, [StartingXAxis, StartingYAxis], [endingXAxis, endingYAxis], width)
        endingXAxis -= 2
        endingYAxis -= 2     
    '''same as above expect in the loop using the -= operator to decrease the x that creates a diagonal slope with a constant slope of +1'''    

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
    '''netPartFour uses a combination of horizontal and diagonal lines to create the net shape. The first 9 lines are drawn horizontally using pygame.draw.line
    to create the top of the net, while the remaining 5 lines are drawn diagonally to create the bottom part of the net.
    
    a combination of horizontal and diagonal lines to create the overall shape'''
    
def goalPostBars(color):
    #draw bars for goal post
    pygame.draw.rect(screen, color, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, color, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, color, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, color, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, color, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, color, [480, 140], [460, 200], 3)


def drawGoalPost(color, width):
    netPartOne(color,width)
    netPartTwo(color, width)
    netPartThree(color,width)
    netPartFour(color, width)
    goalPostBars(color)
    '''this function calls and all parts of the net to complete the shape of the goal post.'''

def drawStands (upperStandColor, lowerStandColor):
    #stands right
    pygame.draw.polygon(screen, lowerStandColor, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, upperStandColor, [[680, 180], [800, 100], [800, 290]])

    #stands left
    pygame.draw.polygon(screen, lowerStandColor, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, upperStandColor, [[120, 180], [0, 100], [0, 290]])
    '''Each set of stands is drawn using pygame.draw.polygon, which allows for the drawing of irregular shapes with multiple vertices.
    The lowerStandColor argument is used to color the lower parts of the stands, while the upperStandColor argument is used to color the upper parts of the stands.
    
    The vertices of each polygon are hardcoded into the function using a series of [x, y] coordinate pairs. 
    The first pair in each polygon corresponds to the bottom left corner of the stand, and the subsequent pairs define the shape of the polygon.'''

def drawLeftFlag(x, y, poleColor, flagColor):
    pygame.draw.line(screen, poleColor, [x, y], [x-5, y-30], 3)
    pygame.draw.polygon(screen, flagColor, [[x-8, y-30], [x-15, y-24], [x-5, y-15]])

def drawRightFlag(x, y, poleColor, flagColor):
    pygame.draw.line(screen, poleColor, [x, y], [x+5, y-30], 3)
    pygame.draw.polygon(screen, flagColor, [[x+8, y-30], [x+15, y-24], [x+5, y-15]]) 
    '''The vertices of the polygon are hardcoded into the function using a series of [x, y] coordinate pairs. 
    The coordinates of these pairs determine the shape of the flag.'''

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
    '''The function begins by drawing a line along the bottom edge of the screen to mark the out-of-bounds area. 
    It then draws lines along the left and right edges of the field to define the out-of-bounds areas on those sides. Next, it draws an ellipse to mark the "safety circle" in the center of the field.'''
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
    '''The function then draws the 18-yard line goal box, which is the rectangular area in front of each goal where certain rules apply. 
    Finally, it draws the smaller 6-yard line goal box within the larger box, and the curved arc at the top of the larger box that defines the penalty area'''
    
def drawStar(x, y, color, scale):
    pygame.draw.ellipse(screen, color, [x,y,scale,scale])
    '''The size of the ellipse is determined by the scale argument specifies the width and height of the ellipse in pixels'''
# Config
lights_on = True #This variable could be used to control whether or not the lights in a game or application are turned on or off.
day = True #This variable could be used to control the appearance or behavior of the game or application based on the time of day.

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    color = random.choice([RED,GREEN,BLUE,YELLOW,WHITE])
    scale = random.uniform(0.5, 3)
    stars.append([x, y, color, scale])
    '''for loop to generate 200 stars 
    x,y are set randomly generates color and scale also has a certain range 
    r is the radius of the star 
    color is also randomly generated from 5 different colors
    scale is also randomly generated size between 0.5 to 3 f'''

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    scale = random.uniform(0.5, 3)
    clouds.append([x, y, scale])
    '''for loop generate 20 clouds 
    x,y make a random integer between two values for the size of the cloud 
    scale is also a random floating point for the size of each cloud 
    '''

# Game loop
done = False
'''the done variable can be set to True to stop the game loop and exit the program.'''

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
    fence(NIGHT_GRAY) 

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    for c in clouds:
        draw_cloud(cloud_color, c[0], c[1], c[2])
    screen.blit(SEE_THROUGH, (0, 0)) #transparency 
    '''to draw the fence set the color for night and day and loop that iterates over the colouds'''

    drawFieldLines(WHITE)
    
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [301, 41, 198, 88], 2)
    


    #light pole and lights 1
    stadium_light(GRAY,[150, 60, 20, 140], light_color, 110,210)

    #light pole and lights 2
    stadium_light(GRAY,[630, 60, 20, 140], light_color, 590,690)

    #Function to draw the goal post with parameters Color and width for net lines
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