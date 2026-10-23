# `ResultSet`, recursos e transações

## Estude

- Cursor de `ResultSet`: posição inicial e avanço com `next()`.
- Leitura de colunas por nome ou índice; índices JDBC iniciados em 1.
- Tipos e métodos de leitura de colunas, atualizações e valores SQL `NULL`.
- Result sets atualizáveis e tipos de cursor em nível conceitual.
- `autoCommit`, `commit` e `rollback`.
- Transações, consistência de operações e tratamento de falhas.
- Ordem adequada de fechamento de `ResultSet`, `Statement` e `Connection`.
- Exceções SQL e encadeamento de causas.

## Verifique se consegue

- Determinar o que `next()` retorna e quando um getter não pode ser chamado.
- Rastrear se uma alteração foi confirmada ou revertida em cada caminho de execução.
