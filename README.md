# CS2520 Assignment 6
Project is located under ---->>>>> Intro to Pygame Graphics > major league soccer animation > graphics_v4.py

__def generate_stars_and_clouds():__
  This code uses list comprehension to create the stars and clouds lists in a more concise way. It also eliminates the need for temporary variables x, y, and r.

__def draw_cloud(x, y):__
  This code stores the ellipse coordinates and dimensions in a list and then iterates over the list to draw each ellipse using a loop. This reduces the number of lines of code from 5 to 2.
 
 __def get_colors(day):__
 	This code defines a function called "get_colors" that takes a parameter "day". Inside the function, it checks if the "day" parameter is truthy (i.e., evaluates to True in a boolean context), and if so, it sets four variables "sky_color", "field_color", "stripe_color", and "cloud_color" to the values of "BLUE", "GREEN", "DAY_GREEN", and "WHITE", respectively. Otherwise, it sets these variables to the values of "DARK_BLUE", "DARK_GREEN", "NIGHT_GREEN", and "NIGHT_GRAY", respectively.
The function then returns a tuple containing these four color values. Finally, the code assigns the values returned by the function to four variables "sky_color", "field_color", "stripe_color", and "cloud_color" using tuple unpacking.
 
__def draw_field_and_stripes(screen, field_color, stripe_color):__
 	This code defines a function called "draw_field_and_stripes" that takes three parameters: "screen", "field_color", and "stripe_color". The function uses the Pygame library to draw a series of rectangles on the "screen" object that represent a field with stripes.
 
__def draw_fence(screen, color):__
 	This code defines a function that draws a fence on a Pygame screen using polygons and lines. The function takes in two parameters: the screen to draw on and the color of the fence. The first loop draws rectangular polygons for the fence, while the second loop draws vertical lines. The third loop draws horizontal lines to complete the fence.
 
__def draw_sun_or_moon(screen, day, sky_color):__
	This code defines a function called "draw_sun_or_moon" that takes three parameters: "screen", "day", and "sky_color". The function uses the Pygame library to draw a sun or moon on the "screen" object depending on the value of the "day" parameter. If day is true then it returns a sun, if it is false it returns a moon. 
 
__goal(length,height,color):__ 
	draws a goal net based on its length, height, and color

__draw_line_goal_box(color):__
	draws the line in front of the goal net based on the provided color
	
__draw_light(x_index):__
	draws the light of the court based on the provided x index


__draw_stand(front_color,back_color):__
	draws the left and right viewer stands based on the provided color

__draw_left_flag(stick_color, flag_color, x, y):__ 
	draws a small flag t that tilted left based on x and y index and its color
	
__draw_right_flag(stick_color, flag_color, x, y):__ 
	draws a small flag t that tilted right based on x and y index and its color





Members:
Natalia Jauregui
Haosi Lin
