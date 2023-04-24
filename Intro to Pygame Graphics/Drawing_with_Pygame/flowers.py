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
TITLE = "Spring Flowers"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
COLOR1 = (138, 203, 243)
COLOR2 = (157, 222, 164)
COLOR3 = (245, 232, 152)
COLOR4 = (244, 166, 126)
COLOR5 = (111, 145, 118)
COLOR6 = (194, 12, 193)
COLOR7 = (252, 106, 175)
COLOR8 = (229, 211, 142)

# Game loop
done = False

while not done:
    # Event processing 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing code 
    screen.fill(COLOR1)

    pygame.draw.rect(screen, COLOR2, [0, 380, 800, 220])

    pygame.draw.line(screen, COLOR4, [120, 20], [120, 220], 8)
    pygame.draw.line(screen, COLOR4, [200, 40], [40, 200], 8)
    pygame.draw.line(screen, COLOR4, [20, 120], [220, 120], 8)
    pygame.draw.line(screen, COLOR4, [40, 40], [200, 200], 8)

    pygame.draw.ellipse(screen, COLOR3, [60, 60, 120, 120])

    pygame.draw.line(screen, COLOR5, [300, 540], [300, 300], 8)
    pygame.draw.line(screen, COLOR5, [300, 460], [240, 400], 6)
    pygame.draw.line(screen, COLOR5, [300, 460], [360, 400], 6)
    
    pygame.draw.line(screen, COLOR5, [500, 540], [500, 300], 8)
    pygame.draw.line(screen, COLOR5, [500, 460], [440, 400], 6)
    pygame.draw.line(screen, COLOR5, [500, 460], [560, 400], 6)
    
    pygame.draw.line(screen, COLOR5, [700, 540], [700, 300], 8)
    pygame.draw.line(screen, COLOR5, [700, 460], [640, 400], 6)
    pygame.draw.line(screen, COLOR5, [700, 460], [760, 400], 6)

    pygame.draw.ellipse(screen, COLOR6, [220, 140, 160, 160])
    pygame.draw.ellipse(screen, COLOR6, [620, 140, 160, 160])

    pygame.draw.ellipse(screen, COLOR7, [420, 140, 160, 160])

    pygame.draw.ellipse(screen, COLOR8, [260, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [300, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [260, 220, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [300, 220, 40, 40])

    pygame.draw.ellipse(screen, COLOR8, [460, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [500, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [460, 220, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [500, 220, 40, 40])

    pygame.draw.ellipse(screen, COLOR8, [660, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [700, 180, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [660, 220, 40, 40])
    pygame.draw.ellipse(screen, COLOR8, [700, 220, 40, 40])

    

    


    
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
