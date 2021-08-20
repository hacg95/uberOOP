from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, driver, license, passenger, typeCarAccepted, seatsMaterial):
        super().__init__(driver, license, passenger)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial