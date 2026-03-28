# src/map.py
import pygame

class GameMap:
    def __init__(self, path=None):
        self.tile_size = 32
        # Grid simples: 0 = livre, 1 = obstáculo (prédio/calçada)
        # 25 colunas x 19 linhas para 800x600
        self.grid = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
            [0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
            [0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0],
            [0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0],
            [0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0],
            [0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0],
            [0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.wall_color  = (150, 150, 180)
        self.road_color  = (100, 100, 110)
        self.grass_color = (80, 160, 80)

    def collides(self, rect):
        ts = self.tile_size
        corners = [
            (rect.left,  rect.top),
            (rect.right-1, rect.top),
            (rect.left,  rect.bottom-1),
            (rect.right-1, rect.bottom-1),
        ]
        for cx, cy in corners:
            col = cx // ts
            row = cy // ts
            if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                if self.grid[row][col] == 1:
                    return True
        return False

    def draw(self, screen):
        ts = self.tile_size
        for row_i, row in enumerate(self.grid):
            for col_i, cell in enumerate(row):
                rect = pygame.Rect(col_i * ts, row_i * ts, ts, ts)
                if cell == 1:
                    pygame.draw.rect(screen, self.wall_color, rect)
                    pygame.draw.rect(screen, (120,120,150), rect, 1)