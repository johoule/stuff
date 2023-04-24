# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


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

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))


# Config
lights_on = True
day = True

# Game loop
done = False

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
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)

    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])
    

    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

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

    #lights for pole 1 (refactored)
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    for x in range(90, 190, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    for x in range(90, 190, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights for pole 2 (refactored) 
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    for x in range(570, 670, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    for x in range(570, 670, 20):
        pygame.draw.ellipse(screen, light_color, [x + 20, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)

    #net part 1 (middle left vertical lines) 
    y = 338
    for x in range(320, 360, 5):
        pygame.draw.line(screen, WHITE, [x+5, 140], [y+3, 200], 1)
        y += 3

    # net part 1 (middle of the middle vertical lines)
    y = 361
    for x in range(360, 376, 4):
       pygame.draw.line(screen, WHITE, [x+4, 140], [y+4, 200], 1)
       y += 4
    for x in range(376, 420, 4):
        pygame.draw.line(screen, WHITE, [x+4, 140], [x+4, 200], 1)
    #net part 1 (middle left vertical lines) 
    y = 338
    for x in range(320, 360, 5):
        pygame.draw.line(screen, WHITE, [x+5, 140], [y+3, 200], 1)
        y += 3

    # net part 1 (middle of the middle vertical lines)
    y = 361
    for x in range(360, 376, 4):
       pygame.draw.line(screen, WHITE, [x+4, 140], [y+4, 200], 1)
       y += 4
    for x in range(376, 420, 4):
        pygame.draw.line(screen, WHITE, [x+4, 140], [x+4, 200], 1)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    y = 423
    for x in range(424, 436, 4):
       pygame.draw.line(screen, WHITE, [x+4, 140], [y+4, 200], 1)
       y += 4
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    y = 438
    for x in range(440, 475, 5):
        pygame.draw.line(screen, WHITE, [x+5, 140], [y+3, 200], 1)
        y += 3

    # net part 2
    y = 216
    for x in range (324, 338, 2):
        pygame.draw.line(screen, WHITE, [320, 140], [x+2, y-2], 1)
        y -= 2
    
    #net part 3
    x = 476
    for y in range(216, 202, -2):
        pygame.draw.line(screen, WHITE, [480, 140], [x-2, y-2], 1)
        x -= 2
    
    #net part 4
    for y in range(144, 176, 4):
        pygame.draw.line(screen, WHITE, [324, y+4], [476, y+4], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    for y in range(176, 196, 4):
         pygame.draw.line(screen, WHITE, [335, y+4], [465, y+4], 1)

    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])
    #pygame.draw.ellipse(screen, BLACK, 
  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])

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
