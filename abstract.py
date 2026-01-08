from abc import ABC,abstractmethod

class Vehicle:
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car is Running")
    def stop(self):
        print("Car is Stopped")


car1 = Car()
car1.go()
car1.stop()