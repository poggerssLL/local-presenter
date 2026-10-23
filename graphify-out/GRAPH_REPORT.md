Documentary planning graph. Relationships are extracted from headings and explicit Markdown links, not inferred execution dependencies. No API/LLM was called for this graph build; input/output model tokens: 0/0. The separate planning agents have unmeasured token use.

# Graph Report - Local Presenter  (2026-10-23)

## Corpus Check
- Documentary headings and explicit links only; no product code or semantic inference.

## Summary
- 109 nodes · 166 edges · 11 communities (10 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Entrega documental e proveniência
- Decisões de arquitetura
- Limites da evidência
- Plano de implementação revisado — Local Presenter
- Local Presenter
- Briefing e envelope da fase de planejamento
- Arquitetura proposta
- Abordagem A — retrato animado por áudio
- Plano de validação e gates
- Abordagem C — rosto 3D simplificado
- Local Presenter — regras do projeto

## God Nodes (most connected - your core abstractions)
1. `Plano de implementação revisado — Local Presenter` - 17 edges
2. `Documentação` - 14 edges
3. `Arquitetura proposta` - 11 edges
4. `Plano de validação e gates` - 11 edges
5. `Abordagem B — vídeo de referência com nova fala` - 11 edges
6. `Entrega documental e proveniência` - 10 edges
7. `Abordagem A — retrato animado por áudio` - 10 edges
8. `Abordagem C — rosto 3D simplificado` - 10 edges
9. `Briefing e envelope da fase de planejamento` - 9 edges
10. `Contrato proposto de trabalhos locais e remotos` - 9 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (11 total, 1 thin omitted)

### Community 0 - "Entrega documental e proveniência"
Cohesion: 0.12
Nodes (16): Entrega documental e proveniência, O que permanece informado ou proposto, O que não foi executado, Localização da evidência, Próxima ação delimitada, Atualização de publicação — 2026-10-21, O que foi observado nesta sessão, Grafo documental com Graphify (+8 more)

### Community 1 - "Decisões de arquitetura"
Cohesion: 0.17
Nodes (13): Decisões de arquitetura, Fase 1 — prova de compatibilidade e piloto de 20 segundos, Contrato proposto de trabalhos locais e remotos, Manifesto e entradas, Estados, idempotência e concorrência, Timeouts, cancelamento e desconexão, Partes, autoridade e transporte, Resultados, logs e retenção (+5 more)

### Community 2 - "Limites da evidência"
Cohesion: 0.14
Nodes (13): Limites da evidência, Fontes técnicas e limites de verificação, Vídeo de referência e sincronização labial, Rosto 3D e animação, Compatibilidade AMD, Voz sintetizada em português, Retrato guiado por áudio, Abordagem B — vídeo de referência com nova fala (+5 more)

### Community 3 - "Plano de implementação revisado — Local Presenter"
Cohesion: 0.20
Nodes (10): Plano de implementação revisado — Local Presenter, Estimativas de esforço e orçamento de decisão, Fase 0 — planejamento e bootstrap documental, Fase 2 — pipeline local por segmentos, Fase 3 — ferramenta local utilizável, Resultado do produto e definição de pronto, Fase 4 — desktop como executor remoto, Fase 5 — apresentação acadêmica completa (+2 more)

### Community 4 - "Local Presenter"
Cohesion: 0.42
Nodes (5): Local Presenter, GitHub e privacidade, Documentação, Comparação das três formas de abordar o problema, Contribuições aproveitadas

### Community 5 - "Briefing e envelope da fase de planejamento"
Cohesion: 0.22
Nodes (9): Briefing e envelope da fase de planejamento, Três abordagens independentes, Escopo autorizado para o planejamento em 2026-10-19, Resultado desejado, Exclusões, Fontes primárias de partida — não equivalem a testes, Aceite e parada desta fase, Autorização de publicação em 2026-10-21 (+1 more)

### Community 6 - "Arquitetura proposta"
Cohesion: 0.25
Nodes (8): Arquitetura proposta, Fluxo local do vídeo gravado, Organização proposta dos dados locais, Voz, prosódia e estilo textual, Componentes e responsabilidades, Isolamento de ambientes e dispositivos, Execução remota e fronteira entre computadores, Falhas e recuperação

### Community 7 - "Abordagem A — retrato animado por áudio"
Cohesion: 0.29
Nodes (6): Abordagem A — retrato animado por áudio, Pipeline e candidatos, Identidade e limitações, Windows, AMD, CPU e licenças, Estimativas e desconhecidos, Proposta e aquisição mínima

### Community 8 - "Plano de validação e gates"
Cohesion: 0.29
Nodes (7): Plano de validação e gates, Critérios de qualidade humana, Tempo e memória, Testes determinísticos e mocks futuros, Validação real e offline, Gate Linux e alternativa de abordagem, Fase 1 — compatibilidade e piloto de 20 segundos

### Community 9 - "Abordagem C — rosto 3D simplificado"
Cohesion: 0.33
Nodes (6): Abordagem C — rosto 3D simplificado, Aquisição e opções de construção, Pipeline proposto, Esforço e condições de escolha, Pesquisa documental adicional — 2026-10-23, Proposta e valor do 3D

## Knowledge Gaps
- **63 isolated node(s):** `GitHub e privacidade`, `Local Presenter — regras do projeto`, `Componentes e responsabilidades`, `Fluxo local do vídeo gravado`, `Organização proposta dos dados locais` (+58 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 65 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Plano de implementação revisado — Local Presenter` connect `Plano de implementação revisado — Local Presenter` to `Entrega documental e proveniência`, `Decisões de arquitetura`, `Limites da evidência`, `Local Presenter`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **What connects `GitHub e privacidade`, `Local Presenter — regras do projeto`, `Componentes e responsabilidades` to the rest of the system?**
  _63 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Entrega documental e proveniência` be split into smaller, more focused modules?**
  _Cohesion score 0.12380952380952381 - nodes in this community are weakly interconnected._
- **Why does `Plano de validação e gates` connect `Plano de validação e gates` to `Entrega documental e proveniência`, `Decisões de arquitetura`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Should `Limites da evidência` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `Arquitetura proposta` connect `Arquitetura proposta` to `Entrega documental e proveniência`, `Decisões de arquitetura`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._