class Shape:
    def __init__(self,color,isFilled):
        self.color = color
        self.isFilled = isFilled

    def specs(self):
        print(f"the shape is {self.color} in color and it is {'filled' if self.isFilled else 'not filled'}")

#Constructor case of Super function
class Circle(Shape):
    def __init__(self,color,radius,isFilled):
        self.radius = radius
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color,isFilled)

    def specs(self):
        print(f"the shape is circle in and its area is {3.14*self.radius*self.radius}")
        super().specs()

class Rectangle(Shape):
    def __init__(self,color,side,isFilled):
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color,isFilled)
        self.side = side
    
    def specs(self):
        print(f"the shape is square in and its side is {self.side}")
    
        
class Triangle(Shape):
    def __init__(self,color,width,isFilled,height):
        # self.color = color
        # self.isFilled = isFilled
        super().__init__(color,isFilled)
        self.width = width
        self.height = height
        
#some attributes are common and repeating in all the class constructors like color,isFilled

circle = Circle("red",10,True)
rectangle = Rectangle("blue",5,False)
triangle = Triangle("yellow",3,True,4)

print(circle.color,circle.isFilled,circle.radius)
circle.specs() #both child and parent(using super) specs method is invoked at same time
rectangle.specs() #child class spec is used due to method overrrrrriding
triangle.specs()   #parent class spec is used