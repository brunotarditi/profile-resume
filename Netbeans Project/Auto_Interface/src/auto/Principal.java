package auto;

/**
 *
 * @author Bruno Tarditi
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        Auto auto = new Auto();
        auto.avanzar();
        auto.detener();
        
        Bicicleta bici = new Bicicleta();
        bici.avanzar();
        bici.detener();
        System.out.print("En la bicicleta ");
        bici.sentarse();

    }
    
}
