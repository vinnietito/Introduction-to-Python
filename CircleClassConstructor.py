import math

class Circle:
    def __init__(self, r):
        self.radius = r
        
    def calArea(self):
        return math.pi * pow(self.radius, 2)
    
    
# Main program
aCircle = Circle(7)
bCircle = Circle(14)

areaA = aCircle.calArea()
areaB = bCircle.calArea()

print("Area of the circle A is:\t", areaB)
print("Area of circle B is:\t", areaB)