# TREASURE
# Jaekyoung Kim (rlakim5521@naver.com)

import math
from PIL.GimpGradientFile import EPSILON

PI = 2.0 * math.acos(0.0)

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + " " + str(self.y)
    
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    
    def __lt__(self, rhs):
        if self.x != rhs.x:
            return self.x < rhs.x
        else:
            return self.y < rhs.y
    
    def __add__(self, rhs):
        return vector(self.x + rhs.x, self.y + rhs.y)
    
    def __sub__(self, rhs):
        return vector(self.x - rhs.x, self.y - rhs.y)
    
    def __mul__(self, rhs):
        return vector(self.x * rhs, self.y * rhs)
    
    # Returns a length of vector.
    def norm(self):
        return math.hypot(self.x, self.y)
    
    # Returns an unit vector which has a same direction.
    def normalize(self):
        return vector(self.x / self.norm(), self.y / self.norm())
    
    def polar(self):
        return math.fmod(math.atan2(self.y, self.x) + 2 * PI, 2 * PI)
    
    # Inner product
    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y
    
    # Cross product
    def cross(self, rhs):
        return self.x * rhs.y - rhs.x * self.y
    
    # what???
    def project(self, rhs):
        r = rhs.normalize()
        return r * r.dot(self)

# Returns a result of cross product of vector a and vector b.
# If vector b is laid on a counterclockwise direction of vector a from the starting point,
# returns a positive number.
# If vector b is laid on a clockwise direction of vector a from the starting point,
# returns a negative number.
# If vector a and vector b are parallel, returns 0.
def ccw2(a, b):
    return a.cross(b)

# Returns a result of cross product of vector a and vector b.
# If vector b is laid on a counterclockwise direction of vector a from vector p,
# returns a positive number.
# If vector b is laid on a clockwise direction of vector a from vector p,
# returns a negative number.
# If vector a and vector b are parallel, returns 0.
def ccw3(p, a, b):
    return ccw2(a-p, b-p)

# Returns an intersection point of two lines which a line including vector a and vector b
# and a line including vector c and vector d.
# If two lines are parallel, returns an vector of (-1,-1).
def lineIntersection(a, b, c, d):
    det = (b - a).cross(d - c)
    if(math.fabs(det) < EPSILON): return vector(-1,-1)
    return a + (b - a) * ((c - a).cross(d - c) / det)

# Returns an area of an simple polygon.
def area(vectors):
    ret = 0.0
    length = len(vectors)
    for i in xrange(length):
        j = (i+1) % length
        ret += vectors[i].x * vectors[j].y - vectors[j].x * vectors[i].y
    return math.fabs(ret) / 2.0

# If point is inside of islands, returns true.
# Else, returns false.
def isInside(point, islands):
    crosses = 0
    length = len(islands)
    for i in xrange(length):
        j = (i+1) % length
        if((islands[i].y > point.y) != (islands[j].y > point.y)):
            atX = (islands[j].x - islands[i].x) * (point.y - islands[i].y) / (islands[j].y - islands[i].y) + islands[i].x
            if(point.x < atX):
                crosses += 1
    return crosses % 2 > 0

# After cutting a polygon by a line including vector a and vector b,
# returns the left parts of the line.
def cutPoly(p, a, b):
    n = len(p)
    inside = []
    for i in xrange(n):
        inside.append(ccw3(a, b, p[i]) >= 0)
    ret = []
    for i in xrange(n):
        j = (i+1) % n
        if(inside[i]): ret.append(p[i])
        if(inside[i] != inside[j]):
            cross = lineIntersection(p[i], p[j], a, b)
            ret.append(cross)
    return ret

# An polygon clipping using an Sutherland-Hodgman algorithm.
def intersection(p, x1, y1, x2, y2):
    a = vector(x1, y1)
    b = vector(x2, y1)
    c = vector(x2, y2)
    d = vector(x1, y2)
    ret = cutPoly(p, a, b)
    ret = cutPoly(ret, b, c)
    ret = cutPoly(ret, c, d)
    ret = cutPoly(ret, d, a)
    return ret      

# Main function
if __name__ == "__main__":
    for _ in xrange(input()):
        # Input
        x1, y1, x2, y2, N = map(float, raw_input().split())
        islands = []
        for _ in xrange(int(N)):
            xi, yi = map(float, raw_input().split())
            islands.append(vector(xi,yi))
            
        # Solve
        rectangles = [vector(x1,y2),vector(x1,y1),vector(x2,y1),vector(x2,y2)]
        investgateds = intersection(islands, x1, y1, x2, y2)
        
        # Output
        print area(investgateds)
