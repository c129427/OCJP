# APIs concorrentes e coleções

## Estude

- `Lock`, `ReentrantLock`, `lock`, `unlock` e liberação segura em `finally`.
- `AtomicInteger` e outras classes atômicas para atualizações simples.
- Coleções concorrentes, como `ConcurrentHashMap`, `CopyOnWriteArrayList` e filas bloqueantes.
- Operações atômicas de `ConcurrentMap`, como `putIfAbsent` e `computeIfAbsent`.
- Sincronização de coleções versus coleções projetadas para acesso concorrente.
- Segurança de iteração e semântica de iteradores concorrentes.
- `CountDownLatch`, `Semaphore` e `CyclicBarrier` em nível conceitual.
- Fork/Join e uso de `parallel` streams: benefícios, custos e cuidado com estado compartilhado.

## Prática

Compare um mapa comum protegido por lock com `ConcurrentHashMap`; identifique quais sequências são atômicas e quais não são.
