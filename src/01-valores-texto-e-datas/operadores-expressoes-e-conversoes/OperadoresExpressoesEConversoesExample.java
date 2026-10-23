public class OperadoresExpressoesEConversoesExample {
    public static void main(String[] args) {
        System.out.println("=== Operadores, expressoes e conversoes ===");

        int divisaoInteira = 7 / 2;
        double divisaoDecimal = 7 / 2.0;
        int conversaoComPerda = (int) 9.8;
        int contador = 0;
        boolean resultadoCurtoCircuito = false && ++contador > 0;
        int contadorAposCurtoCircuito = contador;
        boolean resultadoSemCurtoCircuito = false & ++contador > 0;

        System.out.println("7 / 2: " + divisaoInteira + " (divisao entre inteiros descarta a fracao).");
        System.out.println("7 / 2.0: " + divisaoDecimal + " (double promove a expressao).");
        System.out.println("(int) 9.8: " + conversaoComPerda + " (cast remove a parte fracionaria).");
        System.out.println("false && ...: " + resultadoCurtoCircuito
                + "; contador continua " + contadorAposCurtoCircuito
                + " porque && nao avaliou o incremento.");
        System.out.println("false & ...: " + resultadoSemCurtoCircuito
                + "; o incremento foi avaliado e contador agora vale " + contador + ".");
    }
}
