# Prompt preparado — Fase 1, ainda não autorizado nem despachado

Este documento prepara uma possível etapa futura; não cria permissão ou tarefa. A pesquisa documental B/C de 2026-10-23 foi concluída, mas a escolha explícita de um piloto permanece pendente. Plano: [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md). Adaptar o prompt ao visual escolhido e aplicar somente após autorização expressa para executar a Fase 1 e acesso disponibilizado pelo proprietário ao desktop.

```text
Atue somente no projeto Local Presenter e na Fase 1: prova de compatibilidade e piloto de 20 segundos.

Antes de agir, confirme a raiz Git, AGENTS.md, branch, HEAD/upstream e working tree atuais. Há um snapshot documental publicado; revalide o estado corrente e preserve mudanças preexistentes. Leia docs/BRIEF.md uma vez e consulte docs/IMPLEMENTATION_PLAN.md, docs/VALIDATION.md e docs/SOURCES.md quando necessários à tarefa.

Executor/modelo/esforço: resolver no início conforme preferência do proprietário e capacidade efetiva do runtime; fallback none. Não reutilizar IDs/autorizações dos três planejadores. Se houver delegação, usar despacho real com leitores de compatibilidade/licença em paralelo e um único experimentador. Não prometer modelo indisponível.

Objetivo único: demonstrar ou rejeitar, com evidência, um pipeline local de voz sintetizada em pt-BR e visual próprio pela abordagem B ou C explicitamente escolhida no desktop Windows 11/RX7600 8GB/Ryzen5600/RAM24GB, seguido de composição com um slide em vídeo de 20 s.

Comece com diagnóstico somente leitura. Antes de qualquer instalação/download, registre candidatos, versões, licenças, URLs, limites de disco e envelope explicitamente aprovado. Instalações autorizadas ficam em ambientes locais isolados; nunca globalmente ou com administração. Não instalar drivers, dual boot, camadas de tradução ou modificar firewall sem autorização específica. Fotos/áudios próprios só após o dono fornecê-los para esse teste e ficam fora do Git.

Escopo de escrita, quando aprovado: ferramentas de diagnóstico/experimento, docs/COMPATIBILITY.md e relatório sanitizado da Fase1. Pesos, ambientes, referências e saídas apenas em diretórios ignorados. Sem UI, fila remota, instalador, integração com Automática ou apresentação completa.

Selecionar um TTS multilíngue candidato e o visual B ou C aprovado após a pesquisa. A está descartada para aplicação. CPU e AMD são opções a validar; não trocar automaticamente. HIP SDK não prova PyTorch, operadores nem inferência. Não aplicar overrides de arquitetura. Testar operações pequenas antes do modelo completo, sem alocar gigabytes artificialmente.

Validar pronúncia técnica, timbre, prosódia, identidade visual, sincronismo, formato e duração conforme docs/VALIDATION.md. Registrar tempos/memória realmente medidos e método. Resultado humano do proprietário é obrigatório para semelhança. Teste com áudio gravado ou fake não comprova síntese nova.

Limites: um trabalho GPU por vez; primeira comparação de pilha limitada a4h antes de replanejar; sem repetição infinita, custos pagos, controle visual, acesso a outros projetos, credenciais em logs ou publicação. Se a pilha falhar, informar dependência e menor próximo experimento; não instalar Linux como tentativa cega.

Resposta: observado/informado/proposto/não testado separados, versões, arquivos alterados, teste real20s ou causa de bloqueio, decisão do gate, Git e próxima ação delimitada. Não fazer commit/push sem pedido específico e não iniciar Fase2.
```
