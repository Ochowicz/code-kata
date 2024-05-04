# This series of katas will introduce you to basics of doing geometry with computers.
#
# Write the function circleArea/CircleArea which takes in a Circle object and calculates the area of that circle.
import math
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
def circle_area(circle):
    return math.pi * circle.radius**2