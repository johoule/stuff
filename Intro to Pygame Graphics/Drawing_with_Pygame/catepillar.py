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
TITLE = "Catepillar"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
COLOR1 = (79, 222, 238)
COLOR2 = (66, 43, 6)
COLOR3 = (85, 54, 112)
COLOR4 = (69, 110, 169)
COLOR5 = (101, 156, 87)
COLOR6 = (216, 194, 48)
COLOR7 = (196, 92, 49)
COLOR8 = (174, 47, 60)
COLOR9 = (255, 255, 255)
COLOR10 = (0, 0, 0)

# Game loop
done = False

while not done:
    # Event processing 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing code 
    screen.fill(COLOR1)

    pygame.draw.rect(screen, COLOR2, [0, 0, 100, 600])
    pygame.draw.rect(screen, COLOR2, [0, 460, 800, 80])
    pygame.draw.polygon(screen, COLOR2, [[100, 540], [460, 540], [100, 600]])

    pygame.draw.ellipse(screen, COLOR3, [480, 380, 80, 80])
    pygame.draw.ellipse(screen, COLOR4, [420, 360, 80, 80])
    pygame.draw.ellipse(screen, COLOR5, [360, 380, 80, 80])
    pygame.draw.ellipse(screen, COLOR6, [300, 360, 80, 80])
    pygame.draw.ellipse(screen, COLOR7, [240, 380, 80, 80])
    pygame.draw.ellipse(screen, COLOR8, [200, 340, 80, 80])

    pygame.draw.ellipse(screen, COLOR9, [220, 360, 20, 20])
    pygame.draw.ellipse(screen, COLOR9, [240, 360, 20, 20])
    
    pygame.draw.ellipse(screen, COLOR10, [230, 370, 3, 3])
    pygame.draw.ellipse(screen, COLOR10, [250, 370, 3, 3])

    pygame.draw.line(screen, COLOR10, [200, 320], [220, 350], 2)
    pygame.draw.line(screen, COLOR10, [250, 350], [280, 320], 2)
    pygame.draw.line(screen, COLOR10, [220, 390], [260, 390], 2)
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
