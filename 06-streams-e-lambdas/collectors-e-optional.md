# Collectors e `Optional`

## Estude

- Coleta com `Collectors.toList`, `toSet`, `toMap`, `joining`, `counting`, `summarizing` e `averaging`.
- Agrupamento e particionamento com `groupingBy` e `partitioningBy`.
- Redução downstream, como `mapping`, `counting`, `summarizing` e `maxBy`.
- Colisões de chaves em `toMap` e uso da função de merge.
- `Optional`: `of`, `ofNullable`, `empty`, `isPresent`, `ifPresent`, `orElse`, `orElseGet`, `orElseThrow`, `map` e `flatMap`.
- Diferença entre avaliação imediata de `orElse` e avaliação sob demanda de `orElseGet`.
- `Optional` não deve ser usado como substituto universal de qualquer referência ou campo.

## Prática

Agrupe objetos por categoria e produza um resumo por grupo. Compare `orElse` e `orElseGet` com uma expressão que tenha efeito observável.
