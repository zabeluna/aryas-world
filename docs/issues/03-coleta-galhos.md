# Implementar coleta de galhos no mapa

Labels sugeridas: `gameplay`, `inventario`, `mapa`

## Descricao

Espalhar galhos pelo mapa e permitir que Arya colete os itens ao encostar neles. Cada galho coletado deve ser removido do mundo e adicionado ao inventario.

## Criterios de aceitacao

- [x] Galhos aparecem no mapa
- [x] Colisao entre Arya e galho dispara coleta
- [x] Galho coletado desaparece do mapa
- [x] Inventario recebe o item `Galho`
- [x] Contador do HUD atualiza apos coleta
- [x] Rota TSP atualiza considerando apenas galhos restantes

## Problema computacional

Deteccao de colisao entre retangulos e atualizacao de lista de coletaveis.

## Justificativa

A coleta conecta o mundo do jogo ao inventario e torna a rota calculada pelo TSP util para a tomada de decisao do jogador.
