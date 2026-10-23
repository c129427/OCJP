public class CondicionaisESwitchExample {
    public static void main(String[] args) {
        System.out.println("=== Condicionais e expressao switch ===");
        int nota = args.length == 0 ? 8 : Integer.parseInt(args[0]);
        if (nota < 0 || nota > 10) {
            System.out.println("Nota invalida: informe um valor entre 0 e 10.");
            return;
        }

        String resultado = switch (nota) {
            case 9, 10 -> "Excelente";
            case 7, 8 -> "Aprovado";
            case 5, 6 -> "Recuperacao";
            default -> "Reprovado";
        };

        System.out.println("if validou a faixa da nota: " + nota + " de 10.");
        System.out.println("switch selecionou a classificacao: " + resultado);
        System.out.println("Execute com um argumento, por exemplo: java CondicionaisESwitchExample 6");
    }
}
