# CS2520 Assignment 6
project is located under Intro to Pygame Graphics > major league soccer animation > graphics_v4.py

updated star and cloud loops:
  This code uses list comprehension to create the stars and clouds lists in a more concise way. It also eliminates the need for temporary variables x, y, and r.

simplied draw_cloud:
  This code stores the ellipse coordinates and dimensions in a list and then iterates over the list to draw each ellipse using a loop. This reduces the number of lines of code from 5 to 2.
 
goal(length,height,color): draws a goal net based on its length, height, and color

draw_line_goal_box(color): draws the line in front of the goal net based on the provided color
	
draw_light(x_index): draws the light of the court based on the provided x index


draw_stand(front_color,back_color): draws the left and right viewer stands based on the provided color

draw_left_flag(stick_color, flag_color, x, y): draws a small flag t that tilted left based on x and y index and its color
	
draw_right_flag(stick_color, flag_color, x, y): draws a small flag t that tilted right based on x and y index and its color


Members:
Natalia Jauregui
Haosi Lin
