public class TryWithResourcesExample {
    private static class Recurso implements AutoCloseable {
        private final String nome;

        Recurso(String nome) {
            this.nome = nome;
            System.out.println("Abrindo recurso " + nome + ".");
        }

        public void usar() {
            System.out.println("Usando recurso " + nome + ".");
        }

        @Override
        public void close() {
            System.out.println("Fechando recurso " + nome + ".");
        }
    }

    public static void main(String[] args) {
        System.out.println("=== try-with-resources e AutoCloseable ===");
        try (Recurso primeiro = new Recurso("A");
             Recurso segundo = new Recurso("B")) {
            primeiro.usar();
            segundo.usar();
        }
        System.out.println("Os recursos fecham em ordem inversa: B e depois A.");
    }
}
