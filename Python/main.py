from car import Car
from uberX import UberX
from uberBlack import UberBlack
from account import Account

def run():
    car = UberX(Account("Harold", "1093782789"), "HUX69E", 4, "Hyundai", "Veloster")
    print(vars(car))
    print(vars(car.driver))

if __name__ == "__main__":
    run()