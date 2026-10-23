import java.util.ArrayList;
import java.util.List;

public class GenericsExample {
    private static <T> void copiar(List<? extends T> origem, List<? super T> destino) {
        for (T valor : origem) {
            destino.add(valor);
        }
    }

    private static double somar(List<? extends Number> valores) {
        double soma = 0;
        for (Number valor : valores) {
            soma += valor.doubleValue();
        }
        return soma;
    }

    public static void main(String[] args) {
        System.out.println("=== Generics e wildcards ===");
        System.out.println("? extends Number permite ler elementos como Number.");
        List<Integer> notas = new ArrayList<>(List.of(8, 9, 10));
        List<Number> resultados = new ArrayList<>();
        copiar(notas, resultados);

        System.out.println("Soma de List<Integer> recebida como List<? extends Number>: "
                + somar(notas));
        System.out.println("Copiando de List<? extends Integer> para List<? super Integer>: "
                + resultados);
    }
}
