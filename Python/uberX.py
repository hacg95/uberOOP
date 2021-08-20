from car import Car

class UberX(Car):
    brand = str
    model = str

    def __init__(self, driver, license, passenger, brand, model):
        super().__init__(driver, license, passenger)
        self.brand = brand
        self.model = model