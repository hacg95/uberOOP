public class UberX extends Car {
    String brand;
    String model;

    public UberX(Account driver, String license, String brand, String model){
        super(driver, license);
        this.brand = brand;
        this.model = model;
    }
}
