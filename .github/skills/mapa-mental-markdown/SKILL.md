---
name: mapa-mental-markdown
description: Cria ou atualiza um mapa mental SVG correspondente a um Markdown de conteúdo nas pastas temáticas numeradas do projeto. Use sempre que criar ou editar esse tipo de Markdown.
---

# Mapa mental para arquivos Markdown

Ao criar ou atualizar um arquivo Markdown de conteúdo em uma pasta temática numerada (`01-...` a `11-...`), mantenha esse Markdown e crie ou atualize seu mapa mental SVG como arquivo complementar:

- Para `pasta/assunto.md`, use `pasta/assunto.svg`.
- O `.svg` complementa o `.md`: nunca substitua, apague, renomeie ou converta o Markdown em SVG. Preserve os dois arquivos lado a lado.
- Use somente o conteúdo do Markdown correspondente como fonte. Não complemente com conhecimento externo nem invente detalhes.
- Não aplique a arquivos `README.md`, arquivos de configuração, arquivos em `.github` ou outros documentos que não sejam conteúdo de estudo.
- Preserve o restante do conteúdo e das alterações existentes no projeto. Se o SVG correspondente já existir, atualize-o sem apagar informações não relacionadas; não substitua mudanças não relacionadas do usuário.
- Se não for possível identificar o escopo ou o conteúdo não fornecer informação suficiente para uma seção, adapte os blocos ao tema em vez de inventar conteúdo.

## Padrão visual

- Entregue um SVG horizontal, legível em tela e impressão, com o tema principal central e de 6 a 8 blocos conectados por setas coloridas.
- Siga o estilo de `01-valores-texto-e-datas/1720992799.webp`: papel claro quadriculado, tema central manuscrito sobre destaque azul-claro, ramificações orgânicas e aparência de anotações à mão organizadas.
- Distribua os tópicos ao redor sem cartões rígidos, mantendo uma hierarquia visual clara, espaço em branco e leitura rápida.
- Use títulos manuscritos, texto explicativo limpo, destaques coloridos discretos e ícones ou pequenas ilustrações apenas quando ajudarem a compreensão.
- Selecione blocos apropriados ao assunto; conceito, elementos, funcionamento, exemplo, aplicações, vantagens, cuidados e resumo são sugestões, não uma lista obrigatória.
- Escreva em português brasileiro, preserve a terminologia original de Java e mantenha identificadores e APIs no nome original.
- Resuma em frases curtas, palavras-chave e comparações fiéis à fonte.

## Integração e validação

- Ao criar um novo tópico de estudo, acrescente um link para o SVG no README da pasta, se existir, sem gerar um mapa separado para o próprio README.
- Verifique se o SVG é XML válido, se o conteúdo está bem formado e se os blocos, textos e setas estão dentro da área visual.
- Não declare concluído se a criação do Markdown não vier acompanhada do SVG correspondente ou se a validação falhar.
