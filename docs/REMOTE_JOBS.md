# Contrato proposto de trabalhos locais e remotos

Versão de desenho: `local-presenter/job-v1`. Não há transporte implementado ou acesso ao desktop. Componentes: [arquitetura](ARCHITECTURE.md). Critérios: [validação](VALIDATION.md).

## Partes, autoridade e transporte

- Cliente: prepara texto, slides e seleção de referências; solicita execução, cancelamento e coleta resultados.
- Desktop: fonte de verdade do estado persistido e único executor dos modelos.
- Proprietário: aprova referências, voz, resultado e configuração de conexão.
- Primeiro transporte: diretório local no desktop. Depois, transferência autenticada de pacotes por conexão privada, com SSH/SFTP como candidato. Não implementar sincronização genérica de diretórios pessoais.
- A interface HTTP, se necessária depois, escuta em loopback e usa túnel autenticado. Sem porta pública, UPnP, encaminhamento automático, shell remoto arbitrário ou senha embutida.

Não existe conexão configurada. Login, contas, credenciais e firewall são ações futuras específicas, fora deste bootstrap.

## Manifesto e entradas

UTF-8 JSON, campos desconhecidos rejeitados no MVP. Limites iniciais propostos: 1 MiB por manifesto, até 100 segmentos, até 2.000 caracteres por segmento e até 2 GiB por pacote. Arquivos de vídeo de referência devem ser limitados por duração após sondagem real; teto inicial de 120 segundos.

```json
{
  "schema": "local-presenter/job-v1",
  "job_id": "demo-0001",
  "idempotency_key": "demo-0001-v1",
  "profile_id": "self-demo",
  "visual_adapter": "portrait-candidate",
  "voice_adapter": "multilingual-candidate",
  "segments": [
    {"id": "s01", "text": "A máquina possui cinco estações.", "slide": "assets/slide-01.png"}
  ],
  "assets": [{"path": "assets/slide-01.png", "sha256": "<64-caracteres-hexadecimais>"}],
  "output": {"width": 1920, "height": 1080, "fps": 25}
}
```

O exemplo é ilustrativo e o hash deve ser substituído antes de validação. Referências biométricas residem no perfil local do desktop, não precisam acompanhar cada trabalho. Campos `profile_id` e adaptadores só aceitam entradas de catálogo local; nunca URLs ou caminhos fornecidos livremente.

Todos os caminhos são relativos ao pacote validado. Rejeitar `..`, caminhos absolutos, UNC, unidades Windows, ADS, nomes reservados, symlinks e junctions/reparse points; verificar caminho resolvido antes de leitura/escrita e conter extração de arquivo compactado. Bloquear URLs remotas. Validar extensões e conteúdo com sondagem de mídia e limites de duração/resolução; texto nunca vira código executável.

## Estados, idempotência e concorrência

Estados: `queued -> validating -> voice -> visual -> composing -> review -> completed`. Ramos terminais: `failed` e `cancelled`. `review` não significa aprovação; `completed` exige exportação validada e aprovação dos segmentos previstos.

Mesma chave + mesmo hash de manifesto retorna trabalho existente; mesma chave + conteúdo diferente é conflito. SQLite é candidato para estado/fila, com transações; status JSON é projeção exportável, não segunda fonte de verdade. Um executor GPU por vez e exclusão de execução duplicada após reinício.

## Timeouts, cancelamento e desconexão

Timeouts por estágio são configurados a partir do benchmark local da Fase 1; um teto de segurança não é previsão de desempenho. Proposta inicial: revisão explícita quando o teste de 20 segundos exceder 60 minutos em qualquer estágio. Não iniciar repetição automática ilimitada.

Cancelamento marca pedido durável, interrompe somente árvore de processos do trabalho e fecha recursos. Checkpoint identifica quais estágios estão completos. Desconexão do cliente deixa trabalho continuar no desktop; a reconexão consulta o mesmo ID, sem reenviar automaticamente.

## Resultados, logs e retenção

Exportar manifesto de resultado com schema, hashes das entradas, versões dos adaptadores/checkpoints, dispositivo efetivo, duração de cada estágio, formato/fps/duração do MP4 e estado de aprovação. Seed é registrada quando suportada; não prometer determinismo binário em GPU.

Logs: códigos de erro e métricas, sem texto integral, áudio, rosto, tokens, cabeçalhos de autenticação ou caminhos pessoais. Exceções são sanitizadas; logs brutos, quando indispensáveis, ficam privados e têm retenção explícita. Proposta: temporários até 7 dias após aprovação, sem exclusão automática antes de confirmação; referências e resultados preservados até escolha do dono.

## Aceite e reversão

Antes de mídia pessoal: testar sinteticamente hashes inválidos, caminho fora da raiz, ZIP traversal, reenvio duplicado, reinício após voz, cancelamento durante visual, disco cheio simulado e desconexão. Rede real só é aprovada com transferência pequena, autenticação, retomada e integridade comprovadas entre as máquinas reais.

Rollback: desabilitar consumidor remoto e continuar com pacotes locais. Sem alteração de drivers ou sistema como recuperação automática.
