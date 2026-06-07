# Implementar TSP para rota otima de coleta

Labels sugeridas: `algoritmo`, `gameplay`, `mapa`

## Descricao

Calcular a menor rota que parte da posicao atual de Arya e passa por todos os galhos restantes no mapa. A rota deve ser exibida visualmente para orientar o jogador durante a coleta.

## Criterios de aceitacao

- [x] Algoritmo recebe lista de coordenadas dos coletaveis e ponto inicial do jogador
- [x] Retorna ordem de visitacao
- [x] Para `n <= 15` usa solucao exata Held-Karp
- [x] Para `n > 15` usa heuristica vizinho mais proximo + 2-opt
- [x] Rota e desenhada visualmente no mapa
- [x] Jogador pode mostrar/ocultar a rota com tecla `R`

## Problema computacional

Travelling Salesman Problem.

## Justificativa

O TSP integra planejamento de rota ao gameplay de coleta e permite comparar solucao exata `O(n^2 * 2^n)` com heuristicas mais escalaveis.
