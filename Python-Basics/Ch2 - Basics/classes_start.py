#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, maxspeed):
        self.mode = "driving"
        self.maxspeed = maxspeed

class Car(Vehicle):
    def __init__(self, engine):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 5
        self.engine = engine
    def drive(self, maxspeed):
        super().drive(maxspeed)
        print("This Car drives up to ", self.maxspeed, "/kph whith its ", self.engine, "engine")

class Motorcycle(Vehicle):
    def __init__(self, engine, sidecar):
        super().__init__("Motorcycle")
        if (sidecar):
            self.wheels = 4
        else:
            self.wheels = 2
        self.doors = 0
        self.engine = engine
    def drive(self, maxspeed):
        super().drive(maxspeed)
        print("This Motorcycle drives up to ", self.maxspeed, "/kph whith its ", self.engine, "engine")

car1 = Car("gas")
car2 = Car("diesel")
car3 = Car("eletric")
mc1 = Motorcycle("gas", False)

print (mc1.wheels)
print(car1.engine)
print(car2.engine)

car1.drive(220)
car2.drive(250)
mc1.drive(160)