from abc import ABC,abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side**2
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base/2)*self.height
    
shapes = [Circle(10),Rectangle(5),Triangle(5,10)]

for shape in shapes:
    print(f"{shape.area()}cm²")