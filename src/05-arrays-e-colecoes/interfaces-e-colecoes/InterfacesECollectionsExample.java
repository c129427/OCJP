import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class InterfacesECollectionsExample {
    public static void main(String[] args) {
        System.out.println("=== Collections Framework: List, Set e Map ===");
        System.out.println("List preserva ordem e aceita duplicatas; Set elimina duplicatas.");
        System.out.println("LinkedHashSet e LinkedHashMap mantem a ordem de insercao.");
        List<String> assuntos = new ArrayList<>();
        assuntos.add("Generics");
        assuntos.add("Streams");
        assuntos.add("Generics");

        Set<String> assuntosUnicos = new LinkedHashSet<>(assuntos);
        Map<String, Integer> modulos = new LinkedHashMap<>();
        modulos.put("Generics", 5);
        modulos.put("Streams", 6);

        System.out.println("List: " + assuntos);
        System.out.println("Set criado a partir da lista: " + assuntosUnicos);
        System.out.println("Map associa assunto a modulo: " + modulos);
        System.out.println("Consulta por chave, Streams: " + modulos.get("Streams"));
    }
}
