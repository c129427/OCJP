# Sincronização e visibilidade

## Estude

- Condições de corrida e estado compartilhado mutável.
- Blocos e métodos `synchronized`; monitor associado ao objeto ou à classe.
- Exclusão mútua e visibilidade de alterações entre threads.
- `volatile`: garantias de visibilidade e limites; não torna operações compostas automaticamente atômicas.
- Imutabilidade e confinamento de dados como estratégias para reduzir compartilhamento.
- Deadlock, starvation e contenção.
- `wait`, `notify` e `notifyAll`: uso associado ao monitor e necessidade de testar condições em loop.
- Seções críticas e segurança de operações de leitura-modificação-escrita.

## Verifique se consegue

- Distinguir atomicidade de visibilidade.
- Detectar um deadlock em uma sequência de aquisição de locks.
- Explicar por que uma variável `volatile` não resolve incremento concorrente.
