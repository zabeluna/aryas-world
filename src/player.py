# src/player.py
import pygame

SPEED = 180
DASH_SPEED = 500
DASH_DURATION = 0.15
DASH_COOLDOWN = 1.5

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.hp = 100
        self.max_hp = 100
        self.color = (255, 180, 50)  # Amarelo cachorro

        self.dash_timer = 0.0
        self.dash_cooldown_timer = 0.0
        self.is_dashing = False
        self.dash_dir = (0, 0)

        self.waypoints = []

    def update(self, dt, keys, game_map, path):
        self.dash_cooldown_timer = max(0, self.dash_cooldown_timer - dt)

        if self.is_dashing:
            self.dash_timer -= dt
            dx = self.dash_dir[0] * DASH_SPEED * dt
            dy = self.dash_dir[1] * DASH_SPEED * dt
            self._move(dx, dy, game_map)
            if self.dash_timer <= 0:
                self.is_dashing = False
            return

        # Movimento por teclado (prioridade sobre path)
        vx, vy = 0, 0
        if keys[pygame.K_LEFT]  or keys[pygame.K_a]: vx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: vx =  1
        if keys[pygame.K_UP]    or keys[pygame.K_w]: vy = -1
        if keys[pygame.K_DOWN]  or keys[pygame.K_s]: vy =  1

        if vx != 0 or vy != 0:
            self.dash_dir = (vx, vy)
            self._move(vx * SPEED * dt, vy * SPEED * dt, game_map)
            path.clear()
        elif path:
            # Movimento por pathfinding
            tile_size = game_map.tile_size
            target_x = path[0][0] * tile_size + tile_size // 2
            target_y = path[0][1] * tile_size + tile_size // 2
            dx = target_x - self.rect.centerx
            dy = target_y - self.rect.centery
            dist = (dx**2 + dy**2) ** 0.5
            if dist < 4:
                path.pop(0)
            else:
                nx, ny = dx/dist, dy/dist
                self.dash_dir = (nx, ny)
                self._move(nx * SPEED * dt, ny * SPEED * dt, game_map)

    def _move(self, dx, dy, game_map):
        self.rect.x += int(dx)
        if game_map.collides(self.rect):
            self.rect.x -= int(dx)
        self.rect.y += int(dy)
        if game_map.collides(self.rect):
            self.rect.y -= int(dy)

    def use_skill(self):
        if self.dash_cooldown_timer <= 0 and not self.is_dashing:
            self.is_dashing = True
            self.dash_timer = DASH_DURATION
            self.dash_cooldown_timer = DASH_COOLDOWN

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def reached_waypoint(self):
        return False  # Gerenciado no main

    def draw(self, screen):
        color = (255, 100, 100) if self.is_dashing else self.color
        pygame.draw.ellipse(screen, color, self.rect)
        # Orelhas
        ear_left  = pygame.Rect(self.rect.x,      self.rect.y - 8, 10, 12)
        ear_right = pygame.Rect(self.rect.right-10, self.rect.y - 8, 10, 12)
        pygame.draw.ellipse(screen, (200, 130, 30), ear_left)
        pygame.draw.ellipse(screen, (200, 130, 30), ear_right)