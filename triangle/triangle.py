
# import sys
# sys.path.append("/home/shreyanshu/Videos/Triangles_python_lib/")
import os
print(os.getcwd())
from triangle_exceptions import *


class Triangle:

    def __init__(self, sides=None, angles=None):
        if sides or angles:
            self.sides = sides
            self.angles = angles
            sides.sort()
            if sum(sides[0:2]) < sides[2]:
                raise NotAValidTriangleError
        else:
            raise NotProvidedSidesOrAnglesError


if __name__ == "__main__":
    ob = Triangle(sides=[1,10,12])

    pass
