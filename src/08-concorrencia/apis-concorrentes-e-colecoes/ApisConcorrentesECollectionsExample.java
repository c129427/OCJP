import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class ApisConcorrentesECollectionsExample {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Colecoes concorrentes e tipos atomicos ===");
        System.out.println("computeIfAbsent cria um contador por chave; incrementAndGet e atomico.");
        ConcurrentHashMap<String, AtomicInteger> acessos = new ConcurrentHashMap<>();
        ExecutorService executor = Executors.newFixedThreadPool(4);
        List<Runnable> tarefas = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            tarefas.add(() ->
                    acessos.computeIfAbsent("Java", chave -> new AtomicInteger()).incrementAndGet());
        }

        try {
            for (Runnable tarefa : tarefas) {
                executor.submit(tarefa);
            }
        } finally {
            executor.shutdown();
            if (!executor.awaitTermination(5, java.util.concurrent.TimeUnit.SECONDS)) {
                executor.shutdownNow();
                throw new IllegalStateException("As tarefas nao terminaram dentro do limite.");
            }
        }

        System.out.println("Contagem esperada apos 1000 tarefas concorrentes: "
                + acessos.get("Java").get());
    }
}
