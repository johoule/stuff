import pygame
from constants import *
import random

# This is where the cloud starts to be drawn from
SEE_THROUGH = pygame.Surface((width, 180)) # if the game board size changes, then so will the starting point for clouds
# This is the opacity so how bright or dim the clouds are. If you set it to 20 its barely visible
SEE_THROUGH.set_alpha(150) 
# Not sure what this does. Maybe its the cloud color but it gets over writen? by cloud_color
#SEE_THROUGH.fill((124, 118, 135))


stars = []
for n in range(200):
    x = random.randrange(0, width) #if the board game size changes, so will this and so the stars will be consistent
    y = random.randrange(0, height/3) #same with this. If the board size changes the stars will match the new display
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])



clouds = []
for i in range(20):
    x = random.randrange(-100, 2*width) #This is the range where the clouds start when you first start the game 
                                        # The reason the value is 1600 is because 800 is the max width and all the clouds will be cramped
    y = random.randrange(0, 150)    #The reason why we don't use 200 here is because the fence is 50 points tall but try
                                    #putting 200 here and you will see partial cloud by the fence
    #y = random.randrange(0,height) This might be better
    clouds.append([x, y])


def draw_cloud(x, y, cloud_color):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10]) 
    
    
def draw_stars_moon(sky_color):
    pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) # Change sun to white and shape it
    pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40]) # Color a portion of the circle to make it look crescent
    for s in stars: #
        pygame.draw.ellipse(screen, WHITE, s)

def draw_sun():
    pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])