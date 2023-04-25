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
refresh_rate = int(input("What do you want the refresh rate to be: "))


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
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

import pygame

# Get user input for x_cloud, y_cloud, cloud_color, and cloud_size
x_cloud = int(input("Enter the x-coordinate of the cloud's top-left corner: "))
y_cloud = int(input("Enter the y-coordinate of the cloud's top-left corner: "))
cloud_color = tuple(map(int, input("Enter the color of the cloud in RGB format (comma-separated values): ").split(',')))
cloud_size = int(input("Enter the size of the cloud: "))

def draw_cloud(x_cloud, y_cloud, cloud_color, cloud_size):
    """
    Draw a cloud at the given x, y coordinates with the specified color and size.

    Args:
        x_cloud (int): The x-coordinate of the cloud's top-left corner.
        y_cloud (int): The y-coordinate of the cloud's top-left corner.
        cloud_color (tuple): The color of the cloud in RGB format, e.g. (255, 255, 255) for white.
        cloud_size (int): The size of the cloud, which determines the size of the ellipses and rectangle.

    Returns:
        None
    """
    # Define the sizes of the ellipses and rectangle based on cloud_size
    ellipse1_size = int(10 * cloud_size / 30)
    ellipse2_size = int(8 * cloud_size / 30)
    ellipse3_size = int(16 * cloud_size / 30)
    ellipse4_size = int(10 * cloud_size / 30)
    rect_width = int(18 * cloud_size / 30)
    rect_height = int(10 * cloud_size / 30)

    # Draw the ellipses and rectangle with the specified color and sizes
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x_cloud, y_cloud + ellipse1_size, ellipse1_size, ellipse1_size])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x_cloud + int(6 * cloud_size / 30), y_cloud + ellipse2_size, ellipse2_size, ellipse2_size])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x_cloud + int(10 * cloud_size / 30), y_cloud, ellipse3_size, ellipse3_size])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x_cloud + int(20 * cloud_size / 30), y_cloud + ellipse4_size, ellipse4_size, ellipse4_size])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x_cloud + int(6 * cloud_size / 30), y_cloud + ellipse1_size, rect_width, rect_height])

# Call the function with user input values
draw_cloud(x_cloud, y_cloud, cloud_color, cloud_size)



# Config
#True or False values
def are_lights_on():
    """
    Check if the lights are on.

    Returns:
        bool: True if the lights are on, False otherwise.
    """
    lights_on = input("Are the lights on:(yes/no) ")
    if lights_on.lower() == "yes" or lights_on.lower() == "y":
        return True
    else:
        return False


def is_day():
    """
    Check if it is day.

    Returns:
        bool: True if it is day, False otherwise.
    """
    day = input("Is it day?(yes/no) ")
    if day.lower() == "yes" or day.lower() == "y":
        return True
    else:
        return False


def generate_stars_and_clouds():
    """
    Generate stars and clouds for the animation, taking user input for the number of stars and clouds.

    Returns:
        tuple: A tuple containing two lists: stars and clouds.
    """
    num_stars = int(input("Enter the number of stars to generate: "))
    num_clouds = int(input("Enter the number of clouds to generate: "))

    stars = []
    for n in range(num_stars):
        x = random.randrange(0, 800)
        y = random.randrange(0, 200)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])

    clouds = []
    for i in range(num_clouds):
        x = random.randrange(-100, 1600)
        y = random.randrange(0, 150)
        clouds.append([x, y])

    return stars, clouds


stars, clouds = generate_stars_and_clouds()

    
def event_processing():
    global done, lights_on, day
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

def game_logic():
    global light_color, sky_color, field_color, stripe_color, cloud_color
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

def drawing_code():
    global screen
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)

    if not day:
        # stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    # fence
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
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))

done = False

while not done:
    event_processing()
    game_logic()
    drawing_code()

    
