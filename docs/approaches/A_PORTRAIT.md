# Abordagem A — retrato animado por áudio

Origem: estudo real de planejador Antigravity / Gemini 3.8 Flash High / esforço high, entregue em 2026-10-19. Esta é uma síntese editada pelo coordenador, com correções da [revisão](../REVIEW.md); não é transcrição literal. Não houve execução de modelos. Contexto: [briefing](../BRIEF.md). Fontes: [inventário](../SOURCES.md).

## Proposta e aquisição mínima

Usar uma foto frontal própria bem iluminada e uma amostra limpa de voz para gerar fala nova e um vídeo de cabeça falante. O planejador recomenda essa abordagem como primeiro MVP pela aquisição simples e pelo desacoplamento entre voz e imagem.

Proposta inicial de material: foto sem obstruções com rosto em resolução suficiente para o recorte do modelo; 30–60 segundos de fala limpa para selecionar uma referência adequada, embora o checkpoint possa utilizar apenas parte dela. Taxa de amostragem e duração efetiva serão as exigidas pelo adaptador homologado, não um padrão universal imposto antecipadamente.

## Pipeline e candidatos

1. Roteiro aprovado por slide e expansão de siglas/unidades quando necessário.
2. Chatterbox Multilingual/pack pt-BR como candidato à síntese por referência.
3. Escuta e aprovação do WAV antes de processar o rosto.
4. SadTalker como candidato à animação de retrato, inicialmente com recorte de 256 e sem restaurador facial, se suportado.
5. Clipe aprovado e composição com slides em tela 1920x1080; tamanho do avatar dimensionado pela qualidade real.

Modelo e dependências não estão escolhidos definitivamente. LivePortrait requer fonte de movimento e não substitui sozinho a etapa áudio-dirigida. Restauradores e modelos pesados de difusão ficam fora da primeira tentativa; não há base suficiente para afirmar um requisito universal de VRAM para todas as variantes.

## Identidade e limitações

O timbre depende da referência e da capacidade de clonagem; prosódia e pronúncia precisam de ajuste e escuta. O modo de explicar vem do roteiro aprovado. Pontuação influencia a geração, mas não garante pausas exatas. Nenhum mecanismo específico de embedding é assumido sem inspeção da implementação escolhida.

Riscos visuais: piscadas artificiais, cabeça com movimento repetitivo, deformação de dentes/boca, textura borrada e distância entre resolução facial nativa e exportação final. A face deve ser avaliada no tamanho em que aparecerá na apresentação.

## Windows, AMD, CPU e licenças

Separar disponibilidade do HIP SDK, framework e operadores do modelo. CPU é candidato de teste, não garantia de execução ou de prazo. Não aplicar overrides de arquitetura, camadas de tradução ou recompilação de comunidade como instalação padrão. Linux depende de diagnóstico específico.

O código do SadTalker declara Apache 2.0, mas pesos e componentes auxiliares precisam ser inventariados. O estudo levantou BFM e restauradores; sua presença e licença devem ser verificadas na revisão selecionada. Não se conclui permissão apenas por se tratar de uma apresentação acadêmica. Chatterbox exige checkpoint multilíngue, não as variantes leves listadas como inglês.

## Entregas, gates e rejeição

Contrato de entradas/saídas: [trabalhos](../REMOTE_JOBS.md). A escolha do adaptador será explícita em cada manifesto. Cada estágio gera artefato local, duração e status; não há inferência dividida entre computadores.

- Gate A1: gerar frase técnica nova e aprovar timbre/pronúncia.
- Gate A2: gerar 20 segundos de rosto, medindo tempo e memória, sem crash ou OOM.
- Gate A3: assistir com áudio e validar semelhança, boca e movimentos no tamanho final.
- Gate A4: compor com slide, verificar sincronização e exportação.

Os limiares comuns estão em [VALIDATION.md](../VALIDATION.md). Rejeitar A se identidade visual/voz não atingirem aprovação ou se o custo observado for impraticável após uma configuração menor. Avaliar B explicitamente; não entregar uma foto estática ou voz de catálogo como se cumprisse o avatar com voz própria.

## Estimativas e desconhecidos

O estudo original propôs números exatos de VRAM e tempos em CPU/GPU sem evidência suficiente para este hardware. Eles foram retirados do plano. O primeiro orçamento é um experimento limitado, com duração real medida. Permanecem desconhecidos: dependências Windows, desempenho da RX 7600, tempo de CPU, semelhança da voz e qualidade facial com a referência real.
