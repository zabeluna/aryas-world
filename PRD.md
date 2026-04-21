# PRD - Arya's World

## 1. História do Jogo

**Arya** é uma cachorra corajosa que precisa atravessar a cidade para chegar à casa da sua vovó.
O caminho é cheio de ruas movimentadas, carros perigosos e distrações. Mas Arya não desiste,
ela coleta galhos pelo caminho (seu brinquedo favorito!), conversa com pessoas e outros cães
que encontra, e usa sua esperteza para desviar dos carros e chegar em segurança.

**Objetivo:** Guiar Arya do ponto inicial até a casa da vovó, coletando galhos e sobrevivendo
ao trânsito caótico da cidade.

---

## 2. Personagens

| Personagem | Tipo | Descrição |
|---|---|---|
| Arya | Player | Cachorra protagonista. Move-se por teclado e clique. Possui skill de desvio. |
| Pessoas / Cães | NPCs | Oferecem dicas e diálogos que ajudam (ou atrapalham) a jornada. |
| Carros | Monstros | Percorrem rotas fixas nas ruas. Causam dano por colisão. |

---

## 3. Requisitos Funcionais

### RF01 - Movimentação do Player
- Arya se move via teclado (WASD ou setas).
- Arya também se move via clique no mapa (pathfinding automático).
- A câmera segue Arya pelo mapa.

### RF02 - Pathfinding (A*)
- Ao clicar em um ponto do mapa, o algoritmo A* calcula a rota mais curta desviando de obstáculos (paredes, prédios, etc.).
- Arya percorre o caminho calculado automaticamente.

### RF03 - Sistema de Skill (Desvio)
- Arya possui uma skill de **Desvio Rápido** (dash/esquiva).
- Ativada por tecla (ex: Espaço ou Shift).
- Possui cooldown para não ser usada infinitamente.
- Permite escapar de colisão com carros em situações de perigo.

### RF04 - Monstros (Carros)
- Carros percorrem rotas fixas nas ruas (patrulha).
- Ao colidir com Arya, causam dano (reduz HP).
- Se o HP chegar a zero, o jogo reinicia a fase.

### RF05 - Itens Coletáveis (Galhos)
- Galhos estão espalhados pelo mapa.
- Arya coleta ao passar por cima.
- Os galhos são armazenados no inventário.

### RF06 - Inventário
- Exibe os galhos coletados.
- Implementa algoritmo de ordenação (QuickSort) para ordenar itens por nome ou quantidade.
- Permite filtrar itens por tipo.

### RF07 - NPCs e Árvore de Diálogo
- Pessoas e cães espalhados pelo mapa.
- Ao se aproximar e pressionar E, Arya inicia diálogo.
- O diálogo segue uma estrutura de **árvore**: o jogador escolhe respostas e o fluxo muda.
- Alguns NPCs dão dicas sobre o mapa ou desbloqueiam atalhos.

### RF08 - Condição de Vitória
- Arya chega à casa da vovó → tela de vitória com contagem de galhos coletados.

### RF09 - HUD
- Barra de HP de Arya.
- Contador de galhos coletados.
- Indicador de cooldown da skill.

---

## 4. Requisitos Não-Funcionais

### RNF01 - Portabilidade
- O jogo deve rodar em qualquer sistema com Python 3.8+.
- Instalação via: `pip install -r requirements.txt`
- Execução via: `python main.py`

### RNF02 - Performance
- Rodar a no mínimo 30 FPS em hardware comum.

### RNF03 - Arte Original
- Todos os sprites e animações criados do zero (pixel art).
- Animações obrigatórias: idle, walk, dash, hit.
- Ferramenta sugerida: Aseprite ou Piskel (gratuito online).

### RNF04 - Organização do Código
- Estrutura modular por pastas (ver seção 6).
- Cada sistema em seu próprio arquivo.


## 5. Stack Tecnológica

| Tecnologia | Uso |
|---|---|
| Python 3.8+ | Linguagem principal |
| Pygame | Engine de jogo 2D |
| JSON | Dados de diálogo e save |
| Aseprite / Piskel | Criação de sprites |
| Git + GitHub | Controle de versão |
