# Data e hora com `java.time`

## Estude

- Tipos imutáveis: `LocalDate`, `LocalTime`, `LocalDateTime`, `ZonedDateTime` e `Instant`.
- Criação com `now`, `of`, `parse` e `from`.
- Ajustes e operações que devolvem novos valores: `plus`, `minus`, `with`, `isBefore` e `isAfter`.
- Diferença entre `Period` (anos, meses, dias) e `Duration` (segundos e unidades menores).
- `ZoneId`, `ZoneOffset`, fusos e conversão entre horários locais e horários com zona.
- Parsing e formatação com `DateTimeFormatter`; formatos predefinidos e padrões.
- Imutabilidade e consequências de ignorar o valor devolvido por uma operação.

## Verifique se consegue

- Escolher o tipo adequado para data civil, horário local, instante global ou data com fuso.
- Explicar por que somar um `Period` de um mês não equivale sempre a somar uma quantidade fixa de dias.
- Identificar falhas de parsing e diferenças de zona horária.
