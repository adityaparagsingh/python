class Animal:
    def __init__(self,name):
        self.name = name
        self.isAlive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
#the Dog,Cat,Mouse class will inherit all the methods and attribute from Animal class
class Dog(Animal): 
    def speak(self):
        print("wooofff")
class Cat(Animal): 
    pass 
class Mouse(Animal): 
    pass 


dog1 = Dog("pippo")
cat1 = Cat("scoop")
rat1 = Mouse("cooper")

print(cat1.name)
print(cat1.isAlive)
dog1.eat()
rat1.sleep()
dog1.speak()