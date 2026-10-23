# `try`, `catch`, `finally` e multi-catch

## Estude

- Sintaxe e fluxo de blocos `try`, `catch` e `finally`.
- Ordem dos blocos `catch`, compatibilidade dos tipos e exceção capturada.
- Multi-catch com `|` e a regra de que os tipos não podem ter relação de subtipagem entre si.
- Blocos `finally`: execução normal, retorno, exceção e situações em que o processo termina abruptamente.
- Exceção original versus exceção lançada no `catch` ou `finally`.
- `try` como expressão (try-with-resources) e diferenças em relação ao `try` comum.

## Prática

Monte uma tabela de fluxo para métodos com `return` no `try` e no `finally`. Evite depender de retorno ou lançamento de exceção dentro de `finally`.
