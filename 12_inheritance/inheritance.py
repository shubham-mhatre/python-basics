
class Vehicle:
    def __init__(self):
        print("i am vehicle")

    def general_usage(self):
        print("general use for transportation")

class Car(Vehicle):
    def __init__(self):
        print("i am Car")
        self.wheels=4
        self.has_roof=True

    def special_usage(self):
        print("special use to commute to office, vacation with family")


class Bike(Vehicle):
    def __init__(self):
        print("i am bike")
        self.wheels = 2
        self.has_roof = False

    def special_usage(self):
        print("special use for riding and race")

c=Car()
print("no of wheels : ", c.wheels, " : has roof : " ,c.has_roof)
c.general_usage()
c.special_usage()
print("check if c is instance of Car : isinstance(c,Car)", isinstance(c,Car))
print("check if Car is subclass of Vehicle : issubclass(Car,Vehicle) : ",issubclass(Car,Vehicle))


b=Bike()
print("no of wheels : ", b.wheels, " : has roof : " ,b.has_roof)
b.general_usage()
b.special_usage()
print("check if b is instance of Bike : isinstance(b,Bike)", isinstance(b,Bike))
print("check if Bike is subclass of Vehicle : issubclass(Bike,Vehicle) : ",issubclass(Bike,Vehicle))

