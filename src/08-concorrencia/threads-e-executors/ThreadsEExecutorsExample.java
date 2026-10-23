import java.util.concurrent.ExecutorService;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class ThreadsEExecutorsExample {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        System.out.println("=== Threads, Callable, Future e ExecutorService ===");
        ExecutorService executor = Executors.newFixedThreadPool(2);
        try {
            Future<Integer> primeiraTarefa = executor.submit(() -> {
                System.out.println("Callable executada em " + Thread.currentThread().getName());
                return 20;
            });
            Future<Integer> segundaTarefa = executor.submit(() -> 22);
            int primeiroResultado = primeiraTarefa.get();
            int segundoResultado = segundaTarefa.get();
            System.out.println("Future.get() espera e devolve o resultado: "
                    + primeiroResultado + " + " + segundoResultado + " = "
                    + (primeiroResultado + segundoResultado));
        } finally {
            executor.shutdown();
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        }
    }
}
