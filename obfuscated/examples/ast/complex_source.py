class Vehicle(object):
    """
    The Vehicle class
    """
    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the Vehicle
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the Vehicle
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)


class Car(Vehicle):
    """
    The Car class
    """
    def brake(self):
        """
        Stop the Car
        """
        return "The car class is breaking slowly!"


if __name__ == "__main__":
    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
    car = Car("yellow", 2, 4, "car")
    print(car.brake())
    print(car.drive())
