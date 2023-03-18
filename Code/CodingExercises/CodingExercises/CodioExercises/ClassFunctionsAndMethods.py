'''Exercise to print the distance betwwen 2 points
Simon Bolder - Postgraduate Certificate in Computer Science 2023
ePortfolio - https://sbolder77.github.io/eportfolio/'''

import math
import copy

#region classes

class Point:
    '''Represents a start point and endpoint'''
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Rectangle():   
    def __init__(self):
        self.width = 0
        self.height = 0
        self.corner = (0.0, 0.0)

#endregion

#region functions

def print_point(p):
    print('Distance between 2 points - ' + str(p.y - p.x))
    print('Point values - (%g, %g)' % (p.x, p.y))
    distance = math.sqrt(p.x**2 + p.y**2)
    print('Square root - ' + str(distance))

def find_center(rect):
    _p = Point()
    _p.x = rect.corner.x + rect.width/2
    _p.y = rect.corner.y + rect.height/2
    return _p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    print(str(rect.width) + " - " + str(rect.height))

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    print(str(rect.corner.x) + " - " + str(rect.corner.y))

def copy_rectangle(rect):
    _rect1 = copy.deepcopy(rect)
    return _rect1

#endregion

_points = Point()
_points.x = 3.0
_points.y = 4.0

print_point(_points)

_width = 100.0
_height = 200.0
_corner_x = 0.0
_corner_y = 0.0

_box = Rectangle()
_box.width = _width
_box.height = _height
_box.corner = Point()
_box.corner.x = _corner_x
_box.corner.y = _corner_y

_centre = find_center(_box)
print_point(_centre)

grow_rectangle(_box,50,100)

move_rectangle(_box,3,20)

_box2 = copy_rectangle(_box)
print(_box2)


#TODO
#Exercises
#Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.
#Instantiate a Circle object that represents a circle with its center at   (150,100)
#  and radius 75.
#Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
#Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.
#Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.
#TRY IT
#Remove any printing from your code and then add the following to the end:

#def main():
#    box = Rectangle()
#    box.width = 100.0
#    box.height = 200.0
#    box.corner = Point()
#    box.corner.x = 50.0
#    box.corner.y = 50.0

#    circle = Circle
#    circle.center = Point()
#    circle.center.x = 150.0
#    circle.center.y = 100.0
#    circle.radius = 75.0

#    print(point_in_circle(box.corner, circle))
#    print(rect_in_circle(box, circle))
#    print(rect_circle_overlap(box, circle))


#if __name__ == '__main__':
#    main()
#Then, submit your code using the button below:

#Write a function called draw_rect that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.
#Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle.
#Solution: http://thinkpython2.com/code/draw.py.
