# Assignment 6 Read me [2520.02]
##graphics_v5.py

Code Documentation:

Program Objective lines 1-245:
	Make the program easy to adapt to other programs and for modularity. 

Modification to clouds (lines 51-86):


Refresh rate (line 19) : 
	Allowed the user to choose the refresh rate

Lights-on(line 92-103):
	Allowed the user to use a True or False value for lights 

The modifications made to the code to allow for user input to control the day/night cycle and toggle the lights on/off:

Added two boolean variables, day and lights_on, to represent the current state of the day/night cycle and lights status respectively.
Wrapped the event processing logic inside a for loop that iterates over all events in the event queue using pygame.event.get().
Added event handling for two keys: 'l' to toggle the lights on/off, and 'd' to toggle between day and night mode.
Modified the game logic to use the day and lights_on variables to determine the appropriate colors for the sky, field, stripe, cloud, and fence based on the current state.
Added a function draw_cloud(x, y) to encapsulate the drawing logic for the cloud, which takes in the cloud's coordinates (x, y) as input parameters.
Moved the cloud drawing logic from the main game loop to the draw_cloud() function, and replaced the previously hard-coded color values with the cloud_color variable that is determined based on the day variable.
Removed the unused STAR_COLOR variable, as it was not used in the code.
These modifications allow the user to control the day/night cycle and toggle the lights on/off by pressing the 'd' and 'l' keys respectively during the game loop.

goal(length,height,color):
        goal draws a goal net based on its length, height, and color
Parameter:
        :length: length of the rectangle shape goal net
        :height: height of the rectangle shape goal net
        :color: color of the goal net

draw_line_goal_box(color):
        draw_line_goal_box draws the line in front of the goal net based on the provided color
Parameter:
        :color: color of the boal box line

	
draw_light(x_index):
        draw_light draws the light of the court based on the provided x index
Parameter:
        :x_index: x index of the light pole bottom


def draw_stand(front_color,back_color):
        draw_stand draws the left and right viewer stands based on the provided color
Parameter:
        :front_color: front color of the stand
        :back_color: back color of the stand

def draw_left_flag(stick_color, flag_color, x, y):
	draw_left_flag draws a small flag t that tilted left based on xy index and its color
Parameter:
        :stick_color: stick color
        :flag_color: flag color
        :x: x index
        :y: y index
	
 draw_right_flag(stick_color, flag_color, x, y):
        draw_left_flag draws a small flag t that tilted right based on xy index and its color
Parameter:
        :stick_color: stick color
        :flag_color: flag color
        :x: x index
        :y: y index
        
