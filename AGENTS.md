# Local Presenter — regras do projeto

- Responda em português; comece mensagens ao proprietário com `Erick,`.
- Fase atual: planejamento após pesquisa documental de B e C; a escolha do piloto está pendente. A está preservada como estudo histórico e descartada para aplicação por decisão do proprietário em 2026-10-23. Nenhuma abordagem foi validada na máquina alvo.
- Não implementar a aplicação, instalar dependências, baixar pesos, capturar rosto/voz ou configurar acesso remoto nesta fase.
- Na primeira orientação da sessão, agrupe raiz Git, branch, HEAD, upstream e status em uma consulta. Leia `docs/BRIEF.md` uma vez; depois consulte apenas documentos ligados à tarefa, sem relê-los a cada passo.
- Roteamento: decisão de abordagem ou fase → `docs/IMPLEMENTATION_PLAN.md`; pesquisa B/C → `docs/approaches/B_REFERENCE_VIDEO.md` ou `C_FACE_3D.md` e `docs/SOURCES.md`; contratos → `docs/ARCHITECTURE.md` e `docs/REMOTE_JOBS.md`; gates → `docs/VALIDATION.md`. Relatórios históricos e saídas geradas ficam fora da leitura padrão.
- Um escritor por checkout: coordenador Codex. Pesquisadores delegados são somente leitura e entregam evidências e conclusões na resposta e no `worker_done`, sem criar arquivos.
- Os três planejadores Antigravity / `gemini-3.8-flash-high` / `high` foram a onda de 2026-10-19, não uma regra permanente. Na pesquisa de 2026-10-23, o proprietário pediu Argon e Sol 6.1, ambos em esforço médio. Use os perfis efetivos pedidos e `fallback: none`; não substitua silenciosamente.
- Não ler outros projetos ou diretórios pessoais. Não registrar credenciais, caminhos pessoais, IDs de runtime, fotos, áudios, modelos, transcrições pessoais ou logs brutos no Git.
- Arquivos privados e gerados permanecem nos diretórios ignorados. O repositório contém somente documentação sanitizada e ferramentas locais de documentação.
- Não fazer commit, push, merge, alteração destrutiva, login, publicação de conteúdo ou exposição de serviço sem autorização explícita. Em 2026-10-21, o proprietário autorizou o commit inicial, push do snapshot documental e mudança do repositório para público. Essa autorização não inicia a implementação nem libera dados privados.
- Preferir arquivos, CLI e APIs; controle visual proibido. Dependências de modelos e GPU precisam de validação real antes de qualquer promessa de desempenho.
- Distinguir evidência primária, informação do proprietário, proposta, mock e execução real. Hardware remoto ainda não foi inspecionado.
- Graphify: consultar o grafo local quando existir e confirmar no documento original. Construção local determinística; sem provedor externo. Um grafo documental não comprova código ou inferência implementados.
- Pare após entregar a tarefa delimitada. Novos agentes ou fases exigem pedido específico; a pesquisa B/C de 2026-10-23 foi pedida explicitamente.
