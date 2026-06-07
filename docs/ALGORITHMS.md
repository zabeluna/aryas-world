# Justificativa Algoritmica

## TSP: rota otima de coleta

O TSP foi escolhido como mecanica central porque o mapa possui varios galhos coletaveis e o jogador se beneficia de uma ordem de visita eficiente. A rota amarela desenhada no mapa parte da posicao atual de Arya e visita todos os galhos restantes.

- Ate 15 pontos: Held-Karp, solucao exata por programacao dinamica, complexidade `O(n^2 * 2^n)`.
- Acima de 15 pontos: vizinho mais proximo + 2-opt, solucao heuristica mais barata para fases grandes.

Essa divisao permite discutir o trade-off entre otimalidade e desempenho.

## Inventario e QuickSort

O inventario armazena os itens coletados em uma lista e oferece operacoes de adicionar, remover, consultar, contar e filtrar. A cada insercao, os itens sao ordenados por nome com QuickSort.

O QuickSort foi usado como segundo problema computacional porque ele aparece diretamente no gameplay: os galhos coletados sao exibidos no inventario ja organizados, facilitando leitura e contagem.

## A*

O A* calcula o caminho entre a posicao de Arya e o ponto clicado no mapa. Ele usa distancia Manhattan como heuristica e evita tiles marcados como obstaculo.

Embora nao seja o requisito principal, ele reforca o uso de grafos no jogo e melhora a navegacao do jogador.
