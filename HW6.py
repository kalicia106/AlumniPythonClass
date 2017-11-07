#Homework 6
#Part 1: Create a class called shapes.  The properties should be sides.
#It should have the methods: perimeter, area.  Create 4 instances of the class.
#Print out each attribute of the instances and use each method in the class.

import math

class Shapes():
    def __init__(self, l, w, s):
        self.length = l
        self.width = w
        self.sides = s

    def ret_area(self, l, w):
        area = (l* w)
        return area
        print(ret_area (8, 2))

    def ret_perimeter(self, l, w):
        perimeter = (2*l + 2*w)
        return perimeter
        print(ret_perimeter(8, 2))

    def square_area(self, s):
        area = (s * s)
        return area
        print(square_area(5))

    def square_perimeter(self, s):
        perimeter = (4 * s)
        return perimeter
        print(square_perimeter(9))


NewShape = Shapes(8, 2, 5)
print(NewShape.ret_area(8, 2))
print(NewShape.ret_perimeter(8, 2))
print(NewShape.square_area(5))
print(NewShape.square_perimeter(9))
