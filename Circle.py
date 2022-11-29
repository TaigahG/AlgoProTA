from math import pi
class Circle:
    def __init__(self,radius : float = 5.0, color = "red"):
        self.radius = radius
        self.color = color
    def setRadius(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def getArea(self):
        return pi * self.radius * self.radius
    def toString(self):
        print("radius: ", str(self.getRadius()))
        print("color: ", self.getColor())

