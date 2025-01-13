#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
  def __init__(self, bodystyle): # think of init as kinda like a constructor but not really, you still use it to assign values and do other operations when the object is being created
    self.bodystyle = bodystyle # self is the created object itself
  
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle): # means it's inheriting from the Vehicle class
  def __init__(self, enginetype):
    super().__init__("Car") # we are setting the bodystyle variable from the parent class to the value "Car"
    self.wheels = 4
    self.doors = 4
    self.enginetype = enginetype
  
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.enginetype = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)