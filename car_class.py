#Car class with Name, type and model of car
class Car(object):
condition = "new"
def __init__(self, type, model, name):
    self.model = model
    self.type = color
    self.name = name

def displayCar(self):
    print "This is a %s %s with %r MPG." %(self.model,self.type,self.name)

def driveCar(self):
    self.condition = "used"

class ElectricCar(Car): 
    def __init__(self, type, model, name):
        self.model = model
    self.type = color
    self.name = name

myCar = ElectricCar("prius","black",55,"molten salt")