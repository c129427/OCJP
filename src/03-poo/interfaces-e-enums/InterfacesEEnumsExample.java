public class InterfacesEEnumsExample {
    private interface Saudavel {
        default String saudar() {
            return "Ola";
        }

        static String idioma() {
            return "portugues";
        }
    }

    private enum Nivel {
        INICIANTE(1),
        INTERMEDIARIO(2),
        AVANCADO(3);

        private final int etapa;

        Nivel(int etapa) {
            this.etapa = etapa;
        }

        int getEtapa() {
            return etapa;
        }
    }

    private static class Estudante implements Saudavel {
    }

    public static void main(String[] args) {
        System.out.println("=== Interfaces e enums ===");
        System.out.println("Estudante herda o metodo default da interface Saudavel.");
        Estudante estudante = new Estudante();
        Nivel nivel = Nivel.INTERMEDIARIO;
        System.out.println("Saudacao fornecida pela interface: " + estudante.saudar());
        System.out.println("Metodo static da interface: " + Saudavel.idioma());
        System.out.println("Enum " + nivel + " armazena a etapa " + nivel.getEtapa() + ".");
        System.out.println("values() lista todas as constantes: "
                + java.util.Arrays.toString(Nivel.values()));
    }
}
