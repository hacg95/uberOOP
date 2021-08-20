public class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passenger;

    public Car(Account driver, String license){
        this.license = license;
        this.driver = driver;
    }

    public void setPassenger(Integer passenger){
        if(passenger == 4){
            this.passenger = passenger;
        }else{
            System.out.println("You need 4 available seats");
        }
    }

    public Integer getPassenger(){
        return passenger;
    }

    void printDataCar () {
        System.out.println("Driver: " + driver.name + " Document: " + driver.document +" License: " + license + " passenger: " + passenger);
    }
}
