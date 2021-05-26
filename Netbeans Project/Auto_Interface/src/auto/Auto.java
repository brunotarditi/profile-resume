package auto;

/**
 *
 * @author Bruno Tarditi
 */
public class Auto implements Rueda {

    public Auto() {

    }

    @Override
    public void avanzar() {
        System.out.println("El auto avanza.");
    }

    @Override
    public void detener() {
        System.out.println("El auto se detiene");
    }

}
