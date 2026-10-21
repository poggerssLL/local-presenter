# Local Presenter

Planejamento de uma ferramenta local para gerar apresentações gravadas com voz sintetizada a partir de referência autorizada e uma aproximação visual do próprio apresentador.

**Estado:** planejamento revisado e bootstrap documental; nenhuma aplicação ou inferência implementada. O objetivo é produção offline após preparação, sem obrigação de API paga. O caso inicial é uma apresentação acadêmica sobre uma envasadora de água em copos.

Comece pelo [plano de implementação](docs/IMPLEMENTATION_PLAN.md). Recomendação: piloto de retrato animado por áudio de 20 segundos no desktop Windows 11 antes de construir a ferramenta. Voz, rosto, tempo e suporte AMD/CPU precisam de prova real.

## Documentação

- [Briefing e limites](docs/BRIEF.md)
- [Plano em fases e delegação futura](docs/IMPLEMENTATION_PLAN.md)
- [Estudo A — retrato animado](docs/approaches/A_PORTRAIT.md)
- [Estudo B — vídeo de referência](docs/approaches/B_REFERENCE_VIDEO.md)
- [Estudo C — rosto 3D](docs/approaches/C_FACE_3D.md)
- [Revisão crítica e correções](docs/REVIEW.md)
- [Arquitetura proposta](docs/ARCHITECTURE.md)
- [Contrato de trabalhos locais/remotos](docs/REMOTE_JOBS.md)
- [Validação e critérios de aceite](docs/VALIDATION.md)
- [Fontes e limites de compatibilidade/licença](docs/SOURCES.md)
- [Próximo prompt, ainda não despachado](docs/NEXT_PHASE_PROMPT.md)
- [Entrega e evidências](docs/DELIVERY.md)
- [Grafo documental e reprodução](docs/GRAPH.md)

## GitHub e privacidade

Repositório público: [poggerssLL/local-presenter](https://github.com/poggerssLL/local-presenter). Commit inicial, push e visibilidade pública autorizados expressamente em 2026-10-21. O conteúdo desta publicação é o planejamento revisado, o grafo documental e sua ferramenta de geração; a implementação da aplicação continua pendente.

Rosto, voz, pesos e resultados ficam fora do Git. O desktop alvo foi descrito pelo proprietário e ainda não foi testado.
