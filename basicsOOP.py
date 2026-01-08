# from all_Classes import Car

class Car:

    brand ="Ford"     #class variables

    def __init__(self,model,year,color,forSale):    #constructer
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale

    def drive(self):    #methods in python
        print(f"you are driving {self.model}")

    def stop(self):
        print(f"you stopped the {self.model}")

car1 = Car("shelby GT ",2012,"red","yes")  
car2 = Car("GT",2010,"black","no")

#print(car1.brand)  #always access the class variable using Class name not Object Name
print(Car.brand)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.forSale)
print()
print(car2.brand)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.forSale)

car2.drive()
car1.stop()