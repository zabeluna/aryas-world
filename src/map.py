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
        self.wall_color = (156, 165, 188)
        self.road_color = (84, 91, 98)
        self.sidewalk_color = (190, 195, 188)
        self.grass_color = (92, 166, 96)

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
        screen.fill(self.grass_color)
        for row_i, row in enumerate(self.grid):
            for col_i, cell in enumerate(row):
                rect = pygame.Rect(col_i * ts, row_i * ts, ts, ts)
                if cell == 1:
                    self._draw_building_tile(screen, rect, row_i, col_i)
                else:
                    self._draw_road_tile(screen, rect, row_i, col_i)

        self._draw_crosswalk(screen, 4, 4, horizontal=True)
        self._draw_crosswalk(screen, 17, 8, horizontal=True)
        self._draw_crosswalk(screen, 10, 13, horizontal=False)

    def _draw_road_tile(self, screen, rect, row_i, col_i):
        pygame.draw.rect(screen, self.road_color, rect)

        if row_i in (4, 8, 13, 17) and col_i % 2 == 0:
            lane = pygame.Rect(rect.centerx - 8, rect.centery - 2, 16, 4)
            pygame.draw.rect(screen, (232, 218, 128), lane, border_radius=2)

        if col_i in (0, 4, 10, 16, 23):
            curb = pygame.Rect(rect.left, rect.top, 3, rect.height)
            pygame.draw.rect(screen, self.sidewalk_color, curb)

        if (row_i + col_i) % 11 == 0:
            patch = pygame.Rect(rect.x + 7, rect.y + 7, 7, 7)
            pygame.draw.ellipse(screen, (111, 190, 108), patch)

    def _draw_building_tile(self, screen, rect, row_i, col_i):
        palette = [
            ((176, 184, 204), (120, 130, 160)),
            ((205, 175, 145), (158, 116, 106)),
            ((168, 196, 188), (96, 143, 143)),
            ((198, 190, 154), (142, 132, 100)),
        ]
        body, outline = palette[(row_i + col_i) % len(palette)]
        pygame.draw.rect(screen, body, rect)
        pygame.draw.rect(screen, outline, rect, 1)

        roof = pygame.Rect(rect.x + 3, rect.y + 3, rect.width - 6, 7)
        pygame.draw.rect(screen, outline, roof, border_radius=2)

        if row_i % 2 == 0:
            window_color = (235, 238, 205)
        else:
            window_color = (160, 210, 230)
        for wx in (rect.x + 7, rect.x + 19):
            window = pygame.Rect(wx, rect.y + 15, 6, 7)
            pygame.draw.rect(screen, window_color, window, border_radius=1)

    def _draw_crosswalk(self, screen, col, row, horizontal=True):
        x = col * self.tile_size
        y = row * self.tile_size
        stripe_color = (230, 232, 222)
        for i in range(5):
            if horizontal:
                stripe = pygame.Rect(x + i * 12, y + 5, 7, 22)
            else:
                stripe = pygame.Rect(x + 5, y + i * 12, 22, 7)
            pygame.draw.rect(screen, stripe_color, stripe)
