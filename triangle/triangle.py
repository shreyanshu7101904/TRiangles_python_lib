
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



