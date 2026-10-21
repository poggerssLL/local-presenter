# Entrega documental e proveniência

Data: 2026-10-19. Projeto independente: Local Presenter. Estado: somente planejamento revisado, Git inicial e ferramenta de documentação. O produto audiovisual ainda não foi implementado. [Plano](IMPLEMENTATION_PLAN.md), [revisão](REVIEW.md) e [grafo](GRAPH.md).

## O que foi observado nesta sessão

- Pasta nova e raiz Git própria, branch `main`, sem commits ou upstream; não é subdiretório do repositório Organizer nem do projeto de Automática.
- Repositório GitHub novo criado como privado, com `origin` local configurado. Consulta confirmou remoto vazio.
- Catálogo Antigravity expôs `gemini-3.8-flash-high`.
- Três workers reais começaram em paralelo no Orca, com recibos `launch.effective` confirmando Antigravity, modelo solicitado e esforço high.
- Os três entregaram estudos e `worker_done` com resultado succeeded. O coordenador aceitou contribuições após corrigir afirmações insuficientes; sucesso operacional não é homologação técnica dos modelos.
- Os três receberam `worker-release`; consulta final mostrou três released, nenhum ativo/reclaimable.
- Codex coordenador foi o único escritor, integrou os estudos, conferiu fontes primárias e construiu a documentação e o gerador do grafo.

## O que permanece informado ou proposto

Hardware Windows/RX 7600/Ryzen/RAM é informação do proprietário. Acesso remoto, ambientes, frameworks e drivers não foram inspecionados no desktop. Abordagem A é candidata prioritária; B e C são alternativas planejadas. Esforço, limites e critérios são propostas sem benchmark local.

## O que não foi executado

Sem instalação de dependências de produto, download de pesos, captura de rosto/voz, clonagem, render facial, benchmark AMD/CPU, SSH/VPN/firewall, Linux/dual boot ou alteração do projeto acadêmico. Não houve envio de mídia pessoal para os agentes ou serviço externo de IA. O Graphify usa bibliotecas já instaladas e extração documental determinística, sem API para a construção do grafo.

Sem commit, push, merge ou publicação dos arquivos. A autorização de criação de GitHub foi cumprida criando o remoto privado; a regra global de commit/push continua vigente. Para enviar o conteúdo, revisar o snapshot final e solicitar autorização específica sobre esse conjunto de arquivos.

## Localização da evidência

Documentos e estudos sanitizados ficam em `docs/`. A relação de documentos e seus SHA-256 está em `graphify-out/coverage.json`. Verificações finais da entrega ficam em `graphify-out/verification.json`, quando geradas. Recibos/IDs e mensagens brutas ficam somente no runtime ignorado e no histórico do Orca; não integram os arquivos candidatos a Git.

O [guia do grafo](GRAPH.md) explica como reproduzir a geração e o seu limite estrutural. Não houve inspeção visual por navegador nesta fase. Grafo e relatório não substituem a leitura do plano ou testes reais.

## Próxima ação delimitada

Revisar o plano e autorizar uma etapa por vez. [Prompt preparado da Fase 1](NEXT_PHASE_PROMPT.md), ainda não executado. Abertura de outra etapa, publicação do snapshot ou acesso ao desktop requer o pedido correspondente.

## Atualização de publicação — 2026-10-21

O proprietário autorizou expressamente o commit inicial, o push e a mudança de visibilidade para público. O escopo da publicação é o snapshot de planejamento, os três estudos revisados e o grafo documental com seu gerador local. O relato de 2026-10-19 acima preserva o estado anterior à autorização.

README, regras operacionais e plano foram alinhados com o novo pedido. O grafo é regenerado após essa atualização para manter a cobertura documental atual. Os checks de publicação incluem links locais, hashes de cobertura, integridade do grafo, inspeção do conjunto preparado e ausência de caminhos pessoais, credenciais, mídia, pesos e runtime no Git. A identidade de commit utiliza o endereço noreply da conta GitHub autenticada.

Nenhuma implementação, instalação, inferência, validação do desktop ou configuração remota foi iniciada. A próxima etapa técnica continua sendo a Fase 1, mediante pedido específico.
