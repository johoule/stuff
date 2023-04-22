#computer programming 1
#intro to Pygame Graphics Quiz
#
#Directions:
#
#use the graph paper provided to draw the image created by this program.
#There are  elements you must draw. Each is worth  points.

# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Tropical Vacation"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
COLOR1 = (195, 150, 253)
COLOR2 = (121, 155, 196)
COLOR3 = (210, 96, 8)
COLOR4 = (252, 249, 204)
COLOR5 = (189, 205, 225)


# Game loop
done = False

while not done:
    # Event processing 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing code 
    screen.fill(COLOR1)

    pygame.draw.ellipse(screen, COLOR4, [60, 200, 160, 160])

    pygame.draw.rect(screen, COLOR2, [0, 280, 800, 320])

    pygame.draw.polygon(screen, COLOR3, [[400, 280], [720, 600], [800, 600], [800, 280]])

    pygame.draw.polygon(screen, COLOR5, [[60, 280], [220, 280], [380, 600], [0, 600], [0, 380]])


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
