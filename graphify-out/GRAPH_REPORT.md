Documentary planning graph. Relationships are extracted from headings and explicit Markdown links, not inferred execution dependencies. No API/LLM was called for this graph build; input/output model tokens: 0/0. The separate planning agents have unmeasured token use.

# Graph Report - Local Presenter  (2026-10-21)

## Corpus Check
- Documentary headings and explicit links only; no product code or semantic inference.

## Summary
- 107 nodes · 161 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Execução remota e fronteira entre computadores
- Local Presenter
- Entrega documental e proveniência
- Revisão do coordenador sobre os três estudos
- Briefing e envelope da fase de planejamento
- Plano de implementação revisado — Local Presenter
- Arquitetura proposta
- Abordagem A — retrato animado por áudio
- Plano de validação e gates
- Abordagem B — vídeo de referência com nova fala
- Abordagem C — rosto 3D simplificado
- Local Presenter — regras do projeto

## God Nodes (most connected - your core abstractions)
1. `Plano de implementação revisado — Local Presenter` - 17 edges
2. `Documentação` - 14 edges
3. `Arquitetura proposta` - 11 edges
4. `Plano de validação e gates` - 11 edges
5. `Entrega documental e proveniência` - 10 edges
6. `Abordagem A — retrato animado por áudio` - 10 edges
7. `Abordagem B — vídeo de referência com nova fala` - 10 edges
8. `Briefing e envelope da fase de planejamento` - 9 edges
9. `Contrato proposto de trabalhos locais e remotos` - 9 edges
10. `Abordagem C — rosto 3D simplificado` - 9 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (12 total, 1 thin omitted)

### Community 0 - "Execução remota e fronteira entre computadores"
Cohesion: 0.16
Nodes (13): Execução remota e fronteira entre computadores, Decisões de arquitetura, Fase 1 — prova de compatibilidade e piloto de 20 segundos, Fase 4 — desktop como executor remoto, Contrato proposto de trabalhos locais e remotos, Manifesto e entradas, Estados, idempotência e concorrência, Timeouts, cancelamento e desconexão (+5 more)

### Community 1 - "Local Presenter"
Cohesion: 0.19
Nodes (9): Local Presenter, GitHub e privacidade, Documentação, Próxima ação delimitada, Riscos, incógnitas e parada, Comparação das três formas de abordar o problema, Prompt preparado — Fase 1, ainda não autorizado nem despachado, Decisão técnica (+1 more)

### Community 2 - "Entrega documental e proveniência"
Cohesion: 0.19
Nodes (10): Entrega documental e proveniência, O que permanece informado ou proposto, O que não foi executado, Localização da evidência, Atualização de publicação — 2026-10-21, O que foi observado nesta sessão, Grafo documental com Graphify, Reprodução local sem API (+2 more)

### Community 3 - "Revisão do coordenador sobre os três estudos"
Cohesion: 0.20
Nodes (9): Revisão do coordenador sobre os três estudos, Correções materiais aplicadas, Limites da evidência, Fontes técnicas e limites de verificação, Vídeo de referência e sincronização labial, Rosto 3D e animação, Compatibilidade AMD, Voz sintetizada em português (+1 more)

### Community 4 - "Briefing e envelope da fase de planejamento"
Cohesion: 0.22
Nodes (9): Briefing e envelope da fase de planejamento, Três abordagens independentes, Escopo autorizado para o planejamento em 2026-10-19, Resultado desejado, Exclusões, Fontes primárias de partida — não equivalem a testes, Aceite e parada desta fase, Autorização de publicação em 2026-10-21 (+1 more)

### Community 5 - "Plano de implementação revisado — Local Presenter"
Cohesion: 0.22
Nodes (9): Plano de implementação revisado — Local Presenter, Estimativas de esforço e orçamento de decisão, Fase 0 — planejamento e bootstrap documental, Fase 2 — pipeline local por segmentos, Fase 3 — ferramenta local utilizável, Resultado do produto e definição de pronto, Fase 5 — apresentação acadêmica completa, Fase 6 — rosto 3D opcional (+1 more)

### Community 6 - "Arquitetura proposta"
Cohesion: 0.29
Nodes (7): Arquitetura proposta, Fluxo local do vídeo gravado, Organização proposta dos dados locais, Voz, prosódia e estilo textual, Componentes e responsabilidades, Isolamento de ambientes e dispositivos, Falhas e recuperação

### Community 7 - "Abordagem A — retrato animado por áudio"
Cohesion: 0.29
Nodes (6): Abordagem A — retrato animado por áudio, Pipeline e candidatos, Identidade e limitações, Windows, AMD, CPU e licenças, Estimativas e desconhecidos, Proposta e aquisição mínima

### Community 8 - "Plano de validação e gates"
Cohesion: 0.29
Nodes (7): Plano de validação e gates, Critérios de qualidade humana, Tempo e memória, Testes determinísticos e mocks futuros, Validação real e offline, Gate Linux e alternativa de abordagem, Fase 1 — compatibilidade e piloto de 20 segundos

### Community 9 - "Abordagem B — vídeo de referência com nova fala"
Cohesion: 0.33
Nodes (6): Abordagem B — vídeo de referência com nova fala, Pipeline e comparação dos candidatos, Fidelidade e repetição, Gates, riscos e rejeição, Estimativas e desconhecidos, Proposta e material inicial

### Community 10 - "Abordagem C — rosto 3D simplificado"
Cohesion: 0.33
Nodes (6): Abordagem C — rosto 3D simplificado, Aquisição e opções de construção, Pipeline proposto, Contratos e gates, Esforço e condições de escolha, Proposta e valor do 3D

## Knowledge Gaps
- **61 isolated node(s):** `GitHub e privacidade`, `Local Presenter — regras do projeto`, `Componentes e responsabilidades`, `Fluxo local do vídeo gravado`, `Organização proposta dos dados locais` (+56 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 63 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Plano de implementação revisado — Local Presenter` connect `Plano de implementação revisado — Local Presenter` to `Execução remota e fronteira entre computadores`, `Local Presenter`, `Entrega documental e proveniência`, `Revisão do coordenador sobre os três estudos`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **What connects `GitHub e privacidade`, `Local Presenter — regras do projeto`, `Componentes e responsabilidades` to the rest of the system?**
  _61 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `Plano de validação e gates` connect `Plano de validação e gates` to `Execução remota e fronteira entre computadores`, `Local Presenter`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `Arquitetura proposta` connect `Arquitetura proposta` to `Execução remota e fronteira entre computadores`, `Local Presenter`, `Abordagem A — retrato animado por áudio`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._