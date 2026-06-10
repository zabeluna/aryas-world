import pygame


STICK_PROJECTILE_SPEED = 420
STICK_PROJECTILE_LIFETIME = 1.1


class StickProjectile:
    def __init__(self, x, y, direction):
        dx, dy = direction
        length = (dx * dx + dy * dy) ** 0.5
        if length == 0:
            dx, dy = 1, 0
            length = 1

        self.x = float(x)
        self.y = float(y)
        self.dx = dx / length
        self.dy = dy / length
        self.timer = STICK_PROJECTILE_LIFETIME
        self.rect = pygame.Rect(0, 0, 18, 8)
        self.rect.center = (int(self.x), int(self.y))

    def update(self, dt):
        self.timer -= dt
        self.x += self.dx * STICK_PROJECTILE_SPEED * dt
        self.y += self.dy * STICK_PROJECTILE_SPEED * dt
        self.rect.center = (int(self.x), int(self.y))

    def is_expired(self, bounds):
        return self.timer <= 0 or not bounds.colliderect(self.rect)

    def draw(self, screen):
        start = (
            int(self.rect.centerx - self.dx * 8),
            int(self.rect.centery - self.dy * 4),
        )
        end = (
            int(self.rect.centerx + self.dx * 8),
            int(self.rect.centery + self.dy * 4),
        )
        pygame.draw.line(screen, (92, 54, 28), start, end, 5)
        pygame.draw.line(screen, (166, 104, 52), start, end, 2)
        pygame.draw.circle(screen, (255, 234, 132), self.rect.center, 7, 1)
