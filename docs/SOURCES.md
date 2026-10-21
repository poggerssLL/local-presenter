# Fontes técnicas e limites de verificação

Consulta do coordenador: 2026-10-19. São fontes públicas originais, não testes no desktop. Páginas de branch `main/master` e documentação `latest` podem mudar; fixar revisão/versão e hash na Fase 1. Resultados dos agentes são identificados separadamente nos estudos.

## Voz sintetizada em português

[Chatterbox](https://github.com/resemble-ai/chatterbox): código MIT, geração por referência e variante multilíngue com português e pack pt-BR listados. Turbo e Nano são listados como inglês; não escolhê-los para pt-BR só pelo menor tamanho. Conferir licença e disponibilidade do checkpoint específico antes de baixar. CPU aparece como dispositivo possível nos exemplos, mas tempo e qualidade no Ryzen 5 5600 não foram medidos.

## Retrato guiado por áudio

[SadTalker](https://github.com/OpenTalker/SadTalker): usa retrato e áudio para vídeo de rosto falante; README declara código Apache 2.0 e execução offline. O ambiente de referência é antigo e inclui instruções CUDA; o funcionamento completo em AMD/Windows não foi comprovado. Componentes auxiliares e pesos devem entrar em inventário próprio de licenças, sem atribuir automaticamente a licença do código a todos os artefatos.

## Vídeo de referência e sincronização labial

[MuseTalk](https://github.com/TMElyralab/MuseTalk): código MIT e modelos declarados de uso amplo pelo projeto; adapta a região facial ao áudio. O teste publicado de 4 GB usa NVIDIA e não prevê desempenho AMD. Perdas de detalhes faciais e resolução nativa limitada constam das limitações do projeto. Licenças dos auxiliares continuam pendentes.

[Wav2Lip](https://github.com/Rudrabha/Wav2Lip): parte open source destinada a uso pessoal/pesquisa/não comercial. A API comercial mostrada no topo do README não integra a proposta sem assinatura. Não assumir que um futuro aplicativo distribuído pode reutilizar os mesmos pesos livremente.

[LivePortrait](https://github.com/KlingAIResearch/LivePortrait): transfere movimento a partir de vídeo/template. Não considerar o modelo, sozinho, solução de movimento guiado por áudio; entradas e licença dos auxiliares precisam ser avaliadas.

## Rosto 3D e animação

[Blender — licença](https://www.blender.org/about/license/): software GPL; arquivo de trabalho e vídeo produzidos têm tratamento distinto do código do aplicativo. A página não pôde ser aberta diretamente nesta sessão; o conteúdo sobre licença foi localizado pela busca na fonte original. Confirmar versão e termos na adoção, sem tratar esta anotação como parecer jurídico.

[Blender — suporte RDNA3 no Cycles](https://developer.blender.org/docs/release_notes/3.4/cycles/): evidencia caminho de render HIP para a família RX 7000; não prova que a versão instalada, driver e cena funcionarão no desktop. Renderizar uma malha e executar redes neurais em PyTorch são problemas diferentes.

[Rhubarb Lip Sync](https://github.com/DanielSWolf/rhubarb-lip-sync): produz marcações de boca a partir de áudio; [licença](https://github.com/DanielSWolf/rhubarb-lip-sync/blob/master/LICENSE.md) e dependências devem ser revisadas. Converter as marcações para blendshapes/visemas do rig é trabalho adicional. Avaliar reconhecedor fonético em pt-BR; não presumir alinhamento perfeito.

[Meshroom](https://github.com/alicevision/Meshroom): candidato de fotogrametria, com [documentação de requisitos](https://meshroom-manual.readthedocs.io/en/latest/faq/needs-cuda/needs-cuda.html) apontando exigência NVIDIA/CUDA no caminho denso tradicional. Não escolher esse fluxo para RX 7600 sem verificar alternativa específica e versão. Uma malha reconstruída continua sem rig.

## Compatibilidade AMD

[HIP SDK para Windows](https://github.com/ROCm/rocm-install-on-windows/blob/develop/docs/reference/system-requirements.rst): a RX 7600 consta como `gfx1102`, com suporte de runtime/HIP SDK no documento consultado. Não é certificado de suporte PyTorch ou dos três pipelines.

[Matriz legada Radeon/PyTorch](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/windows/windows_compatibility.html): cobre até 7.2.1. [Matriz unificada 7.14.0](https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/docs-7.14.0/compatibility/compatibility-matrix.html): a página exibe suporte a famílias/arquiteturas, mas a extração textual não permite concluir a configuração específica completa de RX 7600 e framework. Revalidar a seleção exata no início da implementação.

Não confundir: GPU listada no HIP SDK, pacote framework disponível, extensões compiladas compatíveis e geração completa aprovada são quatro evidências distintas. Linux, WSL, DirectML ou camadas de tradução não são cura automática.
