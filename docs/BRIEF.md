# Briefing e envelope da fase de planejamento

## Resultado desejado

Ferramenta própria para gerar um MP4 de apresentação acadêmica com slides, voz semelhante à do proprietário e avatar visual derivado do seu próprio rosto. O professor aceita vídeo pronto. Não há requisito de perguntas ao vivo, corpo inteiro ou perfeição fotorrealista.

## Informações fornecidas pelo proprietário

- Desktop de processamento: Windows 11, Radeon RX 7600 com 8 GB VRAM, Ryzen 5 5600 e 24 GB RAM.
- Linux em dual boot é possibilidade futura, somente se um teste justificar.
- Outro computador pode preparar trabalhos, acompanhar execução e receber resultados remotamente.
- A referência de rosto e voz será do próprio proprietário. Nenhuma mídia foi fornecida nesta fase.
- Sem assinatura ou cobrança por geração de terceiros. Modelos pré-treinados de terceiros com execução local são aceitáveis; licenças precisam ser verificadas antes da adoção.

## Três abordagens independentes

1. **Retrato animado por áudio:** foto frontal, síntese de voz e geração de cabeça falante. Priorizar custo e MVP.
2. **Vídeo de referência e nova fala:** preservar aparência/movimento de vídeo e adaptar sincronização labial. Comparar fidelidade, material necessário e compatibilidade AMD.
3. **Rosto 3D simplificado:** reconstrução, textura, rig/blendshapes e animação facial guiada por áudio. Comparar esforço adicional e valor real para um vídeo gravado.

Cada estudo deve cobrir aquisição mínima de referência, alternativas técnicas e licenças, hardware Windows/AMD e CPU, separação de timbre/prosódia/estilo textual, execução remota por trabalhos, etapas, riscos, critérios de aceite, plano B explícito e estimativas identificadas como estimativas.

## Escopo autorizado para o planejamento em 2026-10-19

- Três planejadores reais em paralelo, via Orca/Antigravity, Gemini 3.8 Flash High, esforço high, fallback none.
- Coordenador único cria documentação e revisa as três propostas.
- Criar pasta, Git local e repositório GitHub novo privado; não modificar o projeto acadêmico ou o Organizer.
- Gerar grafo do planejamento com Graphify local, sem extração por API externa.
- Pesquisa somente em fontes públicas originais. Nenhum dado biométrico real é necessário para planejar.

## Exclusões

Sem aplicativo implementado, instalações, pesos, benchmark real, captura, clonagem real, acesso ao desktop remoto, configuração de VPN/SSH/firewall, dual boot, treinamento, API paga ou deploy. Commit e push não foram pedidos nominalmente; manter o conteúdo local até autorização específica.

## Fontes primárias de partida — não equivalem a testes

Consultadas anteriormente pelo coordenador em 2026-10-19; os estudos devem tratar a escolha técnica como candidata e registrar fonte/data. Compatibilidade deve distinguir HIP SDK, framework, dependências e execução completa.

- https://github.com/resemble-ai/chatterbox — síntese/clonagem por referência; suporte multilíngue, conferir variante pt-BR e licença de cada checkpoint.
- https://github.com/OpenTalker/SadTalker — retrato + áudio, código Apache 2.0, conferir licenças dos componentes/pesos.
- https://github.com/TMElyralab/MuseTalk — lip-sync, código/modelo declarados permissivos no README; dependências precisam de revisão própria.
- https://github.com/KlingAIResearch/LivePortrait — animação por vídeo de movimento; não presumir que áudio sozinho dirige o rosto.
- https://github.com/ROCm/rocm-install-on-windows/blob/develop/docs/reference/system-requirements.rst — HIP SDK inclui RX 7600; isso não garante suporte do aplicativo.
- https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/windows/windows_compatibility.html — documentação legada cobre até ROCm 7.2.1; não generalizar a versões novas.
- https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/docs-7.14.0/compatibility/compatibility-matrix.html — documentação unificada mais nova; confirmar matriz específica no momento da implementação.

## Aceite e parada desta fase

Três estudos reais com modelo efetivo comprovado, revisão do coordenador, arquitetura proposta, roadmap fracionado e critérios mensuráveis, registro sanitizado da evidência e grafo navegável. Hardware/inferência não testados ficam explicitamente pendentes. Não iniciar implementação.

## Autorização de publicação em 2026-10-21

O proprietário pediu expressamente commit, push e visibilidade pública do novo repositório. O envio abrange somente o snapshot documental sanitizado e os artefatos do grafo. As exclusões de mídia, modelos, credenciais e runtime permanecem; a implementação da aplicação não foi autorizada por esse pedido.
