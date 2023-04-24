# Computer Programming 1
# Pygame Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 150)



# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''


	
    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

	
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

	
    ''' fence '''

    

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
