# Plano de implementação revisado — Local Presenter

Plano original de 2026-10-19; direção revista pelo proprietário em 2026-10-23. **B e C receberam pesquisa documental aprofundada; falta escolher um piloto. A permanece documentada, mas foi descartada para aplicação.** Nenhuma biblioteca está homologada; qualquer piloto futuro de 20 segundos depende de autorização própria e prova no desktop.

Este plano integra três estudos paralelos reais Antigravity / Gemini 3.8 Flash High e a [revisão do coordenador](REVIEW.md). Não inicia a aplicação. Premissas e autorização: [BRIEF.md](BRIEF.md). Fontes: [SOURCES.md](SOURCES.md).

## Resultado do produto e definição de pronto

Gerar um MP4 com slides sincronizados, fala nova sintetizada com voz semelhante à do proprietário e avatar visual reconhecível derivado de suas referências. A pessoa revisa roteiro, áudio, aparência e vídeo final antes de apresentar. Não é necessário tempo real, responder perguntas, corpo inteiro, treinamento do zero ou fotorrealismo perfeito.

Funcionar localmente após preparar ambientes/pesos, sem dependência de assinatura/API por geração. Código e checkpoints de terceiros continuam sendo dependências com termos próprios. Interface própria significa integrar componentes locais de forma controlada, não criar um modelo fundacional do zero.

O prazo da apresentação e sua duração exata ainda não foram informados. A primeira referência de planejamento será um piloto de 20 segundos, seguido de 60–90 segundos e uma apresentação completa com duração aprovada pelo dono.

## Comparação das três formas de abordar o problema

| Abordagem | Referência visual | Vantagem proposta | Custo ou risco principal | Decisão |
| --- | --- | --- | --- | --- |
| [A — retrato animado](approaches/A_PORTRAIT.md) | Foto própria | Aquisição simples, menor preparação de ativo | Movimento sintético e dependências antigas; AMD/CPU não testados | Estudo preservado; descartado para aplicação. |
| [B — vídeo de referência](approaches/B_REFERENCE_VIDEO.md) | Vídeo próprio curto | Preserva aparência e movimentos gravados | Loop, costura facial e dependências do lip-sync | Pesquisa documental concluída; candidato a piloto. |
| [C — rosto 3D](approaches/C_FACE_3D.md) | Fotos/scan e ativo facial | Controle de câmera, expressões e reutilização | Preparar rig/visemas e semelhança dá trabalho adicional | Pesquisa documental concluída; candidato a piloto. |

TTS por referência é requisito compartilhado. Trocar A por B ou C não resolve automaticamente falha de clonagem de voz.

## Decisões de arquitetura

- Desktop informado: Windows 11, RX 7600 8 GB, Ryzen 5 5600, RAM 24 GB; ainda sem inspeção real.
- Começar pelo Windows. CPU é candidato de linha de base; AMD será habilitada somente após prova do framework e do modelo completo. Não prometer desempenho em nenhum deles.
- Adaptadores isolados por ambiente e subprocesso: voz, visual, composição e executor de trabalhos.
- Uma tarefa GPU por vez; liberar um modelo antes do próximo. Sem treinamento e sem rede neural distribuída entre PCs.
- CLI e pacote local antes de UI e remoto. Cliente remoto só envia trabalhos e recebe resultados; desktop mantém o estado.
- Roteiro revisado, sem LLM local obrigatório. Estilo pessoal é tratado no texto e na prosódia, separadamente do timbre.
- [Contrato de trabalhos](REMOTE_JOBS.md), [arquitetura](ARCHITECTURE.md) e [critérios de validação](VALIDATION.md) são a base da implementação.

## Fase 0 — planejamento e bootstrap documental

Entrega desta sessão: pasta e Git local novos, GitHub privado criado, três estudos, revisão, arquitetura, contratos, roadmap e grafo documental Graphify. Somente ferramenta de documentação, sem código de inferência ou aplicativo.

