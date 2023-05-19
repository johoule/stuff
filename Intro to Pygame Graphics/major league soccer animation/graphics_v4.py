#Valen edits start here.
# Imports
import pygame
import random
from constants import *
from sky import *
from soccer_field import *
from light_pole import *
from score_board import *

# Initialize game engine
pygame.init()

# Timer
clock = pygame.time.Clock()
refresh_rate = HERTZ

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
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    

    # draw the field with goal box and fence
    # Comment this out and run it :) for fun
    display_field(field_color, stripe_color)

    if not day:
        # draw the stars and moon if its not daytime
        draw_stars_moon(sky_color)
    elif day:
        # draw the sun...
        draw_sun()

    for c in clouds:
        draw_cloud(c[0], c[1], cloud_color)
    screen.blit(SEE_THROUGH, (0, 0)) 

    # this display order does matter as it determines if the object is infront or behind one another
    # Comment this out and run it :) 
    display_score_board()
    display_goal_lines()
    display_goal_box()
    display_lightpole(light_color) 
    display_corner_flag()
    display_stands()
    
   
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
