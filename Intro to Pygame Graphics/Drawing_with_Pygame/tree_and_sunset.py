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
TITLE = "Sunset and Tree"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
COLOR1 = (151, 23, 148)
COLOR2 = (10, 73, 13)
COLOR3 = (234, 155, 36)
COLOR4 = (66, 43, 6)
COLOR5 = (79, 126, 14)


# Game loop
done = False

while not done:
    # Event processing 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing code 
    screen.fill(COLOR1)
    
    pygame.draw.ellipse(screen, COLOR3, [500, 280, 240, 240])

    pygame.draw.rect(screen, COLOR2, [0, 340, 800, 260])

    pygame.draw.rect(screen, COLOR4, [200, 200, 40, 320])
    pygame.draw.polygon(screen, COLOR4, [[200, 500], [180, 540], [260, 540], [240, 500]])

    pygame.draw.ellipse(screen, COLOR5, [160, 40, 120, 120])
    pygame.draw.ellipse(screen, COLOR5, [240, 100, 120, 120])
    pygame.draw.ellipse(screen, COLOR5, [160, 140, 120, 120])
    pygame.draw.ellipse(screen, COLOR5, [80, 100, 120, 120])
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
