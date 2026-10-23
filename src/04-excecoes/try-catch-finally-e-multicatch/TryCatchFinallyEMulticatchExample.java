public class TryCatchFinallyEMulticatchExample {
    public static void main(String[] args) {
        System.out.println("=== try, multi-catch e finally ===");
        String argumento = args.length == 0 ? "0" : args[0];
        System.out.println("Informe o divisor como argumento para testar; padrao atual: " + argumento);
        try {
            int divisor = Integer.parseInt(argumento);
            System.out.println("10 dividido pelo argumento: " + (10 / divisor));
        } catch (ArithmeticException | NumberFormatException excecao) {
            System.out.println("multi-catch capturou: " + excecao.getClass().getSimpleName());
        } finally {
            System.out.println("finally executa tanto no sucesso quanto apos uma excecao.");
        }
        System.out.println("Execucao continua depois do bloco try-catch-finally.");
    }
}
