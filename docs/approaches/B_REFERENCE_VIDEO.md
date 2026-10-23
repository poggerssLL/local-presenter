# Abordagem B — vídeo de referência com nova fala

Origem: estudo real de planejador Antigravity / Gemini 3.8 Flash High / esforço high, entregue em 2026-10-19. Síntese editada pelo coordenador após [revisão](../REVIEW.md); não transcrição literal. Sem inferência executada. Contexto: [briefing](../BRIEF.md). Fontes: [inventário](../SOURCES.md).

## Proposta e material inicial

Gravar um pequeno vídeo próprio para preservar aparência, iluminação e movimentos naturais. Sintetizar a fala do roteiro e adaptar a boca dos quadros à nova narração. Não é necessário gravar a apresentação inteira.

Proposta de aquisição: 20–40 segundos de vídeo frontal estável, sem mãos cobrindo o rosto, com luz contínua e movimentos leves; opcionalmente 2–3 tomadas curtas para variar transições. Captura em 1080p é útil para composição, mas não transforma a resolução nativa da região facial do modelo. A referência de voz permanece separada e limpa.

## Pipeline e comparação dos candidatos

1. Normalizar os slides e dividir o roteiro em segmentos.
2. Sintetizar e aprovar o áudio por segmento.
3. Preparar recortes do vídeo e processar lip-sync, com MuseTalk como primeiro candidato desta abordagem.
4. Revisar costuras de pele, dentes, preservação da identidade e fechamento labial.
5. Alternar avatar e slides, com cortes em pausas e transições para evitar loops evidentes.

MuseTalk declara código MIT e disponibilidade dos modelos para uso amplo. O inventário dos pesos auxiliares continua obrigatório: não estender MIT a VAE, detecção, parsing ou qualquer outro componente sem verificar seus próprios termos.

Wav2Lip permanece candidato secundário para comparação acadêmica, com restrição não comercial. A publicidade da API SyncLabs no README não remove a versão local nem torna seu uso obrigatório. O plano não utiliza a API paga. Não se afirma superioridade visual do MuseTalk na referência do proprietário sem comparação real.

## Fidelidade e repetição

Lip-sync não cria, por si só, gestos novos alinhados ao discurso. Uma tomada curta repetida durante vários minutos pode revelar o ciclo de movimentos. A contribuição central do estudo foi propor avatar em momentos de abertura/síntese, cortes em silêncios e variação de tomadas — opções sujeitas à aprovação do apresentador, sem porcentagem fixa obrigatória de tempo em tela.

Timbre semelhante não garante cadência pessoal. A qualidade é julgada com áudio novo, texto técnico e aparência em movimento. Processar uma fala gravada do próprio dono pode testar infraestrutura, mas não comprova síntese de voz nova.

## Hardware, contratos e execução remota

Windows/AMD precisam de prova completa, incluindo preparação facial e dependências. DirectML/ONNX não são trocas automáticas de backend. CPU pode falhar por dependência ou tornar o trabalho lento demais; será testada, não garantida.

Usar o contrato comum de [trabalhos](../REMOTE_JOBS.md) e a [arquitetura](../ARCHITECTURE.md). Pré-processamento reutilizável do avatar deve ser identificado por hash da referência e versão do adaptador. Reutilizar cache de outra pessoa ou de outro modelo é proibido. Transferência remota transporta pacotes e resultados, nunca exige porta pública.

## Gates, riscos e rejeição

- Gate B1: vídeo é decodificado, rosto detectado e preparação concluída sem erro.
- Gate B2: 20 segundos com voz sintetizada e movimentos coerentes, medindo uso de recursos.
- Gate B3: duas transições de slide sem salto evidente ou loop no meio da fala.
- Gate B4: minuto de teste com integridade do MP4 e aprovação humana.

Critérios comuns: [validação](../VALIDATION.md). Rejeitar B se movimentos distorcerem a identidade, costura facial for persistente ou dependências não tiverem caminho viável dentro do orçamento experimental. A abordagem A foi descartada para aplicação em 2026-10-23; qualquer revisão dessa decisão exigiria pedido explícito. Remover o avatar ou usar voz de catálogo reduz o requisito e precisa ser aceito como mudança de escopo.

## Estimativas e desconhecidos

O estudo atribuiu velocidades de CPU, consumo de VRAM e estabilidade sem medição local; a revisão removeu essas previsões. Desconhecidos: qualidade pt-BR, tempo de pré-processamento, dependências no Windows/RX 7600, tempo por segmento e perceptibilidade do looping. A escolha final depende do piloto comparável de 20 segundos.

## Pesquisa documental adicional — 2026-10-23

Argon, em esforço médio e somente leitura, pesquisou candidatos locais; o coordenador conferiu as afirmações abaixo nas fontes originais. O [MuseTalk 1.5](https://github.com/TMElyralab/MuseTalk) segue como candidato principal **para investigação**, pois o projeto publica inferência em Windows, mas seu guia de instalação usa PyTorch CUDA e `mmcv`/`mmpose`; o fluxo de preparação facial e os pesos auxiliares precisam de inventário antes de uma escolha técnica. O teste publicado em GPU NVIDIA de 4 GB não é medição ou garantia para a RX 7600. O código é MIT, mas os termos de cada peso e componente auxiliar são separados.

O [LatentSync](https://github.com/bytedance/LatentSync) declara mínimo de 8 GB para inferência 1.5 e 18 GB para 1.6; a versão 1.6 não cabe no orçamento nominal de VRAM informado. O código de inferência atual usa dispositivo `cuda`, portanto nenhum desses números comprova execução em AMD/Windows. VideoReTalking e Wav2Lip continuam comparadores documentais sujeitos a revisão de licenças e dependências, sem adoção automática.

O menor experimento futuro de B deve verificar, nesta ordem, preparação do vídeo/rosto (B1), 20 segundos com voz nova aprovada (B2), duas transições e repetição perceptível (B3), e um minuto completo com revisão humana e integridade do MP4 (B4). Registrar versões, dispositivo real, tempo, RAM/VRAM, termos dos pesos, costura e semelhança. Nada disso foi executado nesta pesquisa.
