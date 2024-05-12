# Given two points P and Q, output the symmetric point of point P about Q. Each argument is a two-element array of integers representing the point's X and Y coordinates. Output should be in the same format, giving the X and Y coordinates of point P1. You do not have to validate the input.
def symmetric_point(p, q):
    return [q[0] + (q[0] - p[0]), q[1] + (q[1] - p[1])]