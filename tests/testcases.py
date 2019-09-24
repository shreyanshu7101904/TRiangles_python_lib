import os
os.chdir("../")
print(os.getcwd())
from triangle.triangle import Triangle


if __name__ == "__main__":
    ob = Triangle(sides=[1,10,12])

    pass