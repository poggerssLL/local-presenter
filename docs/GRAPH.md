# Grafo documental com Graphify

O grafo desta entrega mapeia títulos, seções e links explícitos dos documentos de planejamento. Não é extração semântica de modelos externos, arquitetura executável ou prova de produto funcionando. Contexto: [entrega](DELIVERY.md), [plano](IMPLEMENTATION_PLAN.md) e [revisão](REVIEW.md).

## Artefatos e cobertura

- `graphify-out/graph.json`: nós/arestas produzidos por `graphify.build` e `graphify.export`.
- `graphify-out/graph.html`: visualização interativa exportada pelo Graphify.
- `graphify-out/GRAPH_REPORT.md`: comunidades, coesão, hubs e perguntas sugeridas produzidos pelas bibliotecas Graphify, com aviso de escopo documental.
- `graphify-out/coverage.json`: método e SHA-256 de cada documento coberto.
- `graphify-out/verification.json`: resultado sanitizado dos checks finais, separado das fontes indexadas para não produzir autorreferência de hashes.

As relações `contains` e `references` significam estrutura documental e link escrito. Não significam dependência de execução, validação de um modelo ou recomendação inferida. As fontes são `README.md`, `AGENTS.md`, `docs/*.md` e `docs/approaches/*.md`. Mídia, diretórios privados, pesos, runtime e cache não entram.

## Reprodução local sem API

Requer um ambiente Python com o pacote Graphify (`graphifyy`) já instalado. Não há instalação automática no script e não é necessário configurar chave de API. Execute da raiz do projeto com o Python desse ambiente:

```text
python tools/build_project_graph.py
graphify export html
graphify query "compatibilidade Windows AMD" --budget 1200
```

Caso o comando `python` padrão não enxergue o pacote do `graphify`, usar o Python do ambiente em que o Graphify foi instalado; não reinstalar globalmente apenas para resolver o PATH. O gerador recusa grafo vazio e preserva a proteção Graphify contra redução não revisada.

Não usar `graphify update` como substituto deste gerador documental: o modo code-only não cobre estes documentos e pode gerar um mapa diferente. Depois que houver código de produto, planejar uma cobertura AST adicional e preservar o limite entre proposto e implementado.

## Limites, custos e integridade

Construção do grafo: 0 chamadas de modelo externo e 0 tokens de entrada/saída de extração por modelo. Isso não significa custo/token zero para os três agentes de planejamento; consumo deles não foi medido. HTML pode depender dos recursos da versão do Graphify instalada; funcionamento interativo offline precisa ser conferido antes de prometê-lo como requisito de produto.

A verificação confere cobertura por hash, schema, nós únicos, endpoints, localizações de fonte, ausência de caminhos pessoais e exclusão de privados. Não houve QA visual de navegador. Mudou qualquer documento indexado, regenere e confira `coverage.json`; o grafo não é mantido automaticamente por hooks nesta fase.
