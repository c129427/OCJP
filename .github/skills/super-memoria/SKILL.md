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

## Prompt reutilizável: mapa mental

> Crie um mapa mental visual para revisão sobre **[TEMA]**, usando somente o conteúdo de **[PASTA OU FONTES]**. Siga o estilo da referência `01-valores-texto-e-datas/1720992799.webp`: formato horizontal, fundo claro quadriculado, conceito principal central em letras manuscritas sobre uma mancha azul-clara, ramificações com setas orgânicas escuras e tópicos distribuídos ao redor, sem cartões rígidos. Use títulos manuscritos, texto explicativo simples e legível, destaques coloridos discretos e hierarquia clara. Organize os pontos em 6–8 blocos adequados ao tema (por exemplo: conceito, elementos, funcionamento, exemplos, aplicações, vantagens, cuidados e resumo). Resuma com frases curtas e comparações úteis; preserve a terminologia original, escreva em português brasileiro e não acrescente informações que não estejam nas fontes. Entregue como SVG horizontal, legível em tela e impressão, e inclua um link no README da pasta quando fizer parte do projeto.

Ao criar novos mapas mentais, aplique esse padrão como configuração padrão do projeto; adapte a quantidade e os nomes dos blocos ao conteúdo, sem sacrificar precisão nem legibilidade.
