#this program contains functions that evalutate formulas used in geometry.
#
#jordan houle
#december 3, 2015

import math

#  the math module has constants
print(math.pi)
print(math.e)

#the math module also has built in functions
print(math.sqrt(3))
print(math.sin(0.5))


def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def cylinder_surface_area(r,h):
    sa=(2*math.pi*r*h) + (2*math.pi*r**2)
    return sa
#function calls
print("cylinder")
print(cylinder_surface_area(4,10))

def parallelogram_area(b, h):
    a = b * h
    return a

#function calls
print(parallelogram_area(5, 6))

def trapezoid_area(a, b, h):
    a = ((a+b)/2) * h
    return a

#funtion calls
print("trapezoid area")
print(trapezoid_area(12, 6, 5))

def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v

#function calls
print(rectangular_prism_volume(5, 5, 6))

def cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v

#function calls
print(cone_volume(3, 9))

def sphere_volume(r):
    v = (4/3)*math.pi*r**3
    return v

#function calls
print(sphere_volume(6))

def rectangular_prism_surface_area(w, l, h):
    sa = 2 * ((w*l) + (h*l) + (h*w))
    return sa

#function calls
print("rectangular prism surface area")
print(rectangular_prism_surface_area(5,5,6))

def sphere_surface_area(r):
    sa = 4 * math.pi * r**2
    return sa

#function calls
print("sphere surface area")
print(sphere_surface_area(6))

def hypotenuse_right_triangle(a, b):
    c2 = a**2 + b**2
    c = math.sqrt(c2)
    return c

#function calls
print("Hypotenuse")
print(hypotenuse_right_triangle(3, 4))

def herons_formula(a, b, c):
    p= (a+b+c)/2
    a = math.sqrt( p * (p-a) * (p-b) * (p-c) )
    return a

#function calls
print(herons_formula(5, 10, 15))

def rate_of_change (p, r, t):
    a = p * (1 + r)**t
    return a

#function calls
print (rate_of_change(1000, 0.07, 30))





