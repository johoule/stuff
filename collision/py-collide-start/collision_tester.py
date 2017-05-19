#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of py-collide.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/py-collide>.

# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Collision Tester"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Shape definitions
circle = [375, 275, 50]
rectangle = [350, 275, 100, 50]

# Select test case
'''
1 = point-circle
2 = point-rectangle
3 = circle-circle
4 = rectangle-rectangle
'''
case = 2

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic             
    mouse_pos = pygame.mouse.get_pos()
    circle2 = [mouse_pos[0], mouse_pos[1], 50]
    rectangle2 = [mouse_pos[0], mouse_pos[1], 100, 50]

    if case == 1:
        if intersects.point_circle(mouse_pos, circle):
            color = RED
        else:
            color = WHITE
    elif case == 2:
        if intersects.point_rect(mouse_pos, rectangle):
            color = RED
        else:
            color = WHITE
    elif case == 3:
        if intersects.circle_circle(circle, circle2):
            color = RED
        else:
            color = WHITE
    elif case == 4:
        if intersects.rect_rect(rectangle, rectangle2):
            color = RED
        else:
            color = WHITE

    # Drawing code
    screen.fill(BLACK)

    if case == 1:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
    elif case == 2:
        pygame.draw.rect(screen, color, [rectangle[0], rectangle[1], rectangle[2], rectangle[3]])
    elif case == 3:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
        pygame.draw.circle(screen, WHITE, [circle2[0], circle2[1]], circle2[2])
    elif case == 4:
        pygame.draw.rect(screen, color, [rectangle[0], rectangle[1], rectangle[2], rectangle[3]])
        pygame.draw.rect(screen, WHITE, [rectangle2[0], rectangle2[1], rectangle2[2], rectangle2[3]])

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