Concluir depois de validar links, privacidade, integridade do grafo e encerramento dos três workers. Em 2026-10-21, o proprietário autorizou expressamente commit inicial, push e visibilidade pública deste snapshot documental. Esse marco de publicação não inicia a Fase 1 nem altera as exclusões de dados privados.

## Fase 1 — prova de compatibilidade e piloto de 20 segundos

**Objetivo:** descobrir se uma combinação de TTS e visual realmente atende qualidade e tempo no desktop. É a próxima etapa recomendada, mas não está iniciada.

Entregas propostas:

1. Diagnóstico somente leitura no desktop: versões, GPU, driver, espaço disponível e ferramentas existentes, sem inventário pessoal.
2. Matriz código/framework/checkpoint/licenças e revisões; comparar B e C e escolher explicitamente um candidato TTS e um visual antes de instalar.
3. Ambientes isolados por adaptador, sem atualizações globais/driver. Downloads de pesos e instalação de dependências dependem do envelope aprovado para a fase.
4. Pequeno teste CPU e, se houver suporte documentado, AMD. Começar com tensor pequeno e operações do modelo; não alocar gigabytes só para provar detecção.
5. Gerar texto novo em pt-BR, aprovar voz e então 20 segundos do visual escolhido. Compor com um slide e medir tempo, memória e sincronismo.
6. Relatório sanitizado com versões, comandos reproduzíveis sem caminhos pessoais, resultados e decisão de continuar, comparar o outro candidato ou parar.

Escopo de arquivos futuro: `tools/diagnose_runtime.py`, `experiments/`, `docs/COMPATIBILITY.md` e relatório de validação sanitizado. Modelos, ambientes, mídia e saídas ficam nos diretórios ignorados. Não construir UI, fila remota, instalador ou dual boot.

Gate: [VALIDATION.md](VALIDATION.md). Sem voz nova aprovada, não renderizar apresentação longa. Sem teste completo não afirmar suporte AMD. Se Windows bloquear, diagnosticar a dependência exata e só então propor Linux; nenhum override ou troca de backend silenciosos.

## Fase 2 — pipeline local por segmentos

**Objetivo:** transformar o piloto em processamento retomável, ainda local e por CLI.

Entregas: contratos de adaptador `probe/generate/cancel`, validação de manifesto v1, registro dos modelos homologados, segmentos imutáveis com hashes, cache por versão/entrada, checkpoints e composição. Diretórios futuros: `src/local_presenter/{contracts,adapters,pipeline}/`, `tests/` e documentação correspondente.

Gate determinístico: entradas inválidas, isolamento de caminhos, falha parcial, cancelamento e retomada com adapters fake. Gate real: três segmentos de conteúdo aprovado, voz/visual do piloto e MP4 de 60–90 segundos. Não fazer o aplicativo parecer pronto com fake ou mídia pré-gravada.

## Fase 3 — ferramenta local utilizável

**Objetivo:** permitir preparar e revisar a apresentação sem editar comandos.

Entregas: interface local com projeto/segmentos, seleção de referências próprias, texto por slide, prévia de áudio, prévia facial, aprovação e exportação. Tecnologia da UI será escolhida após o pipeline; se HTML/JSX/Tailwind, consultar daisyUI e definir aplicação local sem CDN obrigatório.

Gate: iniciar e cancelar um trabalho pela interface, corrigir somente uma frase, preservar trechos aprovados, reiniciar processo e recuperar estado. O conteúdo e a aparência são revisados pelo dono. Sem telemetria, upload externo ou login de serviço de IA obrigatório.

## Fase 4 — desktop como executor remoto

**Objetivo:** preparar e acompanhar a partir do outro computador sem depender de conexão contínua.

Entregas: transporte autenticado de pacotes, idempotência, fila persistida no desktop, progresso, coleta de prévias/resultado, retomada de cliente e cancelamento. Usar o [contrato remoto](REMOTE_JOBS.md); não implementar shell arbitrário nem expor porta pública.

Gate sintético antes de mídia pessoal: arquivo corrompido, job duplicado, caminho malicioso, perda de conexão, reinício do executor e disco cheio simulado. Gate real: transferência e execução de um trabalho pequeno entre as duas máquinas, com hashes conferidos. Instalação de SSH/VPN/firewall, contas e credenciais exigem autorização específica; conexões ainda não existem.

