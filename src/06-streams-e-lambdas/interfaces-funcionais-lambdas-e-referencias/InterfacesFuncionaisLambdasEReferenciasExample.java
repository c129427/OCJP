import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;

public class InterfacesFuncionaisLambdasEReferenciasExample {
    public static void main(String[] args) {
        System.out.println("=== Interfaces funcionais, lambda e method reference ===");
        System.out.println("Predicate testa, Function transforma e Consumer consome cada valor.");
        Predicate<String> comecaComJ = texto -> texto.startsWith("J");
        Function<String, Integer> obterTamanho = String::length;
        List<String> linguagens = List.of("Java", "Kotlin", "JavaScript");

        linguagens.stream()
                .filter(comecaComJ)
                .forEach(linguagem -> System.out.println(
                        linguagem + " tem " + obterTamanho.apply(linguagem) + " caracteres."));
    }
}
