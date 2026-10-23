public class ConstrutoresEInicializacaoExample {
    private static class Pessoa {
        private static int quantidadeCriada;
        private final String nome;
        private final int numero;

        Pessoa() {
            this("Estudante");
        }

        Pessoa(String nome) {
            this.nome = nome;
            this.numero = ++quantidadeCriada;
        }
    }

    public static void main(String[] args) {
        System.out.println("=== Construtores e inicializacao ===");
        System.out.println("O construtor sem argumentos delega para Pessoa(String) usando this(...).");
        Pessoa pessoaPadrao = new Pessoa();
        Pessoa pessoaNomeada = new Pessoa("Maria");
        System.out.println("Construtor padrao: nome=" + pessoaPadrao.nome + ", numero=" + pessoaPadrao.numero);
        System.out.println("Construtor com argumento: nome=" + pessoaNomeada.nome
                + ", numero=" + pessoaNomeada.numero);
        System.out.println("Campo static compartilhado: " + Pessoa.quantidadeCriada + " objetos criados.");
    }
}
