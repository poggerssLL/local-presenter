# Abordagem C — rosto 3D simplificado

Origem: estudo real de planejador Antigravity / Gemini 3.8 Flash High / esforço high, entregue em 2026-10-19. Síntese editada pelo coordenador após [revisão](../REVIEW.md); não transcrição literal. Sem modelagem, render ou inferência executados. Contexto: [briefing](../BRIEF.md). Fontes: [inventário](../SOURCES.md).

## Proposta e valor do 3D

Criar uma cabeça simplificada com aparência aproximada do proprietário, textura e formas de boca animáveis; dirigir a animação pelo áudio sintetizado e renderizar junto aos slides. A vantagem proposta é controlar câmera, luz e expressões. O custo adicional é preparar um ativo facial funcional.

Um escaneamento estático fornece superfície e textura, não um personagem pronto para falar. A boca precisa abrir e fechar, manter volume e, conforme o estilo, revelar interior simples. São necessários rig e/ou shape keys, com transições entre visemas. Não é obrigatório modelar dentes e língua detalhados para um avatar estilizado, e nem toda malha escaneada tem os mesmos defeitos de topologia.

## Aquisição e opções de construção

Proposta inicial: fotos frontal, de três quartos e de perfil, sem expressão forte e com luz uniforme. Servem para proporção e textura; não constituem escaneamento volumétrico preciso. Voz é adquirida pelo mesmo contrato das demais abordagens.

Dois subcaminhos distintos:

- **Malha base pré-preparada:** ajustar proporções e textura a partir de referências, reduzindo o trabalho de rig. MakeHuman/MPFB foram sugeridos pelo agente, mas versões, código, ativos e licenças precisam ser verificados antes da escolha.
- **Reconstrução real por fotos:** estimar superfície, limpar e adaptar topologia, criar rig e calibrar boca. É escopo maior. Meshroom não é selecionado automaticamente, pois o caminho denso tradicional tem requisitos CUDA que não foram comprovados na placa alvo.

Marcos faciais de uma imagem podem ajudar a ajustar proporções, mas não recuperam geometria exata e partes invisíveis. Não adotar MediaPipe/ONNX como integração pronta sem conferir a API, o modelo e a licença efetivos.

## Pipeline proposto

1. Preparar malha/textura e testar repouso, abertura e fechamento de boca.
2. Gerar e aprovar voz sintetizada com semelhança ao proprietário.
3. Obter marcações temporais de boca; Rhubarb é candidato CPU, com reconhecimento fonético a avaliar em português.
4. Mapear marcações para shape keys/visemas do rig, com interpolação ajustável.
5. Adicionar piscadas e movimentos moderados, sem alegar reprodução do gestual pessoal.
6. Render Blender por CLI e compor com os slides.

A capacidade de render HIP da família RX 7000 é diferente do suporte dos modelos neurais. CPU e render simplificado são alternativas de teste, não garantia do pipeline completo. Verificar separadamente licença do Blender, ativos, addon, marcações e voz.

## Contratos e gates

Compartilhar [trabalhos](../REMOTE_JOBS.md), [arquitetura](../ARCHITECTURE.md) e [validação](../VALIDATION.md). Perfil 3D armazena ativo e versão do mapeamento de visemas, permitindo reutilização local sem refazer a cabeça por apresentação.

- Gate C1: referência aprovada e cabeça reconhecível em repouso.
- Gate C2: poses de boca sem rasgos, interpenetração persistente ou fechamento impossível.
- Gate C3: fala nova de 20 segundos; avaliar visemas, identidade e recursos.
- Gate C4: minuto com transições, render e composição aprovados.

## Esforço e condições de escolha

O esforço manual provavelmente será maior que em A/B por exigir ativo animável, mas a razão de “3 a 5 vezes” sugerida pelo agente não foi comprovada e não é usada como orçamento. Proposta de limite experimental: até 8 horas de ajuste inicial antes de decidir continuar; é limite de investimento, não promessa de conclusão.

Escolher C se o proprietário preferir estilo 3D, se houver valor em controlar expressões/câmera ou se a prova de conceito mostrar vantagem concreta. Não promover C automaticamente quando A/B falharem por um problema vocal compartilhado. Riscos principais: semelhança insuficiente, aparência artificial, tempo de rig e pronúncia/voz ainda pendentes.