## Fase 5 — apresentação acadêmica completa

**Objetivo:** gerar e revisar a apresentação final.

Entregas: roteiro por slide aprovado, léxico de termos técnicos, clipes gerados e aprovados, MP4 final e manifesto sanitizado de produção. Capturas dos slides devem ser importadas/exportadas sem alterar o repositório de Automática.

Gate: assistir e escutar o vídeo inteiro; verificar começo, final, transições, números, cinco estações e ausência de fala inventada. Comprovar geração sem rede após preparar dependências. Registrar duração, formato, tamanho e hashes; entregar o arquivo ao proprietário. Nota e aceite docente não podem ser garantidos pela ferramenta.

## Fase 6 — aprofundamento 3D, se C não for o piloto inicial

Só iniciar por escolha explícita, caso B tenha sido o piloto inicial e C continue relevante. Escolher malha base ajustada ou reconstrução real; inventariar licença dos ativos, criar rig/visemas e testar 20 segundos antes de animação longa. Se C for escolhido como piloto inicial, esses gates pertencem à Fase 1. Sem corpo inteiro. Um render rápido de cabeça genérica não comprova semelhança ao dono.

## Delegação futura e um escritor por checkout

| Momento | Trabalho que pode ser paralelo | Escrita e integração |
| --- | --- | --- |
| Fase 1 | Leitor de compatibilidade e leitor de licenças | Um experimentador, somente após escolher os candidatos. |
| Fase 2 | Revisão de contratos e desenho de casos de falha | Um implementador; QA/gate depois da alteração. |
| Fase 3 | Avaliação de fluxo e acessibilidade | Um implementador UI com pipeline já aprovado. |
| Fase 4 | Revisão de transporte e testes sintéticos | Um implementador da integração; validação nas máquinas reais. |
| Fases 5/6 | Revisão de roteiro ou ativo, sem mudança no mesmo arquivo | Um produtor/implementador por checkout. |

Qualquer nova onda requer despacho real, perfil efetivo, escopo, exclusões, validação, parada e `fallback: none`. O proprietário autorizou especificamente nova pesquisa documental B/C em 2026-10-23 com Argon e Sol 6.1 em esforço médio; isso não autoriza execução das fases técnicas. Modelo e esforço de futuras etapas seguem a preferência da respectiva etapa.

## Estimativas de esforço e orçamento de decisão

Estimativas de planejamento, não medições nem prazos: Fase 1, 4–12 horas de engenharia mais geração/downloads; Fase 2, 12–24 horas; Fase 3, 12–24 horas; Fase 4, 8–16 horas após conectividade disponível. Referem-se a um adaptador por modalidade e pipeline já compatível; retrabalho de dependência pode invalidá-las.

Fase 5 depende do tamanho do roteiro e das revisões. Fase 6 não recebe prazo total antes de avaliar malha e semelhança; propor um teto de 8 horas para o primeiro experimento de ativo. São horas de trabalho, não promessa de dias corridos. Tempo de render final só será estimado com três segmentos medidos e margem de 50%.

Limitar investigação inicial de uma pilha incompatível a 4 horas antes de reportar bloqueio e replanejar; não consumir prazo com recompilações sem evidência de benefício. Não comprar hardware, pagar API ou alterar sistema como contingência automática.

## Riscos, incógnitas e parada

Incógnitas críticas: compatibilidade completa da RX 7600, viabilidade CPU, qualidade pt-BR, semelhança facial/vocal, licença de checkpoints/auxiliares, espaço em disco e conectividade do desktop. Cada uma tem gate na Fase 1 ou 4.

Parar ao concluir a fase autorizada. Não promover piloto para ferramenta completa ou declarar inferência real com base em mocks. Mudanças de requisito, modelos, sistema, dados ou prazo exigem decisão explícita. O [prompt da próxima fase](NEXT_PHASE_PROMPT.md) é apenas um rascunho condicional, ainda não despachado.
