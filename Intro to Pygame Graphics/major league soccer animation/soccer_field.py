import pygame
import math
from constants import *

def display_field(field_color, stripe_color):
    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)
    
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


def display_goal_lines():
    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

def display_goal_box():
    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

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
