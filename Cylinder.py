from Circle import  Circle
from math import pi
class Cylinder(Circle):
    def __init__(self, radius, color, height = 1.0 ):
        super().__init__(radius, color)
        self.height = height

    def setHeight(self, height):
        self.__height = height
    def getHeight(self):
        return self.height
    def toString(self):
        print("height: ", str(self.getHeight()))
        print("radius: ", str(self.getRadius()))
        print("color: ", self.getColor())
    def getVolume(self):
        return self.getArea()*self.getHeight()
