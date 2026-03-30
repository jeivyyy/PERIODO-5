
import java.util.LinkedList;
import java.util.Queue;

// Escreva um pequeno código em Java que:
// - Crie uma Queue;
// - Insira três elementos;
// - Remova e imprima o primeiro elemento.
public class Teste {

    public static void main(String[] args) {

        Queue<String> fila = new LinkedList<>();
        fila.add("João Vitor");
        fila.add("Domenique Joli");
        fila.add("Asaffe Ayron");

        System.out.println(fila);
        System.out.println(fila.remove());
    }
}
