# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Drawing!"
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
    
x = 0
y = 0
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    x += 1
    y += 1

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    window.fill(WHITE)
    pygame.draw.rect(window, RED, [250, 180, 400, 300])
    pygame.draw.rect(window, BLUE, [300, 250, 100, 80], 5)
    pygame.draw.line(window, GREEN, [300, 40], [100,500], 5)
    pygame.draw.ellipse(window, BLUE, [3, 500, 600, 300])
    pygame.draw.polygon(window, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    pygame.draw.arc(window, ORANGE, [200, 100, 100, 100], 0, math.pi/2, 20)
    pygame.draw.arc(window, BLACK, [100, 100, 100, 100], 0, math.pi, 50)

    pygame.draw.ellipse(window, ORANGE, [x, y, 50, 50])

    # Update window (Actually draw the picture in the window.)
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
