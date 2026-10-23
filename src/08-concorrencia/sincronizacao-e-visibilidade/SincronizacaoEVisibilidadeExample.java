public class SincronizacaoEVisibilidadeExample {
    private static class Contador {
        private int valor;

        synchronized void incrementar() {
            valor++;
        }

        synchronized int obterValor() {
            return valor;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Sincronizacao, atomicidade e visibilidade ===");
        System.out.println("incrementar() e sincronizado: apenas uma thread acessa o monitor por vez.");
        System.out.println("join() aguarda o fim das tarefas antes de obter o resultado.");
        Contador contador = new Contador();
        Runnable tarefa = () -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementar();
            }
        };
        Thread primeira = new Thread(tarefa);
        Thread segunda = new Thread(tarefa);
        primeira.start();
        segunda.start();
        primeira.join();
        segunda.join();

        System.out.println("Valor final esperado (2 threads x 1000 incrementos): "
                + contador.obterValor());
    }
}
