# Created vehicle class
class Vehicle:
    make = 'NA'
    model = 'NA'
    year = 0

# Created child class inheriting from Vehicle
class Motorcycle(Vehicle):
    offRoad = False
    streetLegal = False

# Created child class inheriting from Vehicle
class Truck(Vehicle):
    bedLength = "0ft"
    4WheelDrive = False
    
    
