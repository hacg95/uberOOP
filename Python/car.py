from account import Account

class Car: 
    id = int
    license = str
    driver = Account("","")
    passenger = int

    def __init__(self, driver, license, passenger):
        self.driver = driver
        self.license = license
        self.passenger = passenger