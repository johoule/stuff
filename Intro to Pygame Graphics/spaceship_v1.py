#computer programming 1
#Jordan Houle
#space ship

# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Spaceship"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    for n in range(200):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
        r = random.randrange(1, 5)
        pygame.draw.ellipse(screen, WHITE,  [x, y, r, r])

    #ship walls
    pygame.draw.rect(screen, WHITE, [0, 0, 100, 420])
    pygame.draw.rect(screen, WHITE, [100, 0, 700, 80])
    pygame.draw.rect(screen, WHITE, [720, 80, 80, 520])
    pygame.draw.rect(screen, WHITE, [100, 340, 620, 80])

    #windows
    pygame.draw.arc(screen, RED, [90, 70, 40, 40], math.pi/2, math.pi, 10)
    pygame.draw.rect(screen, RED, [90, 85, 10, 200])
    pygame.draw.arc(screen, RED, [90, 310, 40, 40], math.pi, 3/2 * math.pi , 10) 
    

    '''examples'''
    #pygame.draw.rect(screen, RED, [50, 50, 400, 300])
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
    #pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
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
