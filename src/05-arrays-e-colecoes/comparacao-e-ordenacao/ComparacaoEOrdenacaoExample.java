import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ComparacaoEOrdenacaoExample {
    private record Curso(String nome, int duracao) {
    }

    public static void main(String[] args) {
        System.out.println("=== Comparator e ordenacao ===");
        List<Curso> cursos = new ArrayList<>(List.of(
                new Curso("Streams", 4),
                new Curso("POO", 2),
                new Curso("Generics", 4)));
        Comparator<Curso> ordem = Comparator.comparingInt(Curso::duracao)
                .thenComparing(Curso::nome);
        cursos.sort(ordem);

        System.out.println("Ordenacao principal por duracao e desempate pelo nome:");
        cursos.forEach(System.out::println);
        System.out.println("Comparator devolve ordem negativa, zero ou positiva ao comparar dois cursos: "
                + ordem.compare(cursos.get(0), cursos.get(1)));
    }
}
