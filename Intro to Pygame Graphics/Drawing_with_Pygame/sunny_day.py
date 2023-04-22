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


# make stars
stars = []
for i in range(200):
    x = random.randint(0, 800)
    y = random.randint(0, 400)
    d = random.randint(1, 5)
    stars.append([x, y, d, d])

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
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
	
    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

	
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

	
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10,y+5],
                                            [x+10, y+40],[x, y+40],
                                            [x, y+5]])

    pygame.draw.line(screen, WHITE, [0, y+10], [800, y+10], 5)
    pygame.draw.line(screen, WHITE, [0, y+30], [800, y+30], 5)
    

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
