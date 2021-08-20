import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends Car {
    Map<String, ArrayList<Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberBlack(Account driver, String license, 
    Map<String, ArrayList<Integer>> typeCarAccepted,
    ArrayList<String> seatsMaterial){
        super(driver, license);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}
