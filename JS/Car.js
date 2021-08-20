class Car {
    constructor(driver, license, passenger) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger = passenger;
    }

    printDataCar() {
    console.log(this.driver);
    console.log(this.driver.name);
    console.log(this.driver.document);
    console.log(this.license);
    console.log(this.passenger);
    }
}