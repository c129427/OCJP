import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class CollectorsEOptionalExample {
    private record Estudante(String nome, String turma) {
    }

    private static String criarAlternativa() {
        System.out.println("Avaliando a expressao alternativa.");
        return "Valor alternativo";
    }

    public static void main(String[] args) {
        System.out.println("=== Collectors e Optional ===");
        List<Estudante> estudantes = List.of(
                new Estudante("Ana", "A"),
                new Estudante("Bruno", "B"),
                new Estudante("Alice", "A"));
        Map<String, List<String>> porTurma = estudantes.stream()
                .collect(Collectors.groupingBy(
                        Estudante::turma,
                        java.util.TreeMap::new,
                        Collectors.mapping(Estudante::nome, Collectors.toList())));
        Optional<Estudante> estudanteInexistente = estudantes.stream()
                .filter(estudante -> estudante.nome().equals("Carla"))
                .findFirst();
        Optional<Estudante> estudanteEncontrada = estudantes.stream()
                .filter(estudante -> estudante.nome().equals("Ana"))
                .findFirst();

        System.out.println("groupingBy + mapping agrupa nomes por turma: " + porTurma);
        System.out.println("Optional vazio usa a alternativa: "
                + estudanteInexistente.map(Estudante::nome).orElse("Estudante nao encontrado"));
        System.out.println("orElse avalia a alternativa mesmo quando o Optional tem valor:");
        String resultadoOrElse = estudanteEncontrada.map(Estudante::nome).orElse(criarAlternativa());
        System.out.println("Resultado de orElse: " + resultadoOrElse);
        String resultadoOrElseGet = estudanteEncontrada.map(Estudante::nome)
                .orElseGet(CollectorsEOptionalExample::criarAlternativa);
        System.out.println("orElseGet so chama o fornecedor quando o Optional esta vazio: "
                + resultadoOrElseGet);
    }
}
