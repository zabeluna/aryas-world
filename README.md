# Arya's Adventure

Jogo 2D de aventura/exploracao em que Arya atravessa a cidade ate a casa da vovo, coleta galhos e desvia de carros.

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

## Controles

- `WASD` ou setas: mover Arya
- Clique esquerdo: mover ate um ponto usando A*
- `Espaco` ou `Shift`: desvio rapido
- `F`: arremessar um galho coletado para parar um carro por alguns segundos
- `L`: abrir/fechar inventario
- `R`: mostrar/ocultar rota TSP dos galhos restantes
- `E`: conversar com NPC proximo

## Algoritmos implementados

- **Travelling Salesman Problem (TSP):** calcula a menor ordem de coleta dos galhos restantes. Para ate 15 pontos usa Held-Karp exato; acima disso usa vizinho mais proximo com refinamento 2-opt.
- **QuickSort no inventario:** mantem os itens coletados ordenados por nome apos cada coleta.
- **A\* pathfinding:** movimenta Arya por clique desviando dos obstaculos do mapa.

## Genero

Aventura/exploracao com coleta e planejamento de rota. Nao e survivor.

## Organizacao

As issues planejadas estao documentadas em [`docs/issues`](docs/issues). A justificativa das escolhas algoritmicas esta em [`docs/ALGORITHMS.md`](docs/ALGORITHMS.md).
