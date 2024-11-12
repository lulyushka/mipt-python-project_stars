import tkinter as tk
import math 

class Latitude:

    def __init__(self, value):
        self.value = value

    def check(self):
        try:
            val = float(self.value)
            return -90 <= val <= 90
        except(TypeError, ValueError):
            return False
        
class Angle():

    def __init__(self, value):
        self.value = value

    def sin(self):
        return math.sin(math.radians(self.value))
    
    def cos(self):
        return math.cos(math.radians(self.value))

class sphericalCoordinates():
    
    def __init__(self, coordlist):
        self.alpha = Angle(coordlist[0])
        self.theta = Angle(coordlist[1])

    def toCartesian(self):
        return [self.theta.sin()*self.alpha.cos(), self.theta.sin()*self.alpha.sin(), self.theta.cos()]
    
class cartesianCoordinates():

    def __init__(self, coordlist):
        self.x = coordlist[0]
        self.y = coordlist[1]
        self.z = coordlist[2]

    def spinZ (self, angle):
        angle = Angle(angle)
        newx = self.x*angle.cos() + self.y * angle.sin()
        newy = self.y * angle.cos() - self.x * angle.sin()
        self.x = newx
        self.y = newy
    
    def spinY (self, angle):
        angle = Angle(angle)
        saved_x =self.x
        newx = self.x*angle.cos() - self.z * angle.sin()
        newz = self.x * angle.sin() + self.z * angle.cos()
        self.x = newx
        self.z = newz

    def toSpherical(self):
        return [math.acos(self.z), self.y/(self.x**2 + self.y**2)**0.5, self.x/(self.x**2 + self.y**2)**0.5]
    