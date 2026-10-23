public class ClassesObjetosEEncapsulamentoExample {
    private static class Conta {
        private double saldo;

        public void depositar(double valor) {
            if (valor > 0) {
                saldo += valor;
            } else {
                System.out.println("Deposito recusado: o valor precisa ser positivo.");
            }
        }

        public double consultarSaldo() {
            return saldo;
        }
    }

    public static void main(String[] args) {
        System.out.println("=== Classes, objetos e encapsulamento ===");
        System.out.println("Cada Conta tem seu proprio estado; saldo so muda pelo metodo depositar().");
        Conta contaPrincipal = new Conta();
        Conta contaReserva = new Conta();
        contaPrincipal.depositar(50.0);
        contaPrincipal.depositar(-10.0);
        contaReserva.depositar(20.0);

        System.out.println("Saldo da conta principal: " + contaPrincipal.consultarSaldo());
        System.out.println("Saldo independente da conta reserva: " + contaReserva.consultarSaldo());
    }
}
