class Wheel:
    def __init__(self,wheelSize):
        self.wheelSize = wheelSize
    
class Engine:
    def __init__(self,horsePower):
        self.horsePower = horsePower

class Car:
    def __init__(self,year,model,horsePower,wheel_size):
        self.year = year
        self.model = model  
        self.engine = Engine(horsePower)  #composition
        self.wheels = [Wheel(wheel_size) for i in range(4)]  #4 wheels in car

    def showDetails(self):
        print(f"Car Model = {self.model} \nCar Year = {self.year} \nHorse Power = {self.engine.horsePower} \nWheel Size = {self.wheels[0].wheelSize}\n")
#Car object  owns engine obj and wheelSixe objs
car1 = Car(2020,"Golf GT", 500,16)
car2 = Car(2022,"BMW M3 Competition", 600,17)
car1.showDetails()
car2.showDetails()