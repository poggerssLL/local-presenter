# Revisão do coordenador sobre os três estudos

Data: 2026-10-19. Escopo: revisão de planejamento, sem implementação. Os três planejadores foram despachados de verdade em paralelo pelo Orca com Antigravity / `gemini-3.8-flash-high` / `high`, com modelo efetivo confirmado. Não houve fallback de executor/modelo. O coordenador foi o único escritor dos documentos e da ferramenta de geração do grafo.

## Contribuições aproveitadas

| Estudo | Contribuição | Integração |
| --- | --- | --- |
| [A — retrato](approaches/A_PORTRAIT.md) | Aquisição mínima e aprovação do áudio antes do vídeo | Primeiro candidato ao MVP, condicionado a compatibilidade e identidade. |
| [B — vídeo](approaches/B_REFERENCE_VIDEO.md) | Preservar movimentos da referência; reduzir looping com cortes e tomadas | Alternativa comparável, com teste de artefatos e transições. |
| [C — 3D](approaches/C_FACE_3D.md) | Separar escaneamento estático de rig/visemas e renderização | Evolução opcional, sem bloquear entrega do vídeo acadêmico. |

## Correções materiais aplicadas

1. **CPU não é garantia:** os três estudos usaram expressões de execução garantida/determinística. Rejeitado. Dependências, tempo e qualidade continuam pendentes em CPU e GPU.
2. **Tempos e memória sem benchmark:** retirados fps, RTF, GB e tempos exatos atribuídos ao Ryzen/RX 7600 sem base local suficiente. Limites do [plano de validação](VALIDATION.md) são metas propostas, não resultados.
3. **Compatibilidade em camadas:** HIP SDK não comprova PyTorch, dependências ou modelo; documentação legada 7.2.1 não decide o suporte 7.14.0. Removidas recomendações padrão de spoof/override de arquitetura e generalizações sobre todas as GPUs AMD.
4. **Licença por artefato:** removidas afirmações universais sobre MIT/CPML/BFM/restauradores, ativos MakeHuman, Piper e pesos auxiliares. O inventário deve verificar código, checkpoint e dependência por revisão. Não há parecer jurídico ou permissão automática decorrente de uso acadêmico.
5. **Wav2Lip local continua distinto da API:** a chamada comercial no README não torna o serviço pago obrigatório. A versão local tem seus próprios limites e continua candidata de comparação, sem integração com API paga.
6. **Resolução de exportação não é resolução facial:** MP4 1080p não prova rosto em 1080p. A qualidade será revisada no tamanho final do avatar.
7. **Rosto 3D não surge pronto de uma foto:** marcos não recuperam toda a geometria. Malha base e escaneamento real são subcaminhos diferentes; rig/shape keys continuam necessários.
8. **Sem substituição do requisito:** voz de catálogo, fala pré-gravada integral ou slides sem avatar podem testar infraestrutura, mas não comprovam a apresentação com voz sintetizada e rosto próprio. Qualquer redução precisa de decisão explícita.
9. **Sincronização mensurável:** substituídas promessas de “perfeita/exata” por medição e aprovação com critérios propostos comuns.
10. **Integração remota delimitada:** substituída sincronização genérica/serviço aberto por pacote validado, estado no desktop, autenticação e retomada, conforme [contrato](REMOTE_JOBS.md).

## Decisão técnica

Prosseguir futuramente com prova de compatibilidade e piloto A de 20 segundos. Comparar B se A falhar em visual ou se vídeo de referência tiver preferência. Manter C opcional. A escolha de biblioteca/checkpoint não está homologada.

O [plano consolidado](IMPLEMENTATION_PLAN.md) é a proposta revisada. Os estudos editados preservam as contribuições e registram limites; as mensagens brutas de runtime não integram o conteúdo candidato a Git.

## Limites da evidência

- Baseline documental, catálogo, despachos e resultados dos planejadores foram observados nesta sessão.
- O coordenador conferiu fontes primárias em [SOURCES.md](SOURCES.md); isso não equivale a executar código.
- Especificações do desktop são informadas pelo proprietário, não auditadas remotamente.
- Nenhum modelo, licença completa de checkpoint, qualidade de voz, render facial, acesso remoto ou instalação foi validado na máquina alvo.
- Estimativas de esforço não são prazo contratual. Autorizações de implementação, dados pessoais e configuração de sistema permanecem específicas por fase.
