public class RecordsSealedEPatternMatchingExample {
    private sealed interface Forma permits Circulo, Retangulo {
    }

    private record Circulo(double raio) implements Forma {
    }

    private record Retangulo(double largura, double altura) implements Forma {
    }

    public static void main(String[] args) {
        System.out.println("=== Records, sealed e pattern matching ===");
        System.out.println("Forma so pode ser implementada pelas classes declaradas em permits.");
        Forma[] formas = {new Circulo(3.0), new Retangulo(4.0, 5.0)};
        for (Forma forma : formas) {
            if (forma instanceof Circulo circulo) {
                System.out.println("Record Circulo: raio=" + circulo.raio()
                        + ", equals compara componentes: "
                        + circulo.equals(new Circulo(circulo.raio())));
            } else if (forma instanceof Retangulo retangulo) {
                System.out.println("Record Retangulo: largura=" + retangulo.largura()
                        + ", altura=" + retangulo.altura());
            }
        }
    }
}
