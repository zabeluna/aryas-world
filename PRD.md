# PRD — Arya's Adventure

## 1. História do Jogo

**Arya** é uma cachorra corajosa que precisa atravessar a cidade para chegar à casa da sua vovó.
O caminho é cheio de ruas movimentadas, carros perigosos e distrações. Mas Arya não desiste —
ela coleta galhos pelo caminho (seu brinquedo favorito!), conversa com pessoas e outros cães
que encontra, e usa sua esperteza para desviar dos carros e chegar em segurança.

**Objetivo:** Guiar Arya do ponto inicial até a casa da vovó, coletando galhos e atravessando
o trânsito caótico da cidade.

---

## 2. Personagens

| Personagem | Tipo | Descrição |
|---|---|---|
| Arya | Player | Cachorra protagonista. Move-se por teclado e clique. Possui skill de desvio. |
| Pessoas / Cães | NPCs | Oferecem dicas e diálogos que ajudam (ou atrapalham) a jornada. |
| Carros | Obstáculos móveis | Percorrem rotas fixas nas ruas e exigem desvio do jogador. |

---

## 3. Requisitos Funcionais

### RF01 — Movimentação do Player
- Arya se move via teclado (WASD ou setas).
- Arya também se move via clique no mapa (pathfinding automático).
- A câmera segue Arya pelo mapa.

### RF02 — Pathfinding (A*)
- Ao clicar em um ponto do mapa, o algoritmo A* calcula a rota mais curta desviando de obstáculos (paredes, prédios, etc.).
- Arya percorre o caminho calculado automaticamente.

### RF02.1 — Rota Ótima de Coleta (TSP)
- O jogo calcula a melhor ordem para coletar todos os galhos restantes no mapa.
- Para até 15 pontos, usa Held-Karp como solução exata do Travelling Salesman Problem.
- Para mais de 15 pontos, usa heurística de vizinho mais próximo com melhoria 2-opt.
- A rota é desenhada no mapa e pode ser ligada/desligada com a tecla R.

### RF03 — Sistema de Skill (Desvio)
- Arya possui uma skill de **Desvio Rápido** (dash/esquiva).
- Ativada por tecla (ex: Espaço ou Shift).
- Possui cooldown para não ser usada infinitamente.
- Permite desviar rapidamente dos carros e ajustar a rota.

### RF04 — Carros
- Carros percorrem rotas fixas nas ruas (patrulha).
- Funcionam como obstáculos móveis para leitura de rota e desvio.
- Não causam dano nem encerram a fase por colisão.

### RF05 — Itens Coletáveis (Galhos)
- Galhos estão espalhados pelo mapa.
- Arya coleta ao passar por cima.
- Os galhos são armazenados no inventário.

### RF06 — Inventário
- Exibe os galhos coletados.
- Implementa algoritmo de ordenação (QuickSort) para ordenar itens por nome ou quantidade.
- Permite filtrar itens por tipo.
- Permite adicionar, remover, contar e consultar itens.

### RF07 — NPCs e Árvore de Diálogo
- Pessoas e cães espalhados pelo mapa.
- Ao se aproximar e pressionar E, Arya inicia diálogo.
- O diálogo segue uma estrutura de **árvore**: o jogador escolhe respostas e o fluxo muda.
- Alguns NPCs dão dicas sobre o mapa ou desbloqueiam atalhos.

### RF08 — Condição de Vitória
- Arya chega à casa da vovó → tela de vitória com contagem de galhos coletados.

### RF09 — HUD
- Contador de galhos coletados.
- Indicador de cooldown da skill.
- Estado da visualização da rota TSP.

---

## 4. Requisitos Não-Funcionais

### RNF01 — Portabilidade
- O jogo deve rodar em qualquer sistema com Python 3.8+.
- Instalação via: `pip install -r requirements.txt`
- Execução via: `python main.py`

### RNF02 — Performance
- Rodar a no mínimo 30 FPS em hardware comum.

### RNF03 — Arte 2D
- Arya usa a imagem `arya.png` como sprite principal.
- O cenário deve ter leitura visual 2D clara, com ruas, prédios, casa da vovó, carros e coletáveis desenhados.
- O dash deve ter feedback visual.

### RNF04 — Organização do Código
- Estrutura modular por pastas.
- Cada sistema deve ficar em seu próprio arquivo.

## 5. Algoritmos Computacionais

| Algoritmo | Uso no jogo | Complexidade |
|---|---|---|
| TSP (Held-Karp) | Rota ótima dos galhos restantes | O(n²·2ⁿ) |
| TSP heurístico (vizinho mais próximo + 2-opt) | Rota aproximada para muitos pontos | O(n²) por melhoria |
| QuickSort | Ordenação dos itens do inventário | O(n log n) médio |
| A* | Caminho por clique no mapa | Depende do número de tiles explorados |

## 6. Organização do Repositório

- Issues documentadas em `docs/issues`.
- Justificativa algorítmica em `docs/ALGORITHMS.md`.
- Instruções de execução em `README.md`.

## 7. Stack Tecnológica

| Tecnologia | Uso |
|---|---|
| Python 3.8+ | Linguagem principal |
| Pygame | Engine de jogo 2D |
| JSON | Dados de diálogo e save |
| Aseprite / Piskel | Criação de sprites |
| Git + GitHub | Controle de versão |
