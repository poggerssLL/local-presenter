# Plano de validação e gates

Todos os critérios abaixo são propostos; não são resultados medidos. Referências: [briefing](BRIEF.md), [arquitetura](ARCHITECTURE.md), [contrato de trabalhos](REMOTE_JOBS.md), [plano](IMPLEMENTATION_PLAN.md).

## Fase 1 — compatibilidade e piloto de 20 segundos

No desktop real, registrar versões de Windows, driver, Python, framework, GPU detectada e espaço livre sem serial, usuário ou caminhos pessoais. Testar primeiro CPU e depois AMD quando houver instalação compatível documentada. Executar voz e rosto separadamente; medir tempo de carga e geração, pico de RAM/VRAM com método declarado, falhas e tempo total. Não baixar modelos sem decisão explícita da etapa de implementação.

O caso contém texto novo em pt-BR, com “envasadora”, “termosselagem”, “intertravamento”, “150 mililitros” e “cinco estações”. O texto deve explicar o projeto corretamente. Usar referência própria consentida apenas no teste autorizado. Não confundir referência gravada com fala sintetizada.

## Critérios de qualidade humana

| Dimensão | Critério inicial de aceite |
| --- | --- |
| Identidade vocal | Proprietário avalia semelhança de 1 a 5; meta >= 4, em três frases novas. |
| Inteligibilidade | Nenhuma palavra omitida/inventada; números e cinco termos técnicos compreensíveis na escuta. |
| Prosódia | Pausas e ritmo aprovados pelo proprietário; avaliação separada do timbre. |
| Identidade visual | Proprietário reconhece a semelhança e dá nota >= 4/5 no tamanho final do avatar. |
| Sincronização | Inspeção em cinco eventos de fechamento labial; meta de desvio <= 120 ms quando mensurável. Inspeção de quadros e áudio, não afirmação baseada em screenshot. |
| Artefatos | Sem boca dupla, quadro facial quebrado ou tremulação persistente no trecho aprovado. |

Esses limiares são metas de produto ajustáveis pelo proprietário, sem certificação de identidade nem métricas universais de realismo. WER ou similaridade de embedding podem auxiliar depois, mas não substituem escuta, rosto e revisão semântica.

## Tempo e memória

Meta inicial de viabilidade: piloto de 20 segundos concluir em até 60 minutos por estágio, sem OOM, queda de driver ou paginação contínua. Se ultrapassar, registrar medição, tentar somente uma configuração menor explicitamente selecionada e reavaliar viabilidade; não ampliar prazo indefinidamente. Para a apresentação completa, estimar pelo tempo observado em três segmentos representativos e reservar margem de 50%, sem extrapolar apenas o menor trecho.

Memória: um modelo de cada vez; resolução facial e batch conservadores. Não assumir que 8 GB inteiros estão livres ou usar benchmark NVIDIA como previsão AMD.

## Testes determinísticos e mocks futuros

- Manifesto válido/inválido, caminhos maliciosos e conteúdo de tipo incorreto.
- Idempotência: reenvio não executa estágio duas vezes.
- Retomada: queda após voz preserva WAV aprovado e retoma visual.
- Falha/cancelamento: nenhum MP4 parcial é anunciado como concluído; estado e processo filho coerentes.
- Adapter fake: duração e arquivos sintéticos validam contrato, nunca qualidade de IA.
- Composição: rejeitar mídia ausente, mismatch de fps, duração inválida e áudio truncado.

## Validação real e offline

Após ambientes/checkpoints preparados, executar com rede bloqueada para os processos e comprovar ausência de download ou chamadas externas. Aprovar 20 segundos, depois 60–90 segundos e somente então a apresentação completa. FFprobe é candidato para verificar MP4 H.264/AAC, resolução, fps e duração; escutar e assistir começo, meio, final e transições. Meta de desvio áudio/vídeo <= 120 ms sem deriva perceptível.

Não declarar uma resolução facial 1080p apenas porque o compositor exportou 1920x1080. Registrar resolução nativa do modelo e tamanho de exibição.

## Gate Linux e alternativa de abordagem

Linux só é considerado após registrar um bloqueio Windows específico e identificar uma combinação de driver/framework/modelo com evidência melhor para RX 7600. Dual boot, partição e instalação exigem autorização própria e backup; este plano não executa essas ações.

Após a pesquisa documental de B e C, escolher explicitamente a abordagem do piloto pelos mesmos critérios e licenças. A permanece como estudo histórico e foi descartada para aplicação em 2026-10-23. Se C for escolhida, exigir prova de rig/visemas; se B for escolhida, exigir prova de costura facial e repetição. CPU ou troca de abordagem nunca são fallback silencioso: registrar escolha, custo de tempo e resultado esperado.
