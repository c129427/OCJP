import java.util.List;

public class StreamsEPipelinesExample {
    public static void main(String[] args) {
        System.out.println("=== Streams: pipeline de operacoes ===");
        List<String> linguagens = List.of("Java", "Kotlin", "Java", "C", "JavaScript");
        List<String> resultado = linguagens.stream()
                .filter(linguagem -> linguagem.length() > 1)
                .distinct()
                .sorted()
                .toList();
        int somaDosPares = List.of(1, 2, 3, 4, 5, 6).stream()
                .filter(numero -> numero % 2 == 0)
                .mapToInt(Integer::intValue)
                .sum();

        System.out.println("Fonte original (nao e alterada pelo stream): " + linguagens);
        System.out.println("filter + distinct + sorted + toList: " + resultado);
        System.out.println("Stream.toList() devolve uma lista nao modificavel.");
        System.out.println("Pipeline primitivo filter + mapToInt + sum: " + somaDosPares);
    }
}
