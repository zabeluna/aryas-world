# src/monster.py
import pygame

CAR_SPEED = 120

class Car:
    def __init__(self, x, y, route):
        self.rect = pygame.Rect(x, y, 48, 24)
        self.route = route        # Lista de (x, y) waypoints
        self.route_index = 0
        self.color = (220, 50, 50)

    def update(self, dt):
        if not self.route:
            return
        tx, ty = self.route[self.route_index]
        dx = tx - self.rect.centerx
        dy = ty - self.rect.centery
        dist = (dx**2 + dy**2) ** 0.5
        if dist < 4:
            self.route_index = (self.route_index + 1) % len(self.route)
        else:
            nx, ny = dx/dist, dy/dist
            self.rect.x += int(nx * CAR_SPEED * dt)
            self.rect.y += int(ny * CAR_SPEED * dt)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
        # Janelas
        win = pygame.Rect(self.rect.x + 6, self.rect.y + 4, 14, 10)
        pygame.draw.rect(screen, (180, 220, 255), win, border_radius=2)
        # Rodas
        for wx in [self.rect.x + 4, self.rect.right - 14]:
            pygame.draw.circle(screen, (30, 30, 30),
                               (wx + 5, self.rect.bottom + 2), 5)