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
        shadow = pygame.Rect(self.rect.x + 3, self.rect.y + 4, self.rect.width, self.rect.height)
        pygame.draw.rect(screen, (48, 48, 52), shadow, border_radius=7)

        pygame.draw.rect(screen, self.color, self.rect, border_radius=7)
        pygame.draw.rect(screen, (130, 30, 35), self.rect, 2, border_radius=7)

        cabin = pygame.Rect(self.rect.x + 12, self.rect.y + 3, 24, 11)
        pygame.draw.rect(screen, (180, 220, 255), cabin, border_radius=3)
        pygame.draw.line(screen, (85, 120, 150), cabin.center, (cabin.centerx, cabin.bottom), 1)

        pygame.draw.circle(screen, (255, 235, 120), (self.rect.right - 4, self.rect.y + 8), 3)
        pygame.draw.circle(screen, (255, 120, 100), (self.rect.left + 4, self.rect.y + 8), 3)

        for wx in [self.rect.x + 6, self.rect.right - 16]:
            pygame.draw.circle(screen, (24, 24, 26), (wx + 5, self.rect.bottom), 5)
            pygame.draw.circle(screen, (105, 105, 110), (wx + 5, self.rect.bottom), 2)