def draw_soccer_field():
    """
    Draw the soccer field lines and arcs with user-input parameters.
    """
    # Get user input for colors and thicknesses
    out_of_bounds_color = tuple(map(int, input("Enter RGB values for out of bounds lines (comma-separated): ").split(',')))
    left_color = tuple(map(int, input("Enter RGB values for left line (comma-separated): ").split(',')))
    right_color = tuple(map(int, input("Enter RGB values for right line (comma-separated): ").split(',')))
    safety_circle_color = tuple(map(int, input("Enter RGB values for safety circle (comma-separated): ").split(',')))
    yard_line_color = tuple(map(int, input("Enter RGB values for 18 yard line (comma-separated): ").split(',')))
    arc_color = tuple(map(int, input("Enter RGB values for arc (comma-separated): ").split(',')))

    # Get user input for thicknesses
    out_of_bounds_thickness = int(input("Enter thickness for out of bounds lines: "))
    left_thickness = int(input("Enter thickness for left line: "))
    right_thickness = int(input("Enter thickness for right line: "))
    safety_circle_thickness = int(input("Enter thickness for safety circle: "))
    yard_line_thickness = int(input("Enter thickness for 18 yard line: "))
    arc_thickness = int(input("Enter thickness for arc: "))

    # Define lines with same colors and thicknesses
    lines = [
        {'start': [0, 580], 'end': [800, 580], 'color': out_of_bounds_color, 'thickness': out_of_bounds_thickness},
        {'start': [0, 360], 'end': [140, 220], 'color': left_color, 'thickness': left_thickness},
        {'start': [140, 220], 'end': [660, 220], 'color': left_color, 'thickness': left_thickness // 2},
        {'start': [660, 220], 'end': [800, 360], 'color': right_color, 'thickness': right_thickness},
        {'start': [260, 220], 'end': [180, 300], 'color': yard_line_color, 'thickness': yard_line_thickness},
        {'start': [180, 300], 'end': [620, 300], 'color': yard_line_color, 'thickness': yard_line_thickness // 2},
        {'start': [620, 300], 'end': [540, 220], 'color': yard_line_color, 'thickness': yard_line_thickness}
    ]

    # Draw lines with same colors and thicknesses
    for line in lines:
        pygame.draw.line(screen, line['color'], line['start'], line['end'], line['thickness'])

    # Draw safety circle
    pygame.draw.ellipse(screen, safety_circle_color, [240, 500, 320, 160], safety_circle_thickness)

    # Draw arc at the top of the goal box
    pygame.draw.arc(screen, arc_color, [330, 280, 140, 40], math.pi, 2 * math.pi, arc_thickness)

    
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

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #lights
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights

        
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)

    #net
    pygame.draw.line(screen, WHITE, [325, 140], [341, 200], 1)
    pygame.draw.line(screen, WHITE, [330, 140], [344, 200], 1)
    pygame.draw.line(screen, WHITE, [335, 140], [347, 200], 1)
    pygame.draw.line(screen, WHITE, [340, 140], [350, 200], 1)
    pygame.draw.line(screen, WHITE, [345, 140], [353, 200], 1)
    pygame.draw.line(screen, WHITE, [350, 140], [356, 200], 1)
    pygame.draw.line(screen, WHITE, [355, 140], [359, 200], 1)
    pygame.draw.line(screen, WHITE, [360, 140], [362, 200], 1)
    pygame.draw.line(screen, WHITE, [364, 140], [365, 200], 1)
    pygame.draw.line(screen, WHITE, [368, 140], [369, 200], 1)
    pygame.draw.line(screen, WHITE, [372, 140], [373, 200], 1)
    pygame.draw.line(screen, WHITE, [376, 140], [377, 200], 1)
    pygame.draw.line(screen, WHITE, [380, 140], [380, 200], 1)
    pygame.draw.line(screen, WHITE, [384, 140], [384, 200], 1)
    pygame.draw.line(screen, WHITE, [388, 140], [388, 200], 1)
    pygame.draw.line(screen, WHITE, [392, 140], [392, 200], 1)
    pygame.draw.line(screen, WHITE, [396, 140], [396, 200], 1)
    pygame.draw.line(screen, WHITE, [400, 140], [400, 200], 1)
    pygame.draw.line(screen, WHITE, [404, 140], [404, 200], 1)
    pygame.draw.line(screen, WHITE, [408, 140], [408, 200], 1)
    pygame.draw.line(screen, WHITE, [412, 140], [412, 200], 1)
    pygame.draw.line(screen, WHITE, [416, 140], [416, 200], 1)
    pygame.draw.line(screen, WHITE, [420, 140], [420, 200], 1)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    pygame.draw.line(screen, WHITE, [428, 140], [427, 200], 1)
    pygame.draw.line(screen, WHITE, [432, 140], [431, 200], 1)
    pygame.draw.line(screen, WHITE, [436, 140], [435, 200], 1)
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    pygame.draw.line(screen, WHITE, [445, 140], [441, 200], 1)
    pygame.draw.line(screen, WHITE, [450, 140], [444, 200], 1)
    pygame.draw.line(screen, WHITE, [455, 140], [447, 200], 1)
    pygame.draw.line(screen, WHITE, [460, 140], [450, 200], 1)
    pygame.draw.line(screen, WHITE, [465, 140], [453, 200], 1)
    pygame.draw.line(screen, WHITE, [470, 140], [456, 200], 1)
    pygame.draw.line(screen, WHITE, [475, 140], [459, 200], 1)

    #net part 2
    pygame.draw.line(screen, WHITE, [320, 140], [324, 216], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [326, 214], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [328, 212], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [330, 210], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [332, 208], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [334, 206], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [336, 204], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [338, 202], 1)

    #net part 3
    pygame.draw.line(screen, WHITE, [480, 140], [476, 216], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [474, 214], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [472, 212], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [470, 210], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [468, 208], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [466, 206], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [464, 204], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [462, 202], 1)

    #net part 4
    pygame.draw.line(screen, WHITE, [324, 144], [476, 144], 1)
    pygame.draw.line(screen, WHITE, [324, 148], [476, 148], 1)
    pygame.draw.line(screen, WHITE, [324, 152], [476, 152], 1)
    pygame.draw.line(screen, WHITE, [324, 156], [476, 156], 1)
    pygame.draw.line(screen, WHITE, [324, 160], [476, 160], 1)
    pygame.draw.line(screen, WHITE, [324, 164], [476, 164], 1)
    pygame.draw.line(screen, WHITE, [324, 168], [476, 168], 1)
    pygame.draw.line(screen, WHITE, [324, 172], [476, 172], 1)
    pygame.draw.line(screen, WHITE, [324, 176], [476, 176], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    pygame.draw.line(screen, WHITE, [335, 184], [465, 184], 1)
    pygame.draw.line(screen, WHITE, [335, 188], [465, 188], 1)
    pygame.draw.line(screen, WHITE, [335, 192], [465, 192], 1)
    pygame.draw.line(screen, WHITE, [335, 196], [465, 196], 1)

    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    #people
    

    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
