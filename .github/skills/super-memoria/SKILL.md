---
name: super-memoria
description: Mantém e aplica preferências persistentes configuradas pelo usuário para este projeto. Use ao consultar, adicionar, alterar ou remover uma preferência.
---

# Super memória do projeto

Use as instruções em `.github/copilot-instructions.md` como fonte única das preferências persistentes deste projeto. Aplique todas as preferências em cada interação, mesmo quando a solicitação não estiver relacionada a esta skill.

## Regras de manutenção

- Só registre uma preferência quando o usuário a configurar explicitamente.
- Ao configurar, alterar ou remover uma preferência, atualize a fonte única; não mantenha cópias divergentes em outros arquivos.
- Preserve as preferências existentes ao adicionar uma nova.
- Interprete cada preferência de forma consistente e respeite o escopo explícito indicado pelo usuário.
- Se uma preferência nova entrar em conflito com outra ou tiver escopo ambíguo, peça esclarecimento antes de alterar a configuração.
- Não trate dados da conversa, suposições ou detalhes temporários da tarefa como preferências persistentes.

## Configuração inicial

- Idioma das respostas: português brasileiro, sempre.
