# Threads e executors

## Estude

- Criar tarefas com `Runnable` e `Callable`; diferenças entre ambos e seus resultados.
- Criar e iniciar uma `Thread`; diferença entre chamar `start()` e chamar `run()`.
- Estados e ciclo de vida de uma thread; `sleep`, `join` e interrupção.
- Tratamento de `InterruptedException` e preservação do estado de interrupção quando apropriado.
- `Executor`, `ExecutorService`, submissão de tarefas e encerramento com `shutdown`.
- `Future`, obtenção de resultado, cancelamento e exceções de tarefas.
- Agendamento com `ScheduledExecutorService`.
- Daemon threads e encerramento do processo.

## Prática

Submeta tarefas que retornam valores, aguarde os resultados e encerre o executor. Explique o comportamento se uma tarefa falhar.
